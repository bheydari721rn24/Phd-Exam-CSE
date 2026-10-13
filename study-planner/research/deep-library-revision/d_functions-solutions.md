## Q1

**Separate existence of a bijection from a property of the specified function.** An injection $f:A\to B$ itself witnesses the cardinal inequality $|A|\le|B|$, so (a) is true. For a surjection, each fiber $f^{-1}[\{b\}]$ is nonempty. Under the stated choice convention, choose one member $s(b)$ from each fiber. If $s(b)=s(b')$, applying f gives $b=b'$, so the section is injective and witnesses $|B|\le|A|$. For finite B only finitely many choices are needed. Assertion (b) is true. A bijection witnesses equal cardinality by definition, proving (c).

Assertion (d) reverses the quantifiers incorrectly. Equal cardinality says that some bijection exists; it does not classify the map already named. On $A=B=\{0,1\}$ let $f(0)=f(1)=0$. Both carriers have two members. The two inputs collide and target 1 is missed, so this specified f is not bijective.

**Options.** Option 4 lists exactly (a), (b), (c). Option 1 omits the valid surjection comparison. Option 2 includes false (d) and omits two true claims. Option 3 includes false (d) and omits true (a), (b).

**Boundary.** An empty-domain map into a nonempty target is injective and not onto. A map with an empty target exists only if its domain is empty. Neither boundary changes the conclusions. The original cardinality statement is not silently restricted to finite sets.

## Q2

**Evaluate the quantified implication using the interpreted function.** The relation is the directed cycle $0\to1\to2\to0$. A universal implication is false only when its antecedent is true and its consequent is false. For each assigned x, first locate its unique R-successor y; only that y gives a nonvacuous test.

For $v_1(x)=0$, the relevant value is $y=1$. The interpreted output is $f(1)=2$, so the consequent is $R(2,0)$, a listed pair. For $y=0$ and $y=2$, $R(0,y)$ is false and the implications are true. Thus all three y-tests pass.

For $v_2(x)=2$, the relevant value is $y=0$. The interpreted output is $f(0)=1$, and $(1,0)$ is absent from R. This single true-antecedent/false-consequent witness falsifies the universal formula. The other two y-values cannot repair it.

**Options.** Only $v_1$ works, giving option 1. Option 2 reverses the two computed outcomes. Option 3 overlooks witness $(x,y)=(2,0)$. Option 4 rejects the three successful implication tests at $x=0$.

**Transfer.** As a separate check, x=1 also fails: its relevant y=2 gives $f(2)=0$, and R contains no loop $(0,0)$. Therefore the entire truth set of the displayed formula is exactly $\{0\}$. Substituting f(x) instead of f(y) would evaluate a different formula.

## Q3

**Encode a function by output multiplicities.** A weakly increasing five-term sequence using values 1 through 5 is uniquely determined by $c_1,\ldots,c_5$, where $c_j$ counts occurrences of value j. These counts are nonnegative and sum to five. Conversely any such vector reconstructs exactly one sequence: write $c_1$ ones, then $c_2$ twos, and so on. This is a bijection, not merely an upper bound.

Place five identical stars and four separators in a row. The separators determine the five multiplicities, including zero multiplicities when separators touch. There are nine positions and four separator positions:
$$\binom{9}{4}=\frac{9\cdot8\cdot7\cdot6}{4\cdot3\cdot2\cdot1}=126.$$
Thus option 1 is correct. The source's condition at i<j is equivalent here to writing it at i≤j, since the additional self-comparison is always true.

**Check the options and scope.** Strict increase on these equal five-element chains would force the identity and give one function. Allowing every output tuple would give $5^5=3125$. Neither is the weak monotonicity task. Option 2 gives $84=\binom{9}{3}$, which would place three separators and six stars, describing six inputs and four output values rather than the stated five-to-five types. Option 3 gives $168=2\binom{9}{3}$, adding an unjustified factor of two to that different-type count. Option 4 gives $63=126/2$ and would identify pairs of distinct multiplicity vectors; those vectors define different functions. These comparisons explain why no extra label or symmetry factor belongs in the bijective count, without claiming an official explanation for how the source designed its distractors.

**Generalization.** For an m-element input chain and an n-element output chain, the same argument gives $\binom{m+n-1}{n-1}$, allowing repeated outputs and unused target values. Surjectivity would instead require all multiplicities positive.

## Q4

**Use exclusion of missed labelled targets.** Start with all $4^6=4096$ output tuples. If one specified target is forbidden there are $3^6=729$ tuples. Two specified targets forbidden leave $2^6=64$. Three specified targets forbidden leave exactly one constant tuple. The six-element domain cannot map into the empty target.

Choose the forbidden target labels, and alternate signs:
$$A=4^6-\binom{4}{1}3^6+\binom{4}{2}2^6-\binom{4}{3}1^6=4096-2916+384-4=1560.$$
Every onto tuple is counted once. A tuple missing k>0 targets has net coefficient $\sum_{j=0}^k(-1)^j\binom{k}{j}=0$, explaining why the subtraction and restoration remove it exactly.

The question asks for $A/30$, not A. Division gives $1560/30=52$. The only listed interval containing 52 is option 4. Options 1, 2 and 3 end at 15, 30 and 45 respectively, all below 52.

**Independent fiber cross-check.** Four nonempty fibers summing to six have profile 3,1,1,1 or 2,2,1,1. The first contributes $4\cdot6!/3!=480$. The second contributes $\binom{4}{2}6!/(2!2!)=1080$. Their sum is 1560. Target labels were included when choosing the larger fibers; multiplying the final answer by another $4!$ would count them twice.

## Q5

**Read the strength of assertion (a) accurately.** It asks whether the map is the identity, not whether it is injective. On the full integer chain take $f(k)=k+1$. If $i<j$, then $i+1<j+1$, so f preserves the strict order. But $f(0)=1\ne0$; it is not the identity. Thus (a) is false without a finiteness assumption.

Strict order preservation does prove injectivity: two distinct inputs in a linear order are comparable, and their strict output inequality prohibits a collision. On a finite chain an increasing self-map must indeed be the identity. Writing the chain as $a_1<\cdots<a_n$, injection uses every target; the least input must map to the least target, then the next to the next, continuing by induction. This finite theorem cannot decide the unqualified source assertion.

**Construct the order in (b).** For a countably infinite B choose a bijective enumeration $e:\mathbb N\to B$. Declare $e(i)\prec e(j)$ exactly when i<j. The indices of any nonempty subset of B form a nonempty natural-number set with a least index. Its listed element is the subset's least element. Finite B is handled by a finite enumeration; the empty case is vacuous. Hence (b) is true.

**Options.** Only (b) holds, so choose option 2. Options 1 and 3 wrongly accept the identity claim; options 1 and 4 wrongly reject the constructed well-order.

**Distinction.** This constructs some well-order. It does not assert that the usual order on a countable carrier already is a well-order: the integers in their usual order have no least element.

## Q6

**Select attained labels, then require nonempty fibers.** Choose three of the four target labels in $\binom{4}{3}=4$ ways. For a fixed chosen target set, the number of onto maps from five labelled inputs is
$$3^5-3\cdot2^5+3\cdot1^5=243-96+3=150.$$
The omission events overlap at constant functions, which explains the restoring term. The selected target set is the unique image of the function, so different selections cannot produce the same function. Multiply to obtain $4\cdot150=600$, option 1.

**A second derivation.** Onto maps to three labels have fiber profiles 3,1,1 or 2,2,1. For a fixed image set these contribute $3\cdot5!/3!=60$ and $3\cdot5!/(2!2!)=90$, totalling 150. Across four image sets this again gives 600.

**Options.** Option 4 gives $4^5=1024$, which includes functions with one, two or four image values. Options 2 and 3 give 360 and 240; neither equals four copies of the exact fixed-image count 150. In fact 240 is the number of surjections onto all four targets, $4!\binom{5}{2}=240$, a different image-size requirement.

**Transfer.** With m inputs and n target labels, image size k has count $\binom nk k!S(m,k)$. Choosing the image alone does not specify assignments to its members; ordering already labelled fibers again would overcount.

## Q7

**A right inverse is one representative per fiber.** Write the three target labels as a,b,c. The identity $f(g(a))=a$ forces g(a) into the two-element a-fiber. Independently g(b) must lie in the three-element b-fiber, and g(c) in the four-element c-fiber. The fibers are disjoint, so these choices automatically make g injective. Each selection yields one and only one reverse function satisfying the identity.

The product rule gives $2\cdot3\cdot4=24$, option 2. Nine is the sum $2+3+4$ and counts domain elements, not independent selections. Twelve omits the two choices in the first fiber, using only $3\cdot4$. Thirty-six is $3\cdot3\cdot4$, which incorrectly supplies a third available representative in the explicitly two-element first fiber.

**Verify a representative choice.** If chosen inputs are $a_1,b_2,c_4$, composition sends each target through its own chosen antecedent and back to itself. Choosing $a_2$ instead changes g while preserving the identity. Every right inverse arises in this way because the identity forces membership in the named fibers.

**Boundary.** If any target fiber were empty, no right inverse could exist. These non-singleton fibers also show why none of the 24 sections is a true inverse of f: for example, both a-fiber inputs have the same f-value, so g cannot recover both of them.

## Q8

**Account for the fixed endpoints before counting.** The monotone output sequence has six positions and four possible values. Let $c_j$ be the multiplicity of j. The first endpoint being 1 forces $c_1\ge1$; the last being 4 forces $c_4\ge1$. Values 2 and 3 may be absent. Subtract one from the first and fourth counts. Four nonnegative residual counts now sum to $6-2=4$.

Stars and bars gives $\binom{4+4-1}{4-1}=\binom{7}{3}=35$, so option 2 is correct. Equivalently, the four interior positions can be any weakly increasing sequence from four values; attach the prescribed endpoints to recover the full function.

**Options.** Fifteen is $\binom{6}{2}$, the count for four interior positions using only three values; it discards an allowed value. Fifty-six is $\binom{8}{3}$, obtained by imposing only the first endpoint and leaving five interior/residual positions. Seventy is twice 35, but the endpoint order is already fixed as 1 then 4 and has no extra two-way choice.

**Concrete check.** The function with output tuple (1,1,1,1,1,4) is legal and has residual multiplicities (4,0,0,0). The tuple (1,2,2,3,3,4) is also legal. Requiring every target to occur would incorrectly remove the first example and count only positive multiplicities.

## Q9

**Idempotence identifies the image with the fixed set.** If $y=f(x)$, the identity $f(f(x))=f(x)$ says $f(y)=y$. Conversely every fixed point is an image point. Thus exactly two fixed points means exactly two image points, both fixed.

Choose their unordered two-element set in $\binom{5}{2}=10$ ways. Their outputs are forced to themselves. Each of the other three labelled inputs independently chooses one of those two points, giving $2^3=8$ assignments. The total is $10\cdot8=80$, option 2. Every constructed map is idempotent because one application reaches a fixed point; every idempotent map with this image arises exactly once.

**Options.** Forty halves the correct count despite the fixed set already being unordered. One hundred sixty orders the two fixed points and counts each fixed set twice. Twenty is $5\cdot4$, counting ordered distinct fixed-point labels while omitting the three independent assignments; neither operation reflects the specified functions.

**Example.** With fixed points 1 and 2, the output tuple (1,2,1,2,1) is valid. Swapping the two image points to have $f(1)=2,f(2)=1$ would make a two-cycle, not an idempotent map: $f^2(1)=1\ne f(1)$. Two attained outputs alone do not guarantee idempotence.

## Q10

**Track what a composite can actually detect.** If $g\circ f$ is injective and $f(a)=f(a')$, applying g gives equal composite outputs. Composite injection forces $a=a'$, proving f injective. If the composite is onto C, every $c\in C$ equals $g(f(a))$ for some a; therefore c is an output of g, proving g onto. A bijective composite has both properties, so option 3 holds universally.

**Reject option 1 with a typed counterexample.** Let $A=\{0\}$, $B=\{b,c\}$ and $C=\{u\}$; set f(0)=b and g(b)=g(c)=u. The singleton composite is injective, but g has a collision.

**Reject option 2.** With the same maps the composite is onto the singleton C, but f misses c. Onto-ness of the composite says the attained middle points cover all final targets, not all middle targets.

**Reject option 4.** Let $A=B=\{0,1\}$, take f to be the identity and g to be the constant map into $C=\{u\}$. Then f is onto while the composite merges the two inputs and is not injective.

**Sharpen the theorem.** Composite injectivity is equivalent to f injective together with g injective on $f[A]$. Composite surjectivity is equivalent to $g[f[A]]=C$. The full unused part of B is precisely where reverse inferences can fail.

## Q11

**Choose the specified fiber, then exclude that target everywhere else.** There are $\binom{7}{3}=35$ possible three-element preimage sets for the distinguished target b. On that selected set every output is forced to b. Each of the remaining four inputs must avoid b and may independently use either of the other two labelled targets. This gives $2^4=16$ assignments and total $35\cdot16=560$, option 1.

The construction is bijective: a finished function recovers its unique b-fiber, and its four remaining outputs recover the independent choices. No ordering of fiber elements is relevant. There is no requirement that the other two targets are both attained.

**Options.** Two hundred eighty divides the correct count by two as though the remaining target labels could be exchanged without changing the function. They are labelled and different outputs define different functions. Eight hundred forty is $35\cdot4!$ and incorrectly treats the four residual output choices as a permutation of four distinct objects. There are only two available output labels, with repetition allowed. Two thousand one hundred eighty-seven is $3^7$, which ignores the exact distinguished-fiber constraint.

**Transfer.** For m inputs, n target labels and exactly r antecedents of one named target, the unrestricted-other-fiber count is $\binom mr(n-1)^{m-r}$. Requiring the whole function onto would additionally require a surjection from the residual inputs to the residual targets.

## Q12

**Images use existence of an antecedent.** For any output b, membership in $f[X\cup Y]$ means that some input in X or Y maps to b. This is equivalent to membership in $f[X]\cup f[Y]$. Both directions use the same witness, so option 3 is always true without injectivity or surjectivity.

**One explicit collision diagnoses the other options.** Let $A=\{u,v\}$, $B=\{b\}$ and $f(u)=f(v)=b$. Set $X=\{u\}$ and $Y=\{v\}$. The sets are disjoint, so $f[X\cap Y]=\varnothing$, while $f[X]\cap f[Y]=\{b\}$. Option 1 fails because its two output witnesses are different inputs.

For option 2, $X\setminus Y=X$, hence its image is $\{b\}$. But $f[X]\setminus f[Y]=\varnothing$. A point outside Y can share an output with a point inside Y; subtraction after taking images loses that value.

For option 4, both images equal $\{b\}$ although $X\ne Y$. Equal output sets do not recover the input sets when collisions exist.

**Exact recovery conditions.** Injection makes the intersection and difference identities valid for every pair of input subsets, because equal output witnesses must then be the same input. Preimages of target subsets preserve these set operations for every total function: they test one fixed input's value and introduce no competing witnesses.

## Q13

**The identity after two applications restricts cycle lengths.** A permutation satisfying $f^2=\operatorname{id}$ has only fixed points and transpositions. With exactly one fixed point on five labels, the other four must form exactly two disjoint transpositions.

Choose the fixed label in five ways. For the other four, choose a partner for their smallest label in three ways; the remaining pair is then forced. Equivalently the pairing count is $4!/(2^2\cdot2!)=3$, dividing by within-pair order and by order of the two pairs. Hence the total is $5\cdot3=15$, option 1.

**Options.** Thirty omits division by the order of the two disjoint pairs: $5\cdot4!/2^2=30$. Sixty omits both pair-order division and one within-pair division: $5\cdot4!/2=60$. Forty-five would require nine distinct pairings for each fixed point; the explicit partner construction proves there are exactly three, excluding it.

**Concrete list for one fixed point.** If label 5 is fixed, the possible pairings are (12)(34), (13)(24), and (14)(23). Rewriting (12) as (21), or exchanging the displayed pair order, does not change the function. This is why the divisions are required.

**Boundary.** The number of nonfixed labels in any involution must be even. Five labels can have one, three or five fixed points, but not two. Longer cycles cannot satisfy the squared-identity condition.

## Q14

**Derive the count or structural law.** Order the three labelled inputs once. Their distinct outputs have n+3, then n+2, then n+1 possibilities. Multiplication gives the falling product. The order of inputs is a bookkeeping convention, not an extra choice to multiply again. Alternatively choose the three-element image and then a bijection from the three labelled inputs to it, giving $\binom{n+3}{3}3!$. Each function determines both objects uniquely.

**Substitute the stated parameter.** At $n=5$ the law gives $((5)+3)((5)+2)((5)+1)=336$. Every label and every constraint is retained from the stem.

**Compute all alternatives.** Option 1 gives $((5)+3)^3=512$; it allows collisions by restoring every target at each of the three choices. Option 2 gives $\binom{(5)+3}{3}=56$; it chooses the attained set but omits the six assignments of its labels to the three labelled inputs. Option 3 gives $3^{(5)+3}=6561$; it counts unrestricted maps in the reverse direction. Option 4 gives 336, equal to the derived result.

**Boundary and transfer.** At n=0 the codomain has three labels and the count is six bijections. On a codomain of size below three the injection count is zero. The given positive parameter domain avoids that shortage.

## Q15

**Derive the count or structural law.** Order the three labelled inputs once. Their distinct outputs have n+3, then n+2, then n+1 possibilities. Multiplication gives the falling product. The order of inputs is a bookkeeping convention, not an extra choice to multiply again. Alternatively choose the three-element image and then a bijection from the three labelled inputs to it, giving $\binom{n+3}{3}3!$. Each function determines both objects uniquely.

**Substitute the stated parameter.** At $n=8$ the law gives $((8)+3)((8)+2)((8)+1)=990$. Every label and every constraint is retained from the stem.

**Compute all alternatives.** Option 1 gives $\binom{(8)+3}{3}=165$; it chooses the attained set but omits the six assignments of its labels to the three labelled inputs. Option 2 gives $3^{(8)+3}=177147$; it counts unrestricted maps in the reverse direction. Option 3 gives 990, equal to the derived result. Option 4 gives $((8)+3)^3=1331$; it allows collisions by restoring every target at each of the three choices.

**Boundary and transfer.** At n=0 the codomain has three labels and the count is six bijections. On a codomain of size below three the injection count is zero. The given positive parameter domain avoids that shortage.

## Q16

**Derive the count or structural law.** Order the three labelled inputs once. Their distinct outputs have n+3, then n+2, then n+1 possibilities. Multiplication gives the falling product. The order of inputs is a bookkeeping convention, not an extra choice to multiply again. Alternatively choose the three-element image and then a bijection from the three labelled inputs to it, giving $\binom{n+3}{3}3!$. Each function determines both objects uniquely.

**Universal expression.** The bijective construction gives $(n+3)(n+2)(n+1)$, option 2, throughout the stated domain where the required objects exist. The result is not extrapolated from one successful numerical example.

**Compare the other laws.** The alternative $(n+3)^3$ allows collisions by restoring every target at each of the three choices. At $n=5$ it gives $512$, whereas the required count is $336$. The alternative $\binom{n+3}{3}$ chooses the attained set but omits the six assignments of its labels to the three labelled inputs. At $n=5$ it gives $56$, whereas the required count is $336$. The alternative $3^{n+3}$ counts unrestricted maps in the reverse direction. At $n=5$ it gives $6561$, whereas the required count is $336$. A numerical disagreement disproves a competing expression asserted for every valid parameter; agreement at a degenerate parameter would not establish that universal claim.

**Boundary and transfer.** At n=0 the codomain has three labels and the count is six bijections. On a codomain of size below three the injection count is zero. The given positive parameter domain avoids that shortage.

## Q17

**Derive the count or structural law.** Order the three labelled inputs once. Their distinct outputs have n+3, then n+2, then n+1 possibilities. Multiplication gives the falling product. The order of inputs is a bookkeeping convention, not an extra choice to multiply again. Alternatively choose the three-element image and then a bijection from the three labelled inputs to it, giving $\binom{n+3}{3}3!$. Each function determines both objects uniquely.

**Check each scope claim.** Option 1: An injection assigns different targets to distinct inputs, so a finite domain larger than its codomain cannot admit it. Option 2: A total function must define every declared input. Allowing undefined inputs changes the task to partial injections. Option 3: On image $\{a,b,c\}$, the tuples (a,b,c) and (b,a,c) are different injections. The selected image alone does not specify one. Option 4: The inclusion $\{1,2,3\}\to\{1,2,3,4\}$ is injective and misses 4. Equal finite sizes, not finiteness alone, gives the reverse implication. Thus option 1 is correct.

**Boundary and transfer.** At n=0 the codomain has three labels and the count is six bijections. On a codomain of size below three the injection count is zero. The given positive parameter domain avoids that shortage.

## Q18

**Derive the count or structural law.** Let E_a,E_b,E_c denote tuples missing a specified target. There are $3^n$ unrestricted tuples and $2^n$ in each event. Each pair of missed-target events has one constant tuple for positive n. There are three such pairs. Their triple intersection is empty because a nonempty domain has no function into an empty target. Inclusion–exclusion therefore gives $3^n-3\cdot2^n+3$. A constant tuple is removed twice in the first subtraction and restored once, leaving zero net count; an onto tuple is untouched.

**Substitute the stated parameter.** At $n=5$ the law gives $3^(5)-3\cdot2^(5)+3=150$. Every label and every constraint is retained from the stem.

**Compute all alternatives.** Option 1 gives $3!\binom{(5)}{3}=60$; it chooses one distinguished antecedent per target without specifying the other outputs, and may select the same completed function many times. Option 2 gives 150, equal to the derived result. Option 3 gives $3^(5)=243$; it counts all output tuples, including those that miss a target. Option 4 gives $3^(5)-3\cdot2^(5)=147$; it subtracts constant maps twice without restoring the overlaps.

**Boundary and transfer.** At n=1 and n=2 the count is zero, consistent with the finite size obstruction. The positive-domain formula must not be used at n=0 without the triple-intersection term; there the onto count is zero, not one.

## Q19

**Derive the count or structural law.** Let E_a,E_b,E_c denote tuples missing a specified target. There are $3^n$ unrestricted tuples and $2^n$ in each event. Each pair of missed-target events has one constant tuple for positive n. There are three such pairs. Their triple intersection is empty because a nonempty domain has no function into an empty target. Inclusion–exclusion therefore gives $3^n-3\cdot2^n+3$. A constant tuple is removed twice in the first subtraction and restored once, leaving zero net count; an onto tuple is untouched.

**Substitute the stated parameter.** At $n=8$ the law gives $3^(8)-3\cdot2^(8)+3=5796$. Every label and every constraint is retained from the stem.

**Compute all alternatives.** Option 1 gives 5796, equal to the derived result. Option 2 gives $3^(8)=6561$; it counts all output tuples, including those that miss a target. Option 3 gives $3^(8)-3\cdot2^(8)=5793$; it subtracts constant maps twice without restoring the overlaps. Option 4 gives $3!\binom{(8)}{3}=336$; it chooses one distinguished antecedent per target without specifying the other outputs, and may select the same completed function many times.

**Boundary and transfer.** At n=1 and n=2 the count is zero, consistent with the finite size obstruction. The positive-domain formula must not be used at n=0 without the triple-intersection term; there the onto count is zero, not one.

## Q20

**Derive the count or structural law.** Let E_a,E_b,E_c denote tuples missing a specified target. There are $3^n$ unrestricted tuples and $2^n$ in each event. Each pair of missed-target events has one constant tuple for positive n. There are three such pairs. Their triple intersection is empty because a nonempty domain has no function into an empty target. Inclusion–exclusion therefore gives $3^n-3\cdot2^n+3$. A constant tuple is removed twice in the first subtraction and restored once, leaving zero net count; an onto tuple is untouched.

**Universal expression.** The bijective construction gives $3^n-3\cdot2^n+3$, option 4, throughout the stated domain where the required objects exist. The result is not extrapolated from one successful numerical example.

**Compare the other laws.** The alternative $3^n$ counts all output tuples, including those that miss a target. At $n=5$ it gives $243$, whereas the required count is $150$. The alternative $3^n-3\cdot2^n$ subtracts constant maps twice without restoring the overlaps. At $n=5$ it gives $147$, whereas the required count is $150$. The alternative $3!\binom{n}{3}$ chooses one distinguished antecedent per target without specifying the other outputs, and may select the same completed function many times. At $n=5$ it gives $60$, whereas the required count is $150$. A numerical disagreement disproves a competing expression asserted for every valid parameter; agreement at a degenerate parameter would not establish that universal claim.

**Boundary and transfer.** At n=1 and n=2 the count is zero, consistent with the finite size obstruction. The positive-domain formula must not be used at n=0 without the triple-intersection term; there the onto count is zero, not one.

## Q21

**Derive the count or structural law.** Let E_a,E_b,E_c denote tuples missing a specified target. There are $3^n$ unrestricted tuples and $2^n$ in each event. Each pair of missed-target events has one constant tuple for positive n. There are three such pairs. Their triple intersection is empty because a nonempty domain has no function into an empty target. Inclusion–exclusion therefore gives $3^n-3\cdot2^n+3$. A constant tuple is removed twice in the first subtraction and restored once, leaving zero net count; an onto tuple is untouched.

**Check each scope claim.** Option 1: For a function with fiber sizes 2,2,1, there are four choices of representatives but just one completed function. The residual outputs must also be specified. Option 2: Totality demands an output for the first input, which an empty codomain cannot supply. The nonempty hypothesis matters. Option 3: A constant tuple at a misses both b and c. Thus it belongs to two omission events, and the pairwise restoration is necessary. Option 4: The constant tuple at a lies in both E_b and E_c; their intersection is nonempty. The omission events are not disjoint. Thus option 3 is correct.

**Boundary and transfer.** At n=1 and n=2 the count is zero, consistent with the finite size obstruction. The positive-domain formula must not be used at n=0 without the triple-intersection term; there the onto count is zero, not one.

## Q22

**Derive the count or structural law.** For an idempotent map every image point y satisfies $f(y)=y$. Conversely any fixed point lies in the image. Choose this two-element fixed image in $\binom{n}{2}$ ways. Both of its assignments are forced; each of the n−2 remaining labelled inputs chooses one of those two outputs independently. Every constructed function is idempotent, since the second application acts on a fixed point. Recovering its unique image proves that the construction does not duplicate functions.

**Substitute the stated parameter.** At $n=5$ the law gives $\binom{(5)}{2}2^{(5)-2}=80$. Every label and every constraint is retained from the stem.

**Compute all alternatives.** Option 1 gives $2^(5)=32$; it allows both outputs at every point without choosing which two labels are the fixed image. Option 2 gives $(5)((5)-1)=20$; it orders the image labels and omits the free choices for every nonimage input. Option 3 gives 80, equal to the derived result. Option 4 gives $\binom{(5)}{2}2^(5)=320$; it incorrectly leaves the outputs of the two image points free instead of fixing each to itself.

**Boundary and transfer.** Two image points require n≥2; at n=2 the identity is the unique map. The image set is unordered, whereas the remaining input assignments are labelled. Exactly two fixed points and exactly two image points coincide only under the idempotence hypothesis.

## Q23

**Derive the count or structural law.** For an idempotent map every image point y satisfies $f(y)=y$. Conversely any fixed point lies in the image. Choose this two-element fixed image in $\binom{n}{2}$ ways. Both of its assignments are forced; each of the n−2 remaining labelled inputs chooses one of those two outputs independently. Every constructed function is idempotent, since the second application acts on a fixed point. Recovering its unique image proves that the construction does not duplicate functions.

**Substitute the stated parameter.** At $n=8$ the law gives $\binom{(8)}{2}2^{(8)-2}=1792$. Every label and every constraint is retained from the stem.

**Compute all alternatives.** Option 1 gives $(8)((8)-1)=56$; it orders the image labels and omits the free choices for every nonimage input. Option 2 gives 1792, equal to the derived result. Option 3 gives $\binom{(8)}{2}2^(8)=7168$; it incorrectly leaves the outputs of the two image points free instead of fixing each to itself. Option 4 gives $2^(8)=256$; it allows both outputs at every point without choosing which two labels are the fixed image.

**Boundary and transfer.** Two image points require n≥2; at n=2 the identity is the unique map. The image set is unordered, whereas the remaining input assignments are labelled. Exactly two fixed points and exactly two image points coincide only under the idempotence hypothesis.

## Q24

**Derive the count or structural law.** For an idempotent map every image point y satisfies $f(y)=y$. Conversely any fixed point lies in the image. Choose this two-element fixed image in $\binom{n}{2}$ ways. Both of its assignments are forced; each of the n−2 remaining labelled inputs chooses one of those two outputs independently. Every constructed function is idempotent, since the second application acts on a fixed point. Recovering its unique image proves that the construction does not duplicate functions.

**Universal expression.** The bijective construction gives $\binom{n}{2}2^{n-2}$, option 1, throughout the stated domain where the required objects exist. The result is not extrapolated from one successful numerical example.

**Compare the other laws.** The alternative $2^n$ allows both outputs at every point without choosing which two labels are the fixed image. At $n=5$ it gives $32$, whereas the required count is $80$. The alternative $n(n-1)$ orders the image labels and omits the free choices for every nonimage input. At $n=5$ it gives $20$, whereas the required count is $80$. The alternative $\binom{n}{2}2^n$ incorrectly leaves the outputs of the two image points free instead of fixing each to itself. At $n=5$ it gives $320$, whereas the required count is $80$. A numerical disagreement disproves a competing expression asserted for every valid parameter; agreement at a degenerate parameter would not establish that universal claim.

**Boundary and transfer.** Two image points require n≥2; at n=2 the identity is the unique map. The image set is unordered, whereas the remaining input assignments are labelled. Exactly two fixed points and exactly two image points coincide only under the idempotence hypothesis.

## Q25

**Derive the count or structural law.** For an idempotent map every image point y satisfies $f(y)=y$. Conversely any fixed point lies in the image. Choose this two-element fixed image in $\binom{n}{2}$ ways. Both of its assignments are forced; each of the n−2 remaining labelled inputs chooses one of those two outputs independently. Every constructed function is idempotent, since the second application acts on a fixed point. Recovering its unique image proves that the construction does not duplicate functions.

**Check each scope claim.** Option 1: On five labels, the tuple (1,2,1,1,2) is idempotent but fixes only 1 and 2. Nonimage points need not be fixed. Option 2: A function swapping image labels 1 and 2 has two attained values but satisfies $f^2(1)=1\ne2=f(1)$, so it is not idempotent. Option 3: If image point 1 mapped to a different image point 2, an x with f(x)=1 would satisfy $f^2(x)=2\ne f(x)$. This violates the identity. Option 4: For every y=f(x), idempotence gives f(y)=y; conversely f(y)=y puts y in the image. These prove the exact characterization. Thus option 4 is correct.

**Boundary and transfer.** Two image points require n≥2; at n=2 the identity is the unique map. The image set is unordered, whereas the remaining input assignments are labelled. Exactly two fixed points and exactly two image points coincide only under the idempotence hypothesis.

## Q26

**Derive the count or structural law.** Exactly four labels move. Choose them in $\binom{n}{4}$ ways. For four fixed distinct labels a,b,c,d, the only pairings are (ab)(cd), (ac)(bd), (ad)(bc). Each defines exactly one permutation and all remaining labels are fixed. Thus the count is $3\binom{n}{4}$. The equivalent factorial expression is $n!/[2^2\,2!\,(n-4)!]$: within-pair order and pair order do not change the function.

**Substitute the stated parameter.** At $n=5$ the law gives $3\binom{(5)}{4}=15$. Every label and every constraint is retained from the stem.

**Compute all alternatives.** Option 1 gives $6\binom{(5)}{4}=30$; it orders the two disjoint transpositions and counts each resulting permutation twice. Option 2 gives $\binom{(5)}{2}^2=100$; it chooses two pairs independently, permitting overlap and ordering identical or exchanged selections. Option 3 gives $\binom{(5)}{4}=5$; it selects the four moved labels but omits their three pairings. Option 4 gives 15, equal to the derived result.

**Boundary and transfer.** The count is zero for n<4; at n=4 there are three maps. These are permutations with exactly two transpositions. Counting all involutions requires summing over every permitted number of transpositions.

## Q27

**Derive the count or structural law.** Exactly four labels move. Choose them in $\binom{n}{4}$ ways. For four fixed distinct labels a,b,c,d, the only pairings are (ab)(cd), (ac)(bd), (ad)(bc). Each defines exactly one permutation and all remaining labels are fixed. Thus the count is $3\binom{n}{4}$. The equivalent factorial expression is $n!/[2^2\,2!\,(n-4)!]$: within-pair order and pair order do not change the function.

**Substitute the stated parameter.** At $n=8$ the law gives $3\binom{(8)}{4}=210$. Every label and every constraint is retained from the stem.

**Compute all alternatives.** Option 1 gives $\binom{(8)}{2}^2=784$; it chooses two pairs independently, permitting overlap and ordering identical or exchanged selections. Option 2 gives $\binom{(8)}{4}=70$; it selects the four moved labels but omits their three pairings. Option 3 gives 210, equal to the derived result. Option 4 gives $6\binom{(8)}{4}=420$; it orders the two disjoint transpositions and counts each resulting permutation twice.

**Boundary and transfer.** The count is zero for n<4; at n=4 there are three maps. These are permutations with exactly two transpositions. Counting all involutions requires summing over every permitted number of transpositions.

## Q28

**Derive the count or structural law.** Exactly four labels move. Choose them in $\binom{n}{4}$ ways. For four fixed distinct labels a,b,c,d, the only pairings are (ab)(cd), (ac)(bd), (ad)(bc). Each defines exactly one permutation and all remaining labels are fixed. Thus the count is $3\binom{n}{4}$. The equivalent factorial expression is $n!/[2^2\,2!\,(n-4)!]$: within-pair order and pair order do not change the function.

**Universal expression.** The bijective construction gives $3\binom{n}{4}$, option 2, throughout the stated domain where the required objects exist. The result is not extrapolated from one successful numerical example.

**Compare the other laws.** The alternative $\binom{n}{4}$ selects the four moved labels but omits their three pairings. At $n=5$ it gives $5$, whereas the required count is $15$. The alternative $6\binom{n}{4}$ orders the two disjoint transpositions and counts each resulting permutation twice. At $n=5$ it gives $30$, whereas the required count is $15$. The alternative $\binom{n}{2}^2$ chooses two pairs independently, permitting overlap and ordering identical or exchanged selections. At $n=5$ it gives $100$, whereas the required count is $15$. A numerical disagreement disproves a competing expression asserted for every valid parameter; agreement at a degenerate parameter would not establish that universal claim.

**Boundary and transfer.** The count is zero for n<4; at n=4 there are three maps. These are permutations with exactly two transpositions. Counting all involutions requires summing over every permitted number of transpositions.

## Q29

**Derive the count or structural law.** Exactly four labels move. Choose them in $\binom{n}{4}$ ways. For four fixed distinct labels a,b,c,d, the only pairings are (ab)(cd), (ac)(bd), (ad)(bc). Each defines exactly one permutation and all remaining labels are fixed. Thus the count is $3\binom{n}{4}$. The equivalent factorial expression is $n!/[2^2\,2!\,(n-4)!]$: within-pair order and pair order do not change the function.

**Check each scope claim.** Option 1: If a permutation is its own inverse, each orbit has length dividing two. Its cycles are therefore fixed points or transpositions. Option 2: In the four-cycle (1234), two applications take 1 to 3, not 1. Thus its square is not the identity. Option 3: (12)(34) and (34)(12) have the same values at every input. Ordering the two cycles introduces a factor of two with no new function. Option 4: The identity is an involution consisting entirely of fixed points. A nonidentity involution may also have fixed points. Thus option 1 is correct.

**Boundary and transfer.** The count is zero for n<4; at n=4 there are three maps. These are permutations with exactly two transpositions. Counting all involutions requires summing over every permitted number of transpositions.

## Q30

**Derive the count or structural law.** Let c_1,c_2,c_3 be the multiplicities of outputs 1,2,3. Each is nonnegative and their sum is n. A vector reconstructs exactly the sequence containing c_1 ones followed by c_2 twos and c_3 threes. Put n stars and two separators in a row. Choosing the two separator positions among n+2 positions gives $\binom{n+2}{2}$. Empty blocks correspond to adjacent separators or boundary separators, so unused output labels are included.

**Substitute the stated parameter.** At $n=5$ the law gives $\binom{(5)+2}{2}=21$. Every label and every constraint is retained from the stem.

**Compute all alternatives.** Option 1 gives $\binom{(5)}{3}=10$; it chooses three input positions rather than the three possibly zero output multiplicities. Option 2 gives $(5)^3=125$; it counts maps from three labelled inputs into an n-element codomain, a reverse-type task. Option 3 gives 21, equal to the derived result. Option 4 gives $3^(5)=243$; it counts arbitrary output tuples without the weak monotonicity constraint.

**Boundary and transfer.** At n=0 the single empty sequence corresponds to the all-zero multiplicity vector. If onto-ness is added, each count must be positive, changing the answer to $\binom{n-1}{2}$ for n≥3. Weak and strict monotonicity are different conditions.

## Q31

**Derive the count or structural law.** Let c_1,c_2,c_3 be the multiplicities of outputs 1,2,3. Each is nonnegative and their sum is n. A vector reconstructs exactly the sequence containing c_1 ones followed by c_2 twos and c_3 threes. Put n stars and two separators in a row. Choosing the two separator positions among n+2 positions gives $\binom{n+2}{2}$. Empty blocks correspond to adjacent separators or boundary separators, so unused output labels are included.

**Substitute the stated parameter.** At $n=8$ the law gives $\binom{(8)+2}{2}=45$. Every label and every constraint is retained from the stem.

**Compute all alternatives.** Option 1 gives $(8)^3=512$; it counts maps from three labelled inputs into an n-element codomain, a reverse-type task. Option 2 gives 45, equal to the derived result. Option 3 gives $3^(8)=6561$; it counts arbitrary output tuples without the weak monotonicity constraint. Option 4 gives $\binom{(8)}{3}=56$; it chooses three input positions rather than the three possibly zero output multiplicities.

**Boundary and transfer.** At n=0 the single empty sequence corresponds to the all-zero multiplicity vector. If onto-ness is added, each count must be positive, changing the answer to $\binom{n-1}{2}$ for n≥3. Weak and strict monotonicity are different conditions.

## Q32

**Derive the count or structural law.** Let c_1,c_2,c_3 be the multiplicities of outputs 1,2,3. Each is nonnegative and their sum is n. A vector reconstructs exactly the sequence containing c_1 ones followed by c_2 twos and c_3 threes. Put n stars and two separators in a row. Choosing the two separator positions among n+2 positions gives $\binom{n+2}{2}$. Empty blocks correspond to adjacent separators or boundary separators, so unused output labels are included.

**Universal expression.** The bijective construction gives $\binom{n+2}{2}$, option 1, throughout the stated domain where the required objects exist. The result is not extrapolated from one successful numerical example.

**Compare the other laws.** The alternative $3^n$ counts arbitrary output tuples without the weak monotonicity constraint. At $n=5$ it gives $243$, whereas the required count is $21$. The alternative $\binom{n}{3}$ chooses three input positions rather than the three possibly zero output multiplicities. At $n=5$ it gives $10$, whereas the required count is $21$. The alternative $n^3$ counts maps from three labelled inputs into an n-element codomain, a reverse-type task. At $n=5$ it gives $125$, whereas the required count is $21$. A numerical disagreement disproves a competing expression asserted for every valid parameter; agreement at a degenerate parameter would not establish that universal claim.

**Boundary and transfer.** At n=0 the single empty sequence corresponds to the all-zero multiplicity vector. If onto-ness is added, each count must be positive, changing the answer to $\binom{n-1}{2}$ for n≥3. Weak and strict monotonicity are different conditions.

## Q33

**Derive the count or structural law.** Let c_1,c_2,c_3 be the multiplicities of outputs 1,2,3. Each is nonnegative and their sum is n. A vector reconstructs exactly the sequence containing c_1 ones followed by c_2 twos and c_3 threes. Put n stars and two separators in a row. Choosing the two separator positions among n+2 positions gives $\binom{n+2}{2}$. Empty blocks correspond to adjacent separators or boundary separators, so unused output labels are included.

**Check each scope claim.** Option 1: The constant sequence of n ones is weakly increasing and uses neither 2 nor 3. Surjectivity is an additional condition. Option 2: The legal sequence (1,1,2,3) can be permuted to (3,1,2,1), which fails monotonicity. Arbitrary permutations are not new valid encodings. Option 3: At n=2 there are six weakly increasing tuples but nine unrestricted tuples. The tuple (2,1) is an explicit excluded assignment. Option 4: Strict increase excludes equal outputs at distinct positions. Its count into three labels is $\binom{3}{n}$ for n≤3 and zero otherwise. Thus option 4 is correct.

**Boundary and transfer.** At n=0 the single empty sequence corresponds to the all-zero multiplicity vector. If onto-ness is added, each count must be positive, changing the answer to $\binom{n-1}{2}$ for n≥3. Weak and strict monotonicity are different conditions.

## Q34

**Derive the count or structural law.** Name the three target labels a,b,c and their disjoint fibers F_a,F_b,F_c, each of size n. A right inverse g must satisfy $g(a)\in F_a$, $g(b)\in F_b$, $g(c)\in F_c$. Each of these n choices is independent, giving $n\cdot n\cdot n=n^3$. Every such map satisfies $f(g(b))=b$ at each target. Distinct choices yield distinct reverse maps, and every right inverse must make precisely these choices.

**Substitute the stated parameter.** At $n=5$ the law gives $(5)^3=125$. Every label and every constraint is retained from the stem.

**Compute all alternatives.** Option 1 gives $3^(5)=243$; it counts unrestricted maps from n inputs to three outputs, with different domain and codomain. Option 2 gives $(3(5))^3=3375$; it allows each target to choose from all domain points instead of its own n-element fiber. Option 3 gives $(5)!=120$; it counts a permutation of n labels rather than selecting one antecedent for each of three target labels. Option 4 gives 125, equal to the derived result.

**Boundary and transfer.** The n≥1 condition makes the map onto. For n=1 each fiber is a singleton and the unique section is the true inverse. For n>1 no section recovers every original input; the other identity fails on unchosen antecedents.

## Q35

**Derive the count or structural law.** Name the three target labels a,b,c and their disjoint fibers F_a,F_b,F_c, each of size n. A right inverse g must satisfy $g(a)\in F_a$, $g(b)\in F_b$, $g(c)\in F_c$. Each of these n choices is independent, giving $n\cdot n\cdot n=n^3$. Every such map satisfies $f(g(b))=b$ at each target. Distinct choices yield distinct reverse maps, and every right inverse must make precisely these choices.

**Substitute the stated parameter.** At $n=8$ the law gives $(8)^3=512$. Every label and every constraint is retained from the stem.

**Compute all alternatives.** Option 1 gives $(3(8))^3=13824$; it allows each target to choose from all domain points instead of its own n-element fiber. Option 2 gives $(8)!=40320$; it counts a permutation of n labels rather than selecting one antecedent for each of three target labels. Option 3 gives 512, equal to the derived result. Option 4 gives $3^(8)=6561$; it counts unrestricted maps from n inputs to three outputs, with different domain and codomain.

**Boundary and transfer.** The n≥1 condition makes the map onto. For n=1 each fiber is a singleton and the unique section is the true inverse. For n>1 no section recovers every original input; the other identity fails on unchosen antecedents.

## Q36

**Derive the count or structural law.** Name the three target labels a,b,c and their disjoint fibers F_a,F_b,F_c, each of size n. A right inverse g must satisfy $g(a)\in F_a$, $g(b)\in F_b$, $g(c)\in F_c$. Each of these n choices is independent, giving $n\cdot n\cdot n=n^3$. Every such map satisfies $f(g(b))=b$ at each target. Distinct choices yield distinct reverse maps, and every right inverse must make precisely these choices.

**Universal expression.** The bijective construction gives $n^3$, option 2, throughout the stated domain where the required objects exist. The result is not extrapolated from one successful numerical example.

**Compare the other laws.** The alternative $n!$ counts a permutation of n labels rather than selecting one antecedent for each of three target labels. At $n=5$ it gives $120$, whereas the required count is $125$. The alternative $3^n$ counts unrestricted maps from n inputs to three outputs, with different domain and codomain. At $n=5$ it gives $243$, whereas the required count is $125$. The alternative $(3n)^3$ allows each target to choose from all domain points instead of its own n-element fiber. At $n=5$ it gives $3375$, whereas the required count is $125$. A numerical disagreement disproves a competing expression asserted for every valid parameter; agreement at a degenerate parameter would not establish that universal claim.

**Boundary and transfer.** The n≥1 condition makes the map onto. For n=1 each fiber is a singleton and the unique section is the true inverse. For n>1 no section recovers every original input; the other identity fails on unchosen antecedents.

## Q37

**Derive the count or structural law.** Name the three target labels a,b,c and their disjoint fibers F_a,F_b,F_c, each of size n. A right inverse g must satisfy $g(a)\in F_a$, $g(b)\in F_b$, $g(c)\in F_c$. Each of these n choices is independent, giving $n\cdot n\cdot n=n^3$. Every such map satisfies $f(g(b))=b$ at each target. Distinct choices yield distinct reverse maps, and every right inverse must make precisely these choices.

**Check each scope claim.** Option 1: If $f\circ g=\operatorname{id}$, every target b equals f(g(b)), proving onto-ness of f. If g(b)=g(c), applying f gives b=c, proving injection of g. Option 2: On a fiber of size two, f merges its two inputs although a section chooses one successfully. A right inverse does not remove collisions in f. Option 3: Fibers of distinct targets are disjoint: one input has only one output. The same input cannot be chosen for two different targets by a right inverse. Option 4: For an empty target fiber F_b, no g(b) can satisfy f(g(b))=b. A missing fiber makes a right inverse impossible. Thus option 1 is correct.

**Boundary and transfer.** The n≥1 condition makes the map onto. For n=1 each fiber is a singleton and the unique section is the true inverse. For n>1 no section recovers every original input; the other identity fails on unchosen antecedents.

## Q38

**Derive the count or structural law.** Fix one distinguished label a as the first symbol in the cycle display. Arrange the n−1 remaining labels in any order after a; each ordering determines the successor of every label and closes the final successor back to a. Different orderings with this anchored start give different functions. Conversely, following any single n-cycle from a recovers exactly that ordering. Hence there are (n−1)! cycles. Starting with n! unrestricted displays and dividing by the n cyclic rotations gives the same result.

**Substitute the stated parameter.** At $n=5$ the law gives $((5)-1)!=24$. Every label and every constraint is retained from the stem.

**Compute all alternatives.** Option 1 gives $(5)!=120$; it orders all labels while retaining an irrelevant choice of starting point in the displayed cycle. Option 2 gives $2^(5)=32$; it chooses a subset of labels rather than a cyclic successor assignment using every label. Option 3 gives $(5)((5)-1)=20$; it chooses one ordered pair of distinct labels, not all successive values of the cycle. Option 4 gives 24, equal to the derived result.

**Boundary and transfer.** The formula uses n≥1. At n=1 there is one fixed-point cycle; at n=2 there is one transposition. An n-cycle has order n, while a permutation with several cycles has order equal to the least common multiple of their lengths.

## Q39

**Derive the count or structural law.** Fix one distinguished label a as the first symbol in the cycle display. Arrange the n−1 remaining labels in any order after a; each ordering determines the successor of every label and closes the final successor back to a. Different orderings with this anchored start give different functions. Conversely, following any single n-cycle from a recovers exactly that ordering. Hence there are (n−1)! cycles. Starting with n! unrestricted displays and dividing by the n cyclic rotations gives the same result.

**Substitute the stated parameter.** At $n=8$ the law gives $((8)-1)!=5040$. Every label and every constraint is retained from the stem.

**Compute all alternatives.** Option 1 gives $2^(8)=256$; it chooses a subset of labels rather than a cyclic successor assignment using every label. Option 2 gives $(8)((8)-1)=56$; it chooses one ordered pair of distinct labels, not all successive values of the cycle. Option 3 gives 5040, equal to the derived result. Option 4 gives $(8)!=40320$; it orders all labels while retaining an irrelevant choice of starting point in the displayed cycle.

**Boundary and transfer.** The formula uses n≥1. At n=1 there is one fixed-point cycle; at n=2 there is one transposition. An n-cycle has order n, while a permutation with several cycles has order equal to the least common multiple of their lengths.

## Q40

**Derive the count or structural law.** Fix one distinguished label a as the first symbol in the cycle display. Arrange the n−1 remaining labels in any order after a; each ordering determines the successor of every label and closes the final successor back to a. Different orderings with this anchored start give different functions. Conversely, following any single n-cycle from a recovers exactly that ordering. Hence there are (n−1)! cycles. Starting with n! unrestricted displays and dividing by the n cyclic rotations gives the same result.

**Universal expression.** The bijective construction gives $(n-1)!$, option 2, throughout the stated domain where the required objects exist. The result is not extrapolated from one successful numerical example.

**Compare the other laws.** The alternative $n!$ orders all labels while retaining an irrelevant choice of starting point in the displayed cycle. At $n=5$ it gives $120$, whereas the required count is $24$. The alternative $2^n$ chooses a subset of labels rather than a cyclic successor assignment using every label. At $n=5$ it gives $32$, whereas the required count is $24$. The alternative $n(n-1)$ chooses one ordered pair of distinct labels, not all successive values of the cycle. At $n=5$ it gives $20$, whereas the required count is $24$. A numerical disagreement disproves a competing expression asserted for every valid parameter; agreement at a degenerate parameter would not establish that universal claim.

**Boundary and transfer.** The formula uses n≥1. At n=1 there is one fixed-point cycle; at n=2 there is one transposition. An n-cycle has order n, while a permutation with several cycles has order equal to the least common multiple of their lengths.

## Q41

**Derive the count or structural law.** Fix one distinguished label a as the first symbol in the cycle display. Arrange the n−1 remaining labels in any order after a; each ordering determines the successor of every label and closes the final successor back to a. Different orderings with this anchored start give different functions. Conversely, following any single n-cycle from a recovers exactly that ordering. Hence there are (n−1)! cycles. Starting with n! unrestricted displays and dividing by the n cyclic rotations gives the same result.

**Check each scope claim.** Option 1: The cycle (123) sends 1 to 2, whereas its reverse (132) sends 1 to 3. For length at least three, the reverse is a different permutation. Option 2: The same three-cycle counterexample disproves universal equality with the reverse. Only cycles of length one or two coincide with their reverses. Option 3: (123) and (231) both send 1→2, 2→3 and 3→1. Rotating a display does not change the function. Option 4: A single cycle of length greater than one has no fixed point: every label has a different successor. The length-one case is the exception. Thus option 1 is correct.

**Boundary and transfer.** The formula uses n≥1. At n=1 there is one fixed-point cycle; at n=2 there is one transposition. An n-cycle has order n, while a permutation with several cycles has order equal to the least common multiple of their lengths.

## Q42

**Derive the count or structural law.** The two distinguished points have their outputs forced to themselves. No other input may use those two targets because a permutation is injective. Thus the remaining n−2 input labels must biject to the remaining n−2 target labels, with (n−2)! choices. Additional fixed points among those remaining labels are allowed. Every such remaining permutation extends uniquely by the two fixed assignments.

**Substitute the stated parameter.** At $n=5$ the law gives $((5)-2)!=6$. Every label and every constraint is retained from the stem.

**Compute all alternatives.** Option 1 gives 6, equal to the derived result. Option 2 gives $((5)-1)!=24$; it forces only one specified point to be fixed and leaves the second unconstrained. Option 3 gives $(5)!=120$; it permutes the two prescribed fixed points as well as the other labels. Option 4 gives $\binom{(5)}{2}=10$; it chooses which labels to fix although those labels are already specified, and omits the remaining permutation.

**Boundary and transfer.** The two specified distinct points require n≥2. At n=2 the identity is the unique map. Choosing exactly two unspecified fixed points would instead give $\binom{n}{2}D_{n-2}$; the choice factor belongs to that different task.

## Q43

**Derive the count or structural law.** The two distinguished points have their outputs forced to themselves. No other input may use those two targets because a permutation is injective. Thus the remaining n−2 input labels must biject to the remaining n−2 target labels, with (n−2)! choices. Additional fixed points among those remaining labels are allowed. Every such remaining permutation extends uniquely by the two fixed assignments.

**Substitute the stated parameter.** At $n=8$ the law gives $((8)-2)!=720$. Every label and every constraint is retained from the stem.

**Compute all alternatives.** Option 1 gives $((8)-1)!=5040$; it forces only one specified point to be fixed and leaves the second unconstrained. Option 2 gives $(8)!=40320$; it permutes the two prescribed fixed points as well as the other labels. Option 3 gives $\binom{(8)}{2}=28$; it chooses which labels to fix although those labels are already specified, and omits the remaining permutation. Option 4 gives 720, equal to the derived result.

**Boundary and transfer.** The two specified distinct points require n≥2. At n=2 the identity is the unique map. Choosing exactly two unspecified fixed points would instead give $\binom{n}{2}D_{n-2}$; the choice factor belongs to that different task.

## Q44

**Derive the count or structural law.** The two distinguished points have their outputs forced to themselves. No other input may use those two targets because a permutation is injective. Thus the remaining n−2 input labels must biject to the remaining n−2 target labels, with (n−2)! choices. Additional fixed points among those remaining labels are allowed. Every such remaining permutation extends uniquely by the two fixed assignments.

**Universal expression.** The bijective construction gives $(n-2)!$, option 3, throughout the stated domain where the required objects exist. The result is not extrapolated from one successful numerical example.

**Compare the other laws.** The alternative $n!$ permutes the two prescribed fixed points as well as the other labels. At $n=5$ it gives $120$, whereas the required count is $6$. The alternative $\binom{n}{2}$ chooses which labels to fix although those labels are already specified, and omits the remaining permutation. At $n=5$ it gives $10$, whereas the required count is $6$. The alternative $(n-1)!$ forces only one specified point to be fixed and leaves the second unconstrained. At $n=5$ it gives $24$, whereas the required count is $6$. A numerical disagreement disproves a competing expression asserted for every valid parameter; agreement at a degenerate parameter would not establish that universal claim.

**Boundary and transfer.** The two specified distinct points require n≥2. At n=2 the identity is the unique map. Choosing exactly two unspecified fixed points would instead give $\binom{n}{2}D_{n-2}$; the choice factor belongs to that different task.

## Q45

**Derive the count or structural law.** The two distinguished points have their outputs forced to themselves. No other input may use those two targets because a permutation is injective. Thus the remaining n−2 input labels must biject to the remaining n−2 target labels, with (n−2)! choices. Additional fixed points among those remaining labels are allowed. Every such remaining permutation extends uniquely by the two fixed assignments.

**Check each scope claim.** Option 1: Once the prescribed two assignments are fixed, the remaining labels can still be permuted. For n=4 the two residual labels may remain fixed or be exchanged. Option 2: If no additional fixed points are allowed, the residual permutation must have no fixed point, so the count becomes the derangement number D_{n−2}. Option 3: The identity fixes the two prescribed points and also every other point. It is a legal map under the question as written. Option 4: Exchanging the prescribed points sends each to the other and contradicts the two required fixed assignments. Their outputs are not free. Thus option 2 is correct.

**Boundary and transfer.** The two specified distinct points require n≥2. At n=2 the identity is the unique map. Choosing exactly two unspecified fixed points would instead give $\binom{n}{2}D_{n-2}$; the choice factor belongs to that different task.

## Q46

**Count by the exact fixed image.** An idempotent endofunction fixes exactly its image. For image size k on four labelled elements, choose that image in $\binom{4}{k}$ ways; its assignments are fixed. The remaining 4−k inputs independently choose from those k outputs, giving $k^{4-k}$ maps for the chosen image. Different image sets and different image sizes are disjoint cases.

The nonempty domain prohibits an empty image. Sum the four allowed sizes:
$$\binom{4}{1}1^3+\binom{4}{2}2^2+\binom{4}{3}3^1+\binom{4}{4}4^0=4+24+12+1=41.$$
Option 3 is correct. Twenty-four counts only the maps with a two-element fixed image. Thirty-six combines the two-element and three-element cases but omits the four constant maps and the identity. Sixty-four is $4^3$, a free-output count with no appropriate idempotence restriction.

**Why the construction is exhaustive.** If f is idempotent and y=f(x), then f(y)=y. Thus all nonimage points map into fixed image points, exactly as constructed. Conversely every construction has $f(f(x))=f(x)$ at every x. This establishes necessity and sufficiency, rather than checking selected tuples only.

**Generalization.** For a nonempty n-element carrier, sum $\binom{n}{k}k^{n-k}$ for k=1 through n. The empty carrier has one empty idempotent map and must be treated separately from a sum with no nonempty image cases.

## Q47

**The composition identity first forces f to be injective.** If f(a)=f(a'), applying g and using $g\circ f=\operatorname{id}_A$ gives a=a'. There are $3\cdot2=6$ injections from the two labelled A-elements into three labelled B-elements.

For each such f, the values of g on the two attained B-points are forced by their unique antecedents. At the sole unused B-point, g may independently choose either A-point. Thus each f has exactly two left inverses. Multiply to get $6\cdot2=12$, option 3.

**Example.** If A={0,1}, B={a,b,c}, f(0)=a and f(1)=b, then g(a)=0 and g(b)=1 are forced; g(c)=0 or 1 gives the two pairs belonging to this f. No noninjective f can appear because it would violate the first argument.

**Options.** Six counts the injections but omits the two possible reverse maps. Eight counts all $2^3$ reverse assignments for a fixed B without imposing their dependence on a chosen f. Eighteen is $3^2\cdot2$ and incorrectly lets f have collisions. The ordered pair (f,g) includes both functions, so counting only one factor is insufficient.

**Transfer.** For m>0 and n≥m, the number of pairs $f:A\to B,g:B\to A$ with the left identity is $n!/(n-m)!\,m^{n-m}$. If A is empty and B nonempty, the forward map exists but no reverse total map exists; the pair count is zero. If both are empty, the unique empty pair satisfies the identity.
