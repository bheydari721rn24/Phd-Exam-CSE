# Logic: individually derived solutions, revision 2026-10-11

These solutions preserve the seven authentic examination contracts and option order. All answers are independently derived, not attributed to an official key. Each numbered section corresponds to the frozen library inventory. The parameterized exercises intentionally separate a concrete count, a general proof, and a boundary test; a numerical answer alone does not complete the solution.

## Q1

**Correct option: 4.** A universal statement fails as soon as one quantified input has no permitted witness. For statement (a), set $x=4$. The required inequality is $4<y$, but every $y$ in the domain is at most 4. Thus the existential statement fails at this input and the outer universal statement is false. Inputs 0 through 3 having witnesses cannot repair the failure at 4.

For statement (b), an implication is false only when its antecedent is true and its consequent is false. Choose $x=3$ and $y=4$. Then $R(3,4)$ is true, but the cyclic function gives $f(3)=4$ and $f(4)=0$. Consequently $R(f(3),f(4))$ is the false inequality $4<0$. This single pair refutes the universally quantified implication.

| Claim | Tested input | Antecedent or required witness | Result |
| --- | --- | --- | --- |
| (a) | $x=4$ | No domain object exceeds 4 | False |
| (b) | $(x,y)=(3,4)$ | $3<4$ is true; $4<0$ is false | False |

Options 1 and 3 incorrectly accept (a); options 2 and 3 incorrectly accept (b). The important distinction is between an ordered domain and a cyclic successor: wrapping from the maximum back to the minimum destroys preservation of the strict order. Checking $x=0,y=1$ would support (b) for that pair only, not establish its universal validity.

## Q2

**Correct option: 1.** Evaluate the function argument before consulting the relation. The only true relation pairs are $(0,1),(1,2),(2,0)$. In particular, $R(f(y),0)$ is true precisely when $f(y)=2$, which happens only at $y=1$.

| Assignment to $x$ | $y$ | $R(x,y)$ | $f(y)$ | $R(f(y),0)$ | Implication |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 2 | 1 | 1 |
| 0 | 2 | 0 | 0 | 0 | 1 |
| 2 | 0 | 1 | 1 | 0 | 0 |
| 2 | 1 | 0 | 2 | 1 | 1 |
| 2 | 2 | 0 | 0 | 0 | 1 |

The universal conjunction of the first three implication values is true, so the first assignment satisfies the formula. The second assignment fails at $y=0$, so it does not satisfy the formula. Notice that a false consequent in a row with a false antecedent does not refute the implication. Options 2 and 4 reject the valid first assignment; options 2 and 3 accept the invalid second assignment. The table also makes clear why replacing the universal quantifier with an existential quantifier would change the answer: each assignment has at least one vacuously true row.

## Q3

**Correct option: 3.** A canonical CNF contains a maxterm for each false row, not for each true row. The supplied true rows are 110, 100, 011 and 001; therefore the false rows are 000, 010, 101 and 111, in variable order $A,B,C$.

| False row | Clause false on precisely that row |
| --- | --- |
| 000 | $A\lor B\lor C$ |
| 010 | $A\lor\neg B\lor C$ |
| 101 | $\neg A\lor B\lor\neg C$ |
| 111 | $\neg A\lor\neg B\lor\neg C$ |

At 111 all three literals in statement (a)'s clause are false. At 000 all three literals in statement (b)'s clause are false. Both clauses therefore belong to the canonical product. Options 1 and 2 omit one required clause; option 4 omits both.

For a semantic cross-check, the function is true exactly when $A$ and $C$ differ, regardless of $B$. It is therefore equivalent to $A\oplus C$. This simpler expression does not contradict the four-clause canonical form: the canonical form must mention every variable in each clause even when one variable is semantically irrelevant. Do not use the shorter two-variable expression to infer that the requested three-variable canonical CNF contains only two clauses.

## Q4

**Correct option: 3.** Interpret the two-digit domain labels as object names. Relation membership is directed: $E(a,b)$ does not imply $E(b,a)$. The girls are 03, 06 and 09. Their outgoing edges to boys are, respectively, 02, 08 and 02.

| Girl | Boys she loves | Number of qualifying targets |
| --- | --- | --- |
| 03 | {02} | 1 |
| 06 | {08} | 1 |
| 09 | {02} | 1 |

Each girl has exactly one boy target, so statement (a) is true. Sharing the target 02 is permitted: unique existence constrains the targets of one input, whereas injectivity would constrain targets across different inputs. The extra edge $(04,03)$ starts at a boy and ends at a girl, providing the two witnesses for statement (b). Thus (b) is also true.

Option 1 overlooks $(04,03)$; option 2 confuses shared targets with failure of unique existence; option 4 makes both errors. A complete relational evaluation must inspect incoming and outgoing edges separately. Reversing $(04,03)$ would establish that a girl loves a boy, but would not witness the actual existential claim about a boy loving a girl.

## Q5

**Correct option: 4.** First fix an arbitrary object $x$. The statement imposes a requirement on $x$ only if $x$ is a boy and $x$ likes Maryam. That restriction belongs in the antecedent of the outer implication, rather than in a conjunction asserting that every domain object has those properties.

Once $x$ qualifies, fix an arbitrary object $y$. The dislike requirement applies only if $y$ is a boy, Maryam likes $y$, and $y$ differs from $x$. The last condition translates the word “other.” Hence the complete dependency is

$$\forall x\big((B(x)\land E(x,M))\Rightarrow\forall y((B(y)\land E(M,y)\land y\ne x)\Rightarrow H(x,y))\big).$$

Options 1 and 2 use an outer conjunction. A domain containing Maryam and one qualifying boy already shows the problem: the original sentence can hold while those options demand that Maryam herself be a boy liking Maryam. Option 3 omits the inequality. To distinguish it from option 4, take one boy $b$ who likes Maryam, whom Maryam likes, and who does not dislike himself; assume there are no other qualifying boys. The original statement is true because there is no “other” boy to consider, but option 3 demands $H(b,b)$ and is false.

Direction also matters: $E(x,M)$ and $E(M,y)$ express different relation edges. Neither symmetry of liking nor existence of a qualifying boy is assumed. If no boy likes Maryam, the intended universal conditional is vacuously true.

## Q6

**Correct option: 2.** The function is true at 111, 110, 101 and 011. Its false rows are 000, 001, 010 and 100. Construct the clause for each false row by using an unnegated atom at a zero position and a negated atom at a one position.

| False row | Corresponding maxterm |
| --- | --- |
| 000 | $p\lor q\lor r$ |
| 001 | $p\lor q\lor\neg r$ |
| 010 | $p\lor\neg q\lor r$ |
| 100 | $\neg p\lor q\lor r$ |

Their conjunction is exactly option 2, with clause order immaterial. Each clause eliminates its designated false row and is true on every other row, proving the construction rather than merely matching its appearance.

Option 1 is the correct canonical DNF, but the requested representation is a product of sums. It is semantically correct and syntactically the wrong normal form. In the original scanned option 3, the clause $\neg p\lor\neg q\lor\neg r$ vanishes at 111 even though the function must be true there. Its other clauses exclude 010, 101 and 110, so it is not equivalent to the supplied table. The original scanned option 4 is the DNF of the false rows 001, 000, 010 and 100: it computes the complement, not the required function. These two options were mistranscribed in the earlier edition and have now been corrected against the image of the booklet. The function can also be described as “at least two of the three atoms are true”; this supplies a quick conceptual check on every row.

## Q7

**Correct option: 4.** Number rows using $i=4p+2q+r$. The biconditional requires $p=q$. If both are zero, the implication is true for either value of $r$, giving rows 0 and 1. If both are one, the implication requires $r=1$, giving row 7. No row with $p\ne q$ survives.

| $pqr$ | Index | $p\Rightarrow r$ | $p\Leftrightarrow q$ | Conjunction |
| --- | --- | --- | --- | --- |
| 000 | 0 | 1 | 1 | 1 |
| 001 | 1 | 1 | 1 | 1 |
| 010 | 2 | 1 | 0 | 0 |
| 011 | 3 | 1 | 0 | 0 |
| 100 | 4 | 0 | 0 | 0 |
| 101 | 5 | 1 | 0 | 0 |
| 110 | 6 | 0 | 1 | 0 |
| 111 | 7 | 1 | 1 | 1 |

The product of maxterms must list the zero indices, so it is $\prod M(2,3,4,5,6)$. Option 1 is an equivalent sum of minterms, but not the requested product representation. Option 2 wrongly makes rows 0 and 1 false and omits false rows 2 and 5. Option 3 selects an incorrect set of true rows. Checking row 0 alone refutes options 2 and 3; rejecting option 1 requires understanding the requested syntax, not finding a countervaluation, because it computes the same function.

## Q8

**Correct option: 2.** The equality constraint $p\Leftrightarrow q$ lets us replace $q$ by $p$, but it does not create an additional independent choice. Split on the shared value. If $p=q=0$, the implication to $r$ is automatically true. The XOR forces $s=1-r$, producing assignments 0001 and 0010 in order $p,q,r,s$. If $p=q=1$, the implication forces $r=1$ and the XOR then forces $s=0$, producing 1110. These two cases are disjoint and exhaust all possibilities, so there are three models.

Option 1 misses one of the two assignments in the zero case. Option 3 treats $r$ as free even when $p=1$. Option 4 counts a redundant choice for one of the equal atoms. The satisfying assignments themselves are a compact certificate: each can be substituted into every conjunct, and the case split proves there cannot be any others.

For comparison, replacing XOR by inclusive OR changes the zero case to three $(r,s)$ pairs and the one case to two, producing five models. Replacing the implication by a biconditional would instead leave only two models. These variations explain which operator is responsible for each restriction.

## Q9

**Correct option: 2.** With $p$ as the most significant bit, the true index set is $T=\{1,2,4,7\}$. The false set is its complement within $\{0,\ldots,7\}$, namely $Z=\{0,3,5,6\}$. A canonical product of maxterms records $Z$, giving $\prod M(0,3,5,6)$.

For example, index 5 is row 101. Its maxterm is $\neg p\lor q\lor\neg r$, which is false precisely at 101. Index 3 is row 011 and yields $p\lor\neg q\lor\neg r$. Constructing these clauses confirms both the indexing convention and the literal polarity.

Option 1 lists true rows as maxterms and therefore describes the complement of the required function. Option 3 also describes the complement, using its true-row minterms. Option 4 misclassifies index 2 as false and index 5 as true; substituting either row refutes it. The true rows have an odd number of ones, so the function is three-variable parity. This observation is a useful second derivation of the truth set, but does not replace the required complement operation when converting to maxterm notation.

## Q10

**Correct option: 4.** Because $R(x,y)$ means $y=x+1$ modulo 4, every true relation edge fixes its destination. In I, the first edge forces $y=x+1$, while the reverse edge requires $x=y+1=x+2$ modulo 4. This would require $2\equiv0\pmod4$, which is false. Thus no input has the requested two-edge return, and I is false.

In II, the first two edges force $y=x+1$ and $z=x+2$. The final edge $R(z,f(x))$ requires $f(x)=z+1=x+3$ modulo 4, but by definition $f(x)=x+1$. Again the required difference is 2 modulo 4, so II is false.

| Input $x=0$ | Forced path | Required endpoint | Actual endpoint |
| --- | --- | --- | --- |
| I | $0\to1\to2$ | 0 | 2 |
| II | $0\to1\to2\to3$ | $f(0)=1$ | 3 |

Both calculations fail for every $x$, which is stronger than the single counterexample needed to reject each universal. Options 1 and 3 incorrectly accept I; options 2 and 3 incorrectly accept II. A cyclic relation provides successors, but not necessarily the return paths demanded by a nested quantified formula. Changing the cycle length to 2 would make both modular conditions hold, illustrating why domain size matters.

## Q11

**Correct option: 1.** Begin with an arbitrary researcher $x$. Existence requires a paper $y$ with $V(x,y)$. Uniqueness then says that any paper $z$ reviewed by the same researcher must equal $y$. The quantifier over $z$ must remain inside the scope of the selected researcher and the selected paper.

$$\forall x\big(R(x)\Rightarrow\exists y(P(y)\land V(x,y)\land\forall z((P(z)\land V(x,z))\Rightarrow z=y))\big).$$

Consider two researchers who both review one paper and no other paper. This model satisfies the intended sentence and option 1. Option 2 fails in that model because it requires each paper to have exactly one researcher; it reverses the direction of uniqueness. Option 3 requires every domain object to be a researcher, so the paper object itself is a counterexample if it is not also a researcher. Option 4 requires one shared paper for all researchers and omits unique existence. Two researchers each reviewing a different paper satisfy the intended statement while refuting option 4. Conversely, one researcher reviewing two papers can satisfy option 4 while refuting the intended statement.

Uniqueness concerns qualifying papers, so non-paper objects in the domain are not forbidden from participating in $V$ unless another premise forbids it. Read the restricted predicate inside the uniqueness condition rather than silently imposing a stronger relation type.

## Q12

**Correct option: 2.** The interpretation makes $A(x)$ false at every domain object. For each object, the implication has truth value $0\Rightarrow B(x)=1$, independently of $B(x)$. The universal conjunction of these true instances is true. By contrast, every instance of $A(x)\land B(x)$ is false, so no object witnesses the existential statement.

| $A(x)$ | $B(x)$ | $A(x)\Rightarrow B(x)$ | $A(x)\land B(x)$ |
| --- | --- | --- | --- |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 |

Option 1 treats a vacuously true conditional as evidence that an $A$-object exists. Options 3 and 4 incorrectly demand an existing $A$-witness for universal truth; option 3 additionally accepts an impossible existential witness. The domain is nonempty in the exercise, but the restricted set of $A$-objects is empty. These are different assumptions.

If the second formula had instead been $\exists x(A(x)\Rightarrow B(x))$, it would be true on the stated nonempty domain, since every object witnesses the implication. This variation demonstrates why restricted existential quantification uses conjunction rather than implication.

## Q13

**Correct option: 2.** Rewrite the third premise $\neg q\lor s$ as $q\Rightarrow s$. To establish $p\Rightarrow s$, assume $p$. The first premise gives $q$ by modus ponens, and the rewritten third premise then gives $s$. Discharging the assumption proves the conditional. The premise $r\Rightarrow q$ is not needed for this particular conclusion.

A second proof starts from a proposed countermodel. If $p=1$ and $s=0$, the first premise forces $q=1$, but the third premise then becomes $0\lor0=0$, a contradiction. Thus no countermodel to option 2 satisfies all premises.

For options 1 and 3, take $(p,q,r,s)=(0,1,0,1)$. All premises are true, but $s\Rightarrow p$ and $q\Rightarrow p$ are false. For option 4, take $(0,0,0,0)$. All premises remain true, while $\neg s\Rightarrow r$ is false. These complete valuations refute each alternative with the exact entailment criterion. Reversing the direction of an implication is not licensed by chaining forward implications; only the contrapositive preserves equivalence.

## Q14

**Correct option: 4.** In the directed cycle $p\Rightarrow q$, $q\Rightarrow r$, $r\Rightarrow p$, a false implication occurs exactly on an edge whose source is 1 and target is 0. The two constant assignments 000 and 111 contain no such edge and make all three implications true. Each of the six remaining assignments contains exactly one such edge.

| $pqr$ | $p\Rightarrow q$ | $q\Rightarrow r$ | $r\Rightarrow p$ | Number true |
| --- | --- | --- | --- | --- |
| 000 | 1 | 1 | 1 | 3 |
| 001 | 1 | 1 | 0 | 2 |
| 010 | 1 | 0 | 1 | 2 |
| 011 | 1 | 1 | 0 | 2 |
| 100 | 0 | 1 | 1 | 2 |
| 101 | 0 | 1 | 1 | 2 |
| 110 | 1 | 0 | 1 | 2 |
| 111 | 1 | 1 | 1 | 3 |

Therefore exactly six assignments meet the requested condition. Option 1 counts only the constant assignments, which do not qualify. Option 2 counts choices of the false edge but overlooks that each choice occurs in two assignments. Option 3 misses two qualifying assignments. This argument depends on a three-node cycle: a longer cycle can have several 1-to-0 transitions, so “every nonconstant assignment has exactly one false implication” is not a general cycle law.

## Q15

**Correct option: 2.** For a fixed input $x$, “exactly one solution” is the conjunction of at least one solution and at most one solution. Its negation can therefore occur in two disjoint ways: there is no solution, or there are at least two distinct solutions. Negating the outer universal statement requires only one input with either failure.

$$\neg\forall x\exists!y\,S(x,y)\equiv\exists x\big((\forall y\neg S(x,y))\lor\exists y\exists z(S(x,y)\land S(x,z)\land y\ne z)\big).$$

For an explicit zero-solution model, let $D=\{0,1\}$ and $S=\{(1,1)\}$. Input 0 has no solution, whereas input 1 has one; the negation holds without every input failing. For a multiple-solution model, use $S=\{(0,0),(0,1),(1,1)\}$. Input 0 has two solutions and input 1 still has exactly one.

Options 1 and 4 incorrectly require failure at every input. Option 3 misses both the zero-solution case and the possibility of three or more solutions. Distinctness $y\ne z$ is essential: without it, a single solution could be chosen twice and falsely counted as a uniqueness failure. Unique existence is not an additional primitive counting convention; expanding its existence and uniqueness parts makes its negation transparent.

## Q16

**Correct option: 2.** There are seven labelled Boolean variables. The biconditional identifies the first two bits, so the constrained triple can only be 000, 001 or 111: the combination with $x_2=1,x_3=0$ is eliminated by the implication. Four remaining bits are free, producing $3\cdot2^4=48$ assignments.

This count can be checked without enumerating 128 rows. Each of the three allowed triples has exactly sixteen distinct extensions, and extensions from different triples cannot coincide. Hence addition across triples and multiplication within a triple are both justified.

Option 1, 96, is twice the answer: it counts an extra choice for $x_1$ even though $x_1=x_2$. Option 3, 64, allows all four $(x_2,x_3)$ pairs and ignores the implication. Option 4, 32, treats that implication as a biconditional and permits only 000 and 111. Of all $2^7=128$ assignments, a fraction $48/128=3/8$ satisfy the constraints. Equivalently, equality keeps half the assignments, and, conditional on that equality, the implication keeps three quarters. This conditional calculation explains why multiplying fractions requires checking the distribution after the first constraint.

## Q17

**Correct option: 1.** Ten variables are present. The first three have exactly the allowed triples 000, 001 and 111. Each triple has $2^7=128$ extensions on the other seven labelled variables, so the answer is $3\cdot128=384$.

Option 2, 512, enforces equality but not implication. Option 3, 256, enforces both equality and a stronger second equality. Option 4, 768, incorrectly treats the first bit as free after its value has been identified with the second bit. These are counts of different constraint systems, not alternative ways of evaluating the same system.

Suppose, as a follow-up, the last free variable is additionally required to be true. Each allowed triple then has $2^6$ extensions and the count becomes 192. Requiring that last variable to equal $x_3$ has the same count, even though it defines a different set of assignments: for each constrained triple, the last bit is fixed to exactly one value. In contrast, requiring $x_3=1$ retains two of the three triples, giving $2\cdot128=256$. Identical-looking extra restrictions can affect a biased constrained variable differently from an independent free variable.

## Q18

**Correct option: 4.** Among the $n+2$ variables, three belong to the constrained component. Its allowed assignments are 000, 001 and 111. Thus $n-1$ independent free variables remain. A model consists uniquely of one allowed triple and one bit string of length $n-1$.

$$N(n)=3\cdot2^{n-1},\qquad n\ge1.$$

This bijection proves both completeness and absence of duplicate counting. At $n=1$, there are no free variables; the empty bit string has one choice, so the count is 3, agreeing with the direct list. Increasing $n$ by one adds a genuinely free bit, so $N(n+1)=2N(n)$.

Option 1 allows four constrained triples rather than three. Option 2 keeps only two triples, effectively replacing the implication by equivalence. Option 3 has the correct three triples but uses $n$ instead of $n-1$ free bits, so it is double the answer. Expressions involving zero or negative numbers of free variables must not be extended beyond the exercise's domain. The formula depends on labelled Boolean variables and these two stated constraints; additional constraints involving the remaining variables require a new extension count.

## Q19

**Correct option: 3, with the explicit hypothesis $n\ge3$.** Before adding another equality, the $n-1$ free variables are independent. At least two such variables are available only if $n-1\ge2$. Fix two distinct free variables, say $x_4$ and $x_5$. Their four possible ordered values are 00, 01, 10 and 11; equality retains exactly 00 and 11. No condition on the constrained triple changes.

$$N_{\mathrm{new}}(n)=3\cdot2\cdot2^{n-3}=3\cdot2^{n-2}=\frac{N(n)}2.$$

For $n=3$, this reduces the count from 12 to 6, furnishing the smallest valid example. For $n=1$ or $n=2$, there are fewer than two free variables and the proposed added equality cannot even be chosen as described. The previous answer omitted this condition; the revised stem now states it.

Option 1 ignores the forbidden implication pair 10. Option 2 is refuted by replacing $x_2\Rightarrow x_3$ with $x_2\Leftrightarrow x_3$: three triples become two. Option 4 incorrectly increases the number of models by adding a constraint. A constraint can preserve or reduce a model set, never enlarge it. Even “equality halves the count” requires independent free bits: an already implied equality removes no models, whereas an incompatible equality can remove all of them.

## Q20

**Correct option: 3.** Interpreting a unary predicate on five labelled objects is equivalent to choosing its true subset. Each object independently belongs or does not belong, so there are $2^5=32$ interpretations before imposing the conditions. The existential condition forbids the empty subset. The negated universal condition forbids the full five-element subset. These are two distinct interpretations, leaving $32-2=30$.

The same result follows by subset size: $\binom51+\binom52+\binom53+\binom54=5+10+10+5=30$. This second derivation shows that the exercise counts all nonempty proper subsets, not just singleton witnesses.

Option 1 counts only half of all subsets and has no justification from the two restrictions. Option 2 counts just singleton subsets. Option 4 excludes only the empty subset and still includes the interpretation that makes the predicate universally true. If one specified object had to satisfy the predicate, there would instead be $2^4-1=15$ interpretations: membership of that object is fixed and only the all-true interpretation must be removed. The revised calculation explicitly separates existence of a witness from choosing one designated witness.

## Q21

**Correct option: 2.** Eight labelled objects give $2^8=256$ predicate interpretations. Exactly one is all false and exactly one is all true. Neither is allowed, so the answer is 254. The two excluded interpretations are disjoint because the domain is nonempty.

Option 1 counts only the eight singleton subsets. Option 3, 255, excludes just one of the forbidden interpretations. Option 4, 128, is the count obtained by fixing the truth value of one designated object, a condition absent from the stem.

A useful cross-check pairs each allowed subset with its complement. Both members of the pair remain nonempty and proper, and no subset equals its own complement on a nonempty domain. Thus the answer must be even, as 254 is. For a more selective follow-up, interpretations with exactly three true objects number $\binom83=56$; interpretations containing a particular named object number $2^7-1=127$ after excluding the full set. These are different restrictions from merely requiring at least one true and at least one false object.

## Q22

**Correct option: 1.** Let $D$ contain $n\ge1$ labelled objects and let $T\subseteq D$ be the true set of the unary predicate. The formula requires $T\ne\varnothing$ and $T\ne D$. The power set has $2^n$ members, and the two excluded members are distinct, giving $2^n-2$.

$$\sum_{k=1}^{n-1}\binom nk=2^n-2.$$

At $n=1$ the sum has no terms and the formula gives zero: a singleton domain cannot contain both a true object and a false object. At $n=2$, exactly the two singleton subsets qualify. These small cases test the assumptions and the subtraction.

Option 2 still includes one excluded extreme subset. Option 3 counts interpretations with one object's value fixed, not interpretations satisfying both global conditions. Option 4 counts singletons only, agreeing accidentally with the answer at $n=2$ but failing, for instance, at $n=3$ where the answer is 6. A formula that agrees in one small case is not thereby a general counting law. The $n=0$ convention is handled separately in the next question because the excluded empty and full subsets then coincide.

## Q23

**Correct option: 4.** Under an explicitly permitted empty-domain convention, $\exists xP(x)$ is false: there is no object that could serve as a witness. The universal statement $\forall xP(x)$ is true: there is no counterexample object. Their required combination $\exists xP(x)\land\neg\forall xP(x)$ is therefore false.

The subset perspective gives the same answer. The empty domain has exactly one subset, which is simultaneously empty and full. Excluding it leaves zero interpretations. Substituting $n=0$ into $2^n-2$ would yield $-1$, exposing a violated assumption rather than a negative model count. The subtraction of two forbidden interpretations was valid only when those interpretations were distinct.

Option 1 supplies a nonexistent existential witness. Option 2 reverses the meaning of universal quantification by requiring a witness instead of ruling out counterexamples. Option 3 mistakes proper subsets for singleton subsets; on a three-object domain, a two-object subset is proper. Standard first-order structures normally have nonempty domains, and a constant symbol cannot designate an object of an empty domain. This boundary exercise explicitly changes that convention; do not silently carry it into ordinary first-order problems.

## Q24

**Correct option: 1.** Represent the relation by a five-by-five zero-one matrix, with rows for the first argument. For each fixed input $x$, the sentence requires at least one true entry in its row. The row is any subset of five targets except the empty subset, giving $2^5-1=31$ choices. Different rows control different ordered pairs, so their choices are independent.

$$31^5=31^2\cdot31^2\cdot31=961\cdot961\cdot31=28\,629\,151.$$

Option 2 subtracts only the all-zero matrix from $2^{25}$; a matrix can contain many ones and still have an empty row. Option 3 counts exactly-one entries per row, not at least one. Option 4 is $16^5$ and would result from fixing one entry in every row while allowing the other four arbitrarily; no such named entry is required.

For a concrete distinction, rows of sizes 2,1,3,1,4 all qualify. A matrix whose first row is empty and whose other four rows are full fails, even though it has twenty true entries. The semantic unit is one row per universally quantified input, so a global nonzero condition is insufficient.

## Q25

**Correct option: 4.** Each of the eight rows can be any of $2^8-1=255$ nonzero bit strings. Independence across the eight rows gives $255^8=17\,878\,103\,347\,812\,890\,625$. Keeping the power expression until the final arithmetic avoids confusing the structural count with the large decimal representation.

Option 1 is $2^{64}-1$, which excludes only the entirely empty relation. Option 2 is $8^8$, which imposes exactly one target for each input. Option 3 is $128^8$; it would correspond to requiring one specified bit in every row and leaving the other seven unrestricted. Each of these describes a different family of matrices.

As a probability check, under a uniformly chosen relation each row is nonempty with probability $255/256$. Thus the probability of satisfying the universal-existential sentence is $(255/256)^8$, and multiplying it by the $2^{64}$ total relations reproduces $255^8$. Row independence is justified by disjoint entries; the quantified witnesses need not be distinct and may be shared across rows.

## Q26

**Correct option: 3.** For each of $n\ge1$ inputs, choose a nonempty subset of the $n$ targets. There are $2^n-1$ choices. A sequence of $n$ such subsets determines exactly one relation, and every satisfying relation determines exactly one sequence. Therefore

$$N(n)=(2^n-1)^n.$$

This construction is a bijective proof of the product rule. At $n=1$ only the single true matrix entry works. At $n=2$, the nonempty row patterns are 01, 10 and 11, producing $3^2=9$ relations. At $n=3$, the seven nonempty row patterns produce $7^3=343$ relations.

Option 1 restricts every row to a singleton. Option 2 gives $2^{n-1}$ choices per row, as if one target had been fixed in advance. Option 4 requires merely one true entry somewhere in the whole matrix. A rectangular variant with $a$ labelled inputs and $b$ labelled targets gives $(2^b-1)^a$ for $b\ge1$: the row length controls choices and the number of rows controls the exponent. This generalization checks which part of the square-domain formula represents each quantified variable.

## Q27

**Correct option: 2.** Replacing “at least one target” by “exactly one target” changes each permitted row from an arbitrary nonempty subset to one of $n$ singleton subsets. The relation is then the graph of a total function, and the count changes from $(2^n-1)^n$ to $n^n$.

On a two-object domain, the matrix with rows 10 and 10 is a function graph: each row has exactly one entry, though the second column is empty. This refutes option 1, which incorrectly imposes column nonemptiness. The matrix with rows 11 and 10 is total but not functional, refuting option 3. The matrix with rows 10 and 00 has a true entry but is not total, refuting option 4.

| Condition | What each row permits | Square-domain count |
| --- | --- | --- |
| At least one target | Any nonempty subset | $(2^n-1)^n$ |
| Exactly one target | One singleton subset | $n^n$ |
| At most one target | Empty or singleton subset | $(n+1)^n$ |

The last line is a useful boundary: existence and uniqueness are separate constraints. Column conditions describe surjectivity or common witnesses and need their own analysis.

## Q28

**Correct option: 2.** Exactly one target for each of five inputs gives five independent choices per row. Therefore there are $5^5=3125$ function graphs. No requirement prevents two inputs from choosing the same target.

For example, assigning every input to the first target is a valid function and gives five rows each equal to 10000. It would fail an injectivity condition, but no such condition is present. Conversely, a row 11000 fails uniqueness even though it satisfies existence.

Option 1 is the total number $2^{25}$ of unrestricted relations. Option 3 counts nonempty rows, allowing several targets per input. Option 4, $5!=120$, adds the absent requirement that distinct inputs have distinct targets. A function graph contains exactly five true ordered pairs, but not every five-element relation is a function graph: a relation with two entries in one row and none in another is a counterexample. Consequently $\binom{25}{5}$ would also be an incorrect shortcut. One must choose a target in each row, not just five arbitrary positions.

## Q29

**Correct option: 1.** A total function on eight labelled objects selects one of eight targets independently for each input. Thus $8^8=16\,777\,216$ function graphs satisfy the unique-existence condition.

Option 2, $255^8$, allows every nonempty row and therefore admits rows with multiple targets. Option 3, $8!=40320$, counts only bijections. Option 4, $2^{64}$, imposes neither existence nor uniqueness. Choosing a common target for all eight inputs is permitted and yields eight distinct constant functions, one for each target.

For a further conceptual check, suppose two specified distinct inputs must share their target. Their common target has eight choices, and the other six inputs have eight independent choices each, giving $8^7$. If they must instead have different targets, the count is $8\cdot7\cdot8^6$. These two disjoint families sum to $8^8$, verifying that unique output for one input does not mean different outputs for different inputs.

## Q30

**Correct option: 4.** Label the inputs $d_1,\ldots,d_n$. A function is specified by the output vector $(f(d_1),\ldots,f(d_n))$. Each coordinate has $n$ possible values, with repetitions allowed. Thus the product rule gives $n^n$ for $n\ge1$.

The relation matrix interpretation is equivalent: each row has one true position. At $n=2$, the output vectors are $(0,0),(0,1),(1,0),(1,1)$, giving four functions; only two are permutations. At $n=1$, the sole function maps the object to itself.

Option 1 permits several true positions in a row. Option 2 disallows repeated outputs. Option 3 permits all subsets of the ordered-pair universe. For a rectangular relation from an $a$-object domain to a $b$-object codomain, the count is $b^a$. If the codomain is empty and the domain is nonempty there is no function; if the domain is empty there is one empty function, even into an empty codomain. These conventions are separate from the exercise's nonempty square domain and should be derived from the output-vector construction rather than an unexplained use of $0^0$.

## Q31

**Correct option: 3.** Add the condition that distinct arguments choose distinct targets. A total function on a finite $n$-object domain is then injective. Its image contains $n$ distinct elements of an $n$-element codomain, so its image is the entire codomain. It is therefore a permutation.

Choose the first output in $n$ ways, the second in $n-1$ ways, and continue until the final output has one remaining choice. This yields $n!$. The falling factors, rather than $n$ repeated at every position, express the loss of independence caused by distinctness.

Option 1 would require $n^2$ relation entries rather than one per row and is false for $n>1$. Options 2 and 4 claim that unique existence alone forbids shared outputs; a two-object constant function refutes both. The finite equal-size assumption is essential for the permutation conclusion. With two inputs and three targets, an injective map need not be onto. On the infinite natural-number domain, the map $k\mapsto k+1$ is injective and non-surjective even though domain and codomain are the same set. Do not transfer the finite counting argument to infinite models.

## Q32

**Correct option: 1.** Odd parity on five bits is false on exactly the even-weight assignments. Their number is

$$\binom50+\binom52+\binom54=1+10+5=16.$$

Each false row supplies one canonical maxterm, so the canonical CNF has sixteen clauses. Each such clause contains five literals, making eighty literal occurrences before any alternative encoding is introduced.

Option 2 counts all 32 rows rather than just false rows. Option 3 counts variables, not clauses. Option 4 subtracts the all-zero false row even though that row must be excluded by a clause. Pairing each assignment with the result of flipping its first bit gives a second proof: the operation switches parity, has no fixed point, and is its own inverse. Hence half the 32 assignments are false. A short expression using XOR gates does not change the number of maxterms required by a canonical CNF over these five original atoms; representation size and truth-table row count are different quantities.

## Q33

**Correct option: 4.** Eight bits give 256 assignments. Flipping one designated bit pairs every even-parity assignment with an odd-parity assignment, so exactly 128 rows are false. Canonical CNF uses one maxterm per false row and therefore has 128 clauses.

The binomial check is $\binom80+\binom82+\binom84+\binom86+\binom88=1+28+70+28+1=128$. Each clause contains eight literals, giving 1024 literal occurrences.

Option 1 counts both true and false rows. Option 2 mistakes the number of input atoms for the number of clauses. Option 3 omits one necessary clause; removing any canonical clause allows its corresponding false assignment to satisfy all the remaining clauses. This last statement follows because a full maxterm is false at exactly one row. It is a stronger verification than merely recounting clauses: it explains why every clause is necessary in this particular full canonical representation.

## Q34

**Correct option: 3.** Assume $n\ge1$. Define a map on bit strings that flips the first coordinate and leaves the other coordinates unchanged. The map is invertible and changes parity, so it is a bijection from even-weight strings to odd-weight strings. Since the two classes partition $2^n$ strings, each has $2^{n-1}$ members. Odd parity is false on the even-weight strings, giving $2^{n-1}$ canonical maxterms.

At $n=1$, odd parity is simply the single bit and its canonical CNF has one clause, agreeing with $2^0$. At $n=2$, the false rows 00 and 11 produce two clauses. The proof requires at least one coordinate to flip; it must not be applied to a zero-variable function.

Option 1 gives a linear count of atoms rather than false rows. Option 2 drops one false row. Option 4 includes all rows. As a refinement, any clause over the original atoms that omits an atom cannot be an implicate of parity unless it is tautological: choose values falsifying that clause, then choose the missing atom so the total parity is odd. This gives a parity model falsifying the proposed shorter clause. Consequently parity's difficulty in ordinary CNF is structural, not just an accident of how the canonical form was constructed.

## Q35

**Correct option: 2.** A chain of $n-1$ binary XOR gates computes parity of $n\ge1$ inputs. By contrast, canonical CNF over the original inputs has $2^{n-1}$ clauses and $n\cdot2^{n-1}$ literal occurrences. These numbers measure different representations; a short circuit may reuse intermediate values and may use a connective absent from CNF clauses.

Option 1 is refuted by 00 and 01 at two inputs, which have different parity. Option 3 reverses the canonical convention: a maxterm excludes a false row. Option 4 confuses one displayed XOR expression with one CNF clause; even two-input XOR needs the clauses $p\lor q$ and $\neg p\lor\neg q$.

Auxiliary-variable encodings can avoid the large expansion. For example, introduce $z$ and enforce $z\Leftrightarrow(p\oplus q)$ by four three-literal clauses, then use $z$ as the next circuit value. A linear chain of such local constraints has linear encoding size. It is not simply an equivalent formula over the original variables: the new variables must be existentially projected away to recover the original Boolean function. Distinguish circuit complexity, CNF over original variables, and CNF with auxiliary variables before comparing their sizes.

## Q36

**Correct option: 2.** Every premise pair permits 00, 01 and 11; only 10 falsifies $p_i\Rightarrow q_i$. Thus all five premises have $3^5=243$ models. In one of those models, the converse $q_i\Rightarrow p_i$ fails exactly at pair 01. The conjunction of all converses is true only if every pair is 00 or 11, giving $2^5=32$ premise models with a true conclusion.

The premise-true/conclusion-false count is therefore $243-32=211$. The subtracted family is a subset of the counted premise models, so complement subtraction is justified.

Option 1, 781, instead counts assignments with at least one 11 pair, a different event. Option 3 counts every premise model without testing the conclusion. Option 4 counts the models in which the conclusion is true, the opposite of the requested countermodel condition. A concrete countermodel has the first pair 01 and the other four pairs 00. Every forward implication is true, while the first converse is false. The exercise counts many such countermodels, but one already suffices to refute entailment.

## Q37

**Correct option: 1.** Eight independent premise pairs yield $3^8=6561$ models. Among them, all eight converse implications hold exactly when every pair is 00 or 11, giving $2^8=256$ models. Hence the countermodel count is $6561-256=6305$.

Option 2 includes the 256 models where the conclusion is true. Option 3 counts those conclusion-true premise models rather than countermodels. Option 4, $4^8-3^8=58975$, counts models with at least one 11 pair among unrestricted pairs; it does not enforce the premise family.

The conditional probability that the conjunction of converses fails, given that all forward implications hold, is $1-(2/3)^8$. This follows because each premise-compatible pair has three equally numerous choices, two of which satisfy its converse. The conditional probability is not the same as the unconditional fraction $6305/4^8$. Identifying the universe of assignments before taking a complement prevents this common error in validity and probability questions.

## Q38

**Correct option: 4.** For $n\ge1$ independent labelled pairs, the premise-compatible alphabet is $\{00,01,11\}$. A countermodel is a length-$n$ word in that alphabet containing at least one occurrence of 01. The total word count is $3^n$; words avoiding 01 use only 00 and 11 and number $2^n$. Thus the answer is $3^n-2^n$.

Counting by the exact number $k$ of failing converses gives a second derivation:

$$\sum_{k=1}^{n}\binom nk2^{n-k}=3^n-2^n.$$

Choose the $k$ positions carrying 01; each remaining position has two choices. This partitions the countermodels by a unique value of $k$, avoiding overlap. At $n=1$ there is exactly one countermodel, 01. Option 1 includes models with no converse failure; option 2 counts just those non-countermodels; option 3 refers to the unrelated event “at least one pair is 11” in a four-choice alphabet. If pair variables are shared, the alphabet product proof must be replaced by a dependency-aware count.

## Q39

**Correct option: 3.** Entailment means that every valuation satisfying all premises also satisfies the conclusion. Its negation is the existence of one valuation satisfying every premise and falsifying the conclusion. Set one pair to 01 and every other pair to 00. This is an explicit countermodel to the converse conjunction, so entailment fails for every $n\ge1$.

Option 1 confuses the converse with the contrapositive. On the pair 01, the forward implication is true and the converse false. Option 2 replaces a universal condition with a majority condition; even a single exceptional valuation invalidates entailment. Option 4 selects a valuation with a false premise, which is outside the set quantified over by entailment and cannot refute it.

Supporting examples are useful for discovering a conjecture but cannot establish validity unless they exhaust the relevant universe or are subsumed by a general proof. Exhaustive propositional search is possible for a fixed finite atom set; exhaustive testing of structures up to a finite size is not a universal validity proof for arbitrary first-order structures. The solution therefore distinguishes a concrete certificate of invalidity from a complete proof of validity.

## Q40

**Correct option: 1.** Five independent pairs supply $4^5=1024$ total assignments. The disjunction is false exactly when every conjunction $p_i\land q_i$ is false. Each pair can then be 00, 01 or 10, giving $3^5=243$ false assignments. The desired count is $1024-243=781$.

Option 2 ignores the disjunction's failure cases. Option 3 counts the false models. Option 4, 32, permits only the pair patterns 00 and 11 and omits satisfying assignments containing 01 or 10 elsewhere. For instance, first pair 11 and all other pairs 01 satisfy the formula and must be counted.

Directly summing the counts “pair $i$ is 11” overcounts assignments where several pairs are 11. For two pairs, the naive sum is $4+4=8$, but the shared assignment 1111 is counted twice; the correct answer is $16-9=7$. Complement counting treats the absence of every successful pair as a product event and avoids the overlap automatically.

## Q41

**Correct option: 4.** The eight pairs use sixteen distinct Boolean atoms, so there are $2^{16}=4^8=65536$ complete assignments. For the disjunction to be false, each pair must avoid 11, leaving three choices per pair and $3^8=6561$ false assignments. Subtracting gives $65536-6561=58975$.

Option 1 counts all assignments, including the all-zero false assignment. Option 2 counts only false assignments. Option 3, 256, treats the eight pair-success values as if each had one equally represented true and one equally represented false state. In fact a conjunction is true for one pair state and false for three; the underlying atom assignments have unequal multiplicities when projected onto conjunction outputs.

Counting assignments with exactly $k$ successful pairs yields $\binom8k3^{8-k}$. Each successful pair must be 11, while each unsuccessful pair has three choices. Summing this expression for $k=1$ through 8 gives 58975 by the binomial theorem. This provides both a verification and a method for a harder “exactly $k$” variant.

## Q42

**Correct option: 3.** With $n\ge1$ pairwise disjoint variable pairs, the complement of at least one successful conjunction is the event that every pair avoids 11. The complete universe has $4^n$ assignments; the complement has $3^n$. Hence

$$N(n)=4^n-3^n=\sum_{k=1}^{n}\binom nk3^{n-k}.$$

The sum partitions by the number of successful pairs and therefore counts each assignment once. At $n=1$, the answer is one, the pair 11. At $n=2$, it is seven, confirmed by the union of the two four-assignment events with their one-assignment intersection removed.

Option 1 counts the complement. Option 2 confuses choices of conjunction outputs with choices of the underlying two-bit states. Option 4 retains every assignment, including all zeros. The theorem requires distinct atoms across pairs. It also uses inclusive disjunction, so assignments with two or more successful pairs qualify. An exclusive condition requiring exactly one successful pair instead has $n\cdot3^{n-1}$ models; this is a different formula.

## Q43

**Correct option: 2.** Independence in the product calculation comes from distinct underlying atoms. If pairs share an atom, their successful or failed states cannot be chosen independently. Consider

$$F=(p\land q)\lor(p\land r)\equiv p\land(q\lor r).$$

When $p=0$, all four $(q,r)$ assignments fail. When $p=1$, three $(q,r)$ assignments satisfy $q\lor r$. Thus there are three satisfying assignments among eight, not the seven obtained from an invalid two-independent-pair model.

Option 1 is refuted by a false assignment with $p=0,q=r=1$; false models are not only the all-zero assignment. Option 3 excludes the assignment where both pairs succeed, although inclusive OR accepts it. Option 4 asserts independence despite the common variable and is refuted by the factorization above.

More generally, $\bigvee_{i=1}^{k}(p\land q_i)$ has $2^k-1$ satisfying assignments on $k+1$ atoms: $p$ must be one and the $q_i$ vector must not be all zero. Factoring shared atoms before counting exposes the correct independent choices. Treating repeated occurrences of the same atom as separate variables changes the Boolean function and the sample space.

## Q44

**Correct option: 2.** A predicate constant on each of five equivalence classes chooses one truth value per class, not per object. Without the nonempty-truth condition there are $2^5=32$ class-label vectors. Exactly one vector is all false, leaving 31 allowed interpretations.

Class sizes do not enter this count because the value assigned to a class determines the value at all its objects. For example, classes of sizes 1,2,4,7,9 still provide five independent Boolean choices. Assigning true to the two-object class is one interpretation, not two interpretations.

Option 1 fixes a class value without any premise requiring that restriction. Option 3 keeps the forbidden all-false interpretation. Option 4 counts only predicates true on exactly one class and misses predicates true on several classes. The “at least one object” condition is equivalent here to “at least one class” because equivalence classes are nonempty. If the question instead asked for exactly two true objects, class sizes would matter: only combinations of classes whose sizes sum to two would qualify.

## Q45

**Correct option: 1.** The eight equivalence classes supply eight independent truth bits. There are $2^8=256$ assignments of those class bits; excluding the all-false assignment leaves 255 predicates.

Option 2 misses the nonempty-truth restriction. Option 3 counts only one true class at a time. Option 4 would fix one named class's bit and is not implied by existence of some true class. The distinction between a designated class and an unspecified class is the same witness distinction that appears in quantified formulas.

Complementation gives a useful alternative view. Every permitted nonempty selection of classes corresponds to a union of those whole classes. Distinct class selections give distinct subsets of the domain because the classes are disjoint and nonempty. This injectivity justifies transferring the power-set count from classes to predicates. If the underlying relation were not an equivalence relation, its connected or directed components would need separate analysis; one cannot simply label arbitrary overlapping groups independently.

## Q46

**Correct option: 4.** Let the equivalence classes be $C_1,\ldots,C_n$, with $n\ge1$. A class-constant predicate's true set is uniquely a union of some selected classes. The selection is any nonempty subset of the $n$ classes, giving $2^n-1$ interpretations.

$$\sum_{k=1}^{n}\binom nk=2^n-1.$$

The sum classifies interpretations by the exact number of true classes. At $n=1$, the only permitted predicate is true on the sole class and hence everywhere. At $n=2$, the selections are the first class, the second class, and both.

Option 1 includes the all-false predicate. Option 2 counts exactly one selected class. Option 3 counts selections containing one prescribed class rather than selections containing any class. If the condition were “some object true and some object false,” the empty and full class selections would both be excluded, yielding $2^n-2$. If all objects are allowed to be false, the count returns to $2^n$. State the existence condition before choosing the subtraction.

## Q47

**Correct option: 3.** The number of class-constant predicates depends on the number of classes, even when those classes have unequal sizes. Once a class is assigned a truth value, every member inherits it. This produces one binary choice per class, and the nonempty-truth condition removes the one all-false class vector.

For a concrete model with class sizes 1,2 and 3, the seven nonempty selections are $\{C_1\},\{C_2\},\{C_3\},\{C_1,C_2\},\{C_1,C_3\},\{C_2,C_3\},\{C_1,C_2,C_3\}$. The corresponding numbers of true objects are 1,2,3,3,4,5,6. Thus seven interpretations remain, while the distribution of true-object counts depends on the sizes.

Option 1 uses the number of relation pairs, which does not count independent class bits. Option 2 violates constancy by choosing values separately within a class. Option 4 adds an equal-size assumption absent from the definition of equivalence.

For the harder variant “exactly $t$ true objects,” class sizes $s_i$ matter through the coefficient of $z^t$ in $\prod_i(1+z^{s_i})$. Each factor chooses whether to include that whole class. In the example, the coefficient of $z^3$ is two, corresponding to $C_3$ or $C_1\cup C_2$. This distinguishes the unrestricted count from a weighted count.

## Q48

**Correct option: 1.** Negate the statement one quantifier at a time:

$$\neg\forall x\exists y\,R(x,y)\equiv\exists x\forall y\neg R(x,y).$$

In a five-by-five matrix this means at least one completely empty row. There are $2^{25}=33554432$ unrestricted relations. Relations with no empty row number $31^5=28629151$. The desired complementary count is $33554432-28629151=4925281$.

Option 2 counts the opposite event. Option 3 excludes only the all-zero matrix, nearly the reverse of the required empty-row event. Option 4 is $5\cdot2^{20}$: it chooses a named empty row and then fills the remaining entries. A matrix with two empty rows is counted twice by that procedure, and the all-zero matrix five times, so it is not a count of distinct matrices.

For a smaller two-row check, the correct count is $16-9=7$. Counting a selected empty row would give $2\cdot4=8$, overcounting the entirely zero matrix once. This explicit example reveals the overlap behind the incorrect five-row shortcut.

## Q49

**Correct option: 4.** An eight-by-eight relation has 64 independent entries, so its universe contains $2^{64}=18446744073709551616$ matrices. Matrices whose rows are all nonempty number $255^8=17878103347812890625$. Subtracting gives $568640725896660991$ matrices with at least one empty row.

Option 1 counts matrices with no empty row. Option 2 counts every nonzero relation and has no row-specific condition. Option 3, $8\cdot2^{56}$, counts choices of a marked empty row rather than distinct matrices; a matrix with $k$ empty rows appears $k$ times.

As a refined question, exactly one empty row gives $8\cdot255^7$: choose its location, then require each other row to be nonempty. Exactly $k$ empty rows gives $\binom8k255^{8-k}$. Summing this for $k=1,\ldots,8$ reproduces the answer by the binomial theorem. Requiring nonempty remaining rows is the detail that removes the overlap in the marked-row approach.

## Q50

**Correct option: 3.** On an $n$-object domain, a relation is a subset of $n^2$ ordered pairs, giving $2^{n^2}$ relations. The complement of “some empty row” is “every row nonempty,” whose count is $(2^n-1)^n$. Therefore

$$N(n)=2^{n^2}-(2^n-1)^n,\qquad n\ge1.$$

An independent inclusion-exclusion derivation lets $E_i$ denote the event that row $i$ is empty. If a specified set of $j$ rows is empty, the remaining $n(n-j)$ entries are free. Hence

$$N(n)=\sum_{j=1}^{n}(-1)^{j+1}\binom nj2^{n(n-j)}.$$

At $n=2$, this gives $2\cdot4-1=7$, matching complement counting. Option 1 imposes only a global nonzero condition. Option 2 stops after the first inclusion-exclusion term and overcounts overlaps. Option 4 is the complement of the requested event. Notice that relation-counting has $n^2$ independent bits, while unary predicate-counting has $n$; swapping these sample spaces produces superficially similar but fundamentally wrong formulas.

## Q51

**Correct option: 2.** The valid transformation is $\neg\forall x\exists yR(x,y)\equiv\exists x\forall y\neg R(x,y)$. Both quantifiers flip, and the predicate is negated. The resulting witness $x$ must be one input whose entire row fails, not a different input chosen for each failed entry.

On domain $\{0,1\}$, take the relation matrix with first row 00 and second row 11. It satisfies the negation because input 0 has no target, although input 1 has both targets. This refutes option 4, which incorrectly requires every row to be empty. Option 3 would yield $\forall x\exists y\neg R(x,y)$; that sentence fails in this example because the second row is full, proving non-equivalence.

Option 1 is refuted by the entirely zero two-by-two matrix: it would be counted once for choosing row 0 and again for choosing row 1. Distinguish a quantified witness from a labelled object being counted. Existence of an empty row does not endow a matrix with a unique distinguished empty row. Complement counting or inclusion-exclusion removes that extra marking and counts each interpretation once.

## Q52

**Correct option: 3.** A truth function on four atoms assigns one output bit independently to each of sixteen input rows. The implications require $G\le F\le H$ pointwise, where $G=p\land q$ and $H=p\lor r$. Because $G\Rightarrow H$ is valid, these inequalities never conflict.

| $(G,H)$ | Required value of $F$ | Number of four-atom rows |
| --- | --- | --- |
| (1,1) | 1 | 4 |
| (0,0) | 0 | 4 |
| (0,1) | Either 0 or 1 | 8 |
| (1,0) | Impossible pair here | 0 |

The first row count comes from $p=q=1$ with $r,s$ free. The second comes from $p=r=0$ with $q,s$ free. For the free region, $p=0,r=1$ gives four rows after choosing $q,s$, and $p=1,q=0$ gives four after choosing $r,s$. These cases are disjoint. The eight independently free output bits yield $2^8=256$ functions.

This counts functions, not satisfying assignments: the number eight identifies free input rows, and each such row offers two choices for the function's output. The two forced regions contribute one choice each, not additional powers of two. If there were any row with $G=1,H=0$, no function could satisfy both implications. A general sandwich problem therefore first checks consistency and then counts the rows with $G=0,H=1$; its answer is two raised to that count.

Option 1 uses only four free output bits, as if the unused input atom $s$ could be dropped from the table. Option 2 uses six free output bits and fails to match the explicit partition into four forced-one, four forced-zero and eight free rows. Option 4 uses all twelve rows where $H$ is true as free, ignoring the four where $G$ forces the output to one. The table supplies the exact reason each proposed exponent fails.

## Q53

**Correct option: 1.** Let $C_j$ be the event that column $j$ is entirely true. If any column is full, every row automatically contains a true entry; hence the row-nonempty condition introduces no further restriction once the column condition holds. We need the union of the three full-column events.

For one specified full column, three bits are fixed and six remain free, giving $2^6=64$ matrices. For two specified full columns, six bits are fixed and three remain free, giving $2^3=8$. All three columns being full gives the single all-one matrix. Inclusion-exclusion therefore yields

$$3\cdot64-\binom32\cdot8+1=192-24+1=169.$$

| Selected full columns | Choices of the selected set | Matrices for that set | Contribution |
| --- | --- | --- | --- |
| One | 3 | 64 | $+192$ |
| Two | 3 | 8 | $-24$ |
| Three | 1 | 1 | $+1$ |

Why the signs matter: a matrix with exactly one full column is counted once; one with exactly two is counted twice and subtracted once; the all-one matrix is counted three times, subtracted three times and restored once. Each consequently contributes exactly one. As a cross-check by disjoint cases, exactly one full column gives $3\cdot7^2=147$ matrices, exactly two give $3\cdot7=21$, and exactly three give one. Their sum is 169. The factors 7 require each unspecified column not to be full, preventing hidden overcounting.

Option 2 stops at $3\cdot64=192$ and counts a matrix repeatedly when several columns are full. Option 3, $7^3=343$, requires each row to be nonempty but does not require a common full column; the identity matrix is a counterexample. Option 4 counts all $2^9=512$ relations, including the zero matrix, which fails both conditions.
