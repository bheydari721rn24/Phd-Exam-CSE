## Detailed final decisions for calculation and proof

These decisions supplement the retained sixty full-sentence rules. Use the example and failure condition to decide *when* a formula applies, rather than memorize its shape alone.

### 1. Name the object being counted before choosing an exponent

An $n$-input truth table has $2^n$ rows, whereas the class of all scalar tables has $2^{2^n}$ functions. At three inputs these are eight rows and256 functions. The sixteen symmetric functions are yet another restricted class. If a question says “how many functions,” counting accepted rows of a single formula answers a different question.

### 2. Prove a half split through a predicate-changing bijection

Odd binary parity has $2^{n-1}$ true rows for $n\ge1$ because flipping one fixed bit reverses the predicate and pairs words bijectively. A length-four string over four symbols with even zero count instead has136 members out of256, because nonzero flag patterns have unequal multiplicities. A pair of names such as even/odd does not by itself justify division by two.

### 3. Complement the index set for a canonical product

With order $p,q,r$, $F=(p\Rightarrow r)(p\Leftrightarrow q)$ has true indices0,1,7. Its canonical CNF therefore uses false indices2,3,4,5,6. A product at0,1,7 describes the complement, not another notation for the same function. Write “true” or “false” beside the index set before selecting $\sum m$ or $\prod M$.

### 4. Reverse literal polarity between minterms and maxterms

Row101 has minterm $a\neg b c$ but maxterm $\neg a+b+\neg c$. The minterm equals one there; the maxterm equals zero there. Evaluate the three literals on the named row to check polarity before combining several rows. This one-row certificate is more reliable than memorizing a prime-placement convention without its meaning.

### 5. Reject the wrong syntax even when the truth function agrees

Majority's canonical DNF and canonical CNF are equivalent, but only one answers a CNF request. Its shorter POS $(p+q)(p+r)(q+r)$ is also not canonical over three inputs, because each clause omits one variable. Check format and function independently; neither substitutes for the other.

### 6. Check self-dual constraints pair by pair before counting freedom

For three inputs the pairs are0/7,1/6,2/5,3/4. An unconstrained pair supplies two choices; a consistent fixed pair supplies one; equal fixed outputs make the whole specification impossible. Fixing outputs0 and1 at0/7 leaves $2^3=8$ completions. Counting the six remaining cells independently would wrongly give64.

### 7. “Disjoint input blocks” does not mean “exclusive product events”

For $ab+cd$, the inputs are independent blocks but both products can be true at1111. Complement counting gives $16-9=7$ true rows; adding the two four-row events gives eight and double-counts1111. For $ab+ac$, shared $a$ invalidates the independent-block formula, and conditioning gives three true rows.

### 8. Implication chains exclude descents, not all changes

A chain $x_i\Rightarrow x_{i+1}$ accepts $0^k1^{n-k}$ and has $n+1$ true words. The all-zero word is valid because false antecedents make each implication true. Requiring neighboring equivalence would leave only the two constant words. The strict “weaker” claim needs at least two inputs; at one input both chains are empty conjunctions.

### 9. Separate symmetric class size from a selected function's layer sizes

There are $2^{n+1}$ symmetric functions because each of $n+1$ weights has one output choice. A particular exact-two function instead has $\binom n2$ true rows. At four inputs the former count is32 and the latter is six. Binomial coefficients count words within layers, not the number of layer-output choices.

### 10. Recover coefficients to justify a count of distinct ANF functions

Affine coefficients are recovered by $c=F(0)$ and $a_i=F(e_i)\oplus F(0)$. The recovery proves that $2^{n+1}$ coefficient lists are distinct functions. Quadratic coefficients additionally use the four-row XOR for $a_{ij}$. Merely counting written expressions is unsafe when a representation is not known to be unique.

### 11. Include the constant and remove repeated powers in ANF

Degree-at-most-two permits $1+n+\binom n2$ independent monomials and $2^{1+n+\binom n2}$ functions. Omitting the constant halves the count. Adding $x_i^2$ as another coefficient is wrong because $x_i^2=x_i$ on the binary domain. “Exactly two” additionally excludes all affine functions and therefore requires subtraction.

### 12. Use the complete overlap multiplicity before replacing OR by XOR

Two functions satisfy $f+g=f\oplus g$ exactly when $fg=0$. In majority, three overlapping pair terms agree as OR and XOR because their common111 row activates three terms, an odd number. The agreement of that whole expression does not validate replacing an arbitrary pairwise OR: two active terms would cancel under XOR.

### 13. Distinguish essential support from a redundant formula

The expression $xy+(\neg x)y+zz'$ contains three names but equals $y$. An input is irrelevant exactly when its two cofactors agree as functions. Its declared three-input truth table still has eight rows. Support size does not authorize changing the question's table domain or numerical indexing.

### 14. Count derivative contexts and starting words separately

For $F=x\oplus yz$, $D_xF=1$ on four $(y,z)$ contexts. There are four undirected sensitivity edges but eight complete starting words, since each edge has two endpoints. Specify the counting convention before doubling. A derivative equal to one says the output changes, not that every change is increasing.

### 15. Prove unateness using ordered cofactors

Positive unateness is $F_0\le F_1$; negative unateness is the reverse. XOR has cofactors $y,\neg y$, with increases at $y=0$ and decreases at $y=1$, proving binateness. Seeing both input polarities in an expression is insufficient: absorption can make that input irrelevant. Equal cofactors satisfy both unateness directions.

### 16. Trace all outputs of a circuit before naming its function

The authentic NAND network has first output $x\oplus y$, which is compatible with either half-addition or half-subtraction. Its second output $(\neg x)y$ identifies borrow and rules out carry $xy$. Check $01$ and11 to distinguish them, then verify $x-y=D-2B$ in ordinary integer arithmetic on all rows.

### 17. Write a mux's select contract before substituting data

For $s=0$ selecting $I_0$, the formula is $(\neg s)I_0+sI_1$. Cascading $(1,0)$ selected by$b$ with $(t,0)$ selected by$a$ gives $(\neg a)(\neg b)$, NOR. Reversing the pin convention reverses a cofactor and changes the function. A label inside a block names a select value; a label on a data wire supplies a constant.

### 18. State the delay model for a hazard claim

Consensus makes $ab+(\neg a)c+bc$ equal to $ab+(\neg a)c$ in steady state. With stable $b=c=1$, the extra term bridges the handoff when$a$ changes in a two-level SOP implementation. Without a single-input/stable-context contract, this does not prove arbitrary waveform safety. Algebraic redundancy and physical usefulness are compatible because they answer different questions.

### 19. OR mismatch indicators when checking vector outputs

If both coordinates disagree, their two mismatch bits are1,1. OR reports an error; XOR gives zero and loses it. Under care set$C$, use $C\bigvee_i(F_i\oplus G_i)=0$. For $(a+b,ab)$ versus $(a\oplus b,0)$, both errors occur at11 and the correct miter is$ab$.

### 20. Preserve the order of quantified choices

For equality $x\Leftrightarrow y$, $\forall x\exists y$ is true because a matching$y$ may depend on$x$. The reversed order is false because one fixed$y$ cannot match both$x$ values. Derive the inner cofactor combination first: existential is OR, universal is AND. Swapping unlike quantifiers without a dependency proof changes the task.
