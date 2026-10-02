## 13. Forty fully worked problems

The problems progress from interpreting symbols to independent proof and verification. All statements and solutions are independently written. "Course-pattern" identifies the reasoning skill found in the cited written material, not a verbatim reproduction of its question. Each solution gives a derivation, a check or boundary condition, and the lesson to transfer to a new question. You may read the solutions immediately; this section does not require a pre-study test.

### Problem 1. Evaluate the expression tree

**Statement.** For E=(x+y′)(x′+z), evaluate assignments 011 and 101, in input order x,y,z. Explain why complement scope matters. **Origin:** Original notation exercise.

**Solution.** On 011, y′=0 and x′=1. The first factor is 0+0=0; the second is 1+1=1. Their product is zero. On 101, y′=1 and x′=0. The factors are 1+1=1 and 0+1=1, so the output is one. The prime on y affects that leaf only; the second factor's prime affects x only. Complementing the first whole factor would create (x+y)′, which is a different tree and, on 101, equals zero. **Transfer:** Label intermediate nodes before substituting values in a nested formula.

### Problem 2. Build and independently check a truth table

**Statement.** Construct the table of f=x′y+z. Identify all one rows. **Origin:** MIT/Cornell specification-to-table pattern, new function.

**Solution.** If z=1, the output is one regardless of the other two inputs. If z=0, the output is one only on x=0,y=1. Thus in binary row order the vector is 0,1,1,1,0,1,0,1; its one rows are 001,010,011,101,111. There are five satisfying assignments. As a separate check, the z term covers four assignments, x′y covers two, and their overlap covers one, so their union has 4+2−1=5 assignments. The subtraction here is ordinary arithmetic on **set sizes**, not Boolean subtraction of expressions. **Transfer:** Use a structural case split and a count to catch an omitted row.

### Problem 3. Detect an incomplete or inconsistent specification

**Statement.** A two-input specification says "output one whenever x=1" and "output zero whenever y=1." Is it a function? What if the second condition is restricted to x=0? **Origin:** Original specification audit.

**Solution.** At 11 the first statement requires one and the second requires zero. No deterministic function satisfies both. Restricting the second statement to x=0 removes the conflict: rows 10 and 11 are one and row 01 is zero. Row 00 is still unspecified, so there are two completions. Choosing its value as zero gives f=x; choosing one gives f=x+y′. Both satisfy all three fixed rows. **Transfer:** Conflicting conditions and missing conditions are distinct defects; enumerate the affected rows rather than accepting vague prose.

### Problem 4. Count functions under different constraints

**Statement.** Count all four-input scalar functions; then count three-output functions on two inputs; then count completions with five free scalar rows. **Origin:** Original counting exercise.

**Solution.** Four inputs produce sixteen rows. Each row has two choices, hence 2<sup>16</sup>=65536 functions. Two inputs produce four rows, each with three independent binary output choices. This is twelve independent output bits, yielding 2<sup>12</sup>=4096 functions. Five unconstrained scalar rows give 2<sup>5</sup>=32 completions, provided no additional relation couples them. With no free rows there is one completion; an inconsistent fixed row instead gives none. **Transfer:** Count independent output decisions after counting input assignments.

### Problem 5. Count literal occurrences and compare objectives

**Statement.** Compare xy+xz with x(y+z). How many literal occurrences and distinct inputs are present? Does factoring prove the fastest implementation? **Origin:** CMU literal-counting pattern.

**Solution.** The SOP has four occurrences: x,y,x,z. The factored expression has three: x,y,z. Both have the same three distinct inputs and the same function by distributivity. Factoring reduces this syntactic metric. With two-input gates, the SOP can compute two products in parallel then OR them, whereas the factored form computes one OR then one AND; both have depth two under equal input arrival times. Gate type, loading, fan-out, and unequal arrival times can change actual delay. No global fastest-implementation conclusion follows from the occurrence count. **Transfer:** State the optimization metric before claiming an expression is better.

### Problem 6. Prove both distributive laws by cases

**Statement.** Prove x(y+z)=xy+xz and x+yz=(x+y)(x+z), without assuming real-number algebra. **Origin:** Cambridge/Berkeley law-verification pattern.

**Solution.** In the first identity, x=0 makes both sides zero and x=1 makes both sides y+z. Those two cases exhaust the domain. In the second, x=0 makes both sides yz and x=1 makes both sides one. Neither argument depends on particular values of y or z. The same proof works if those letters stand for larger Boolean subfunctions. The second law would fail over ordinary integers: with x=y=z=1 the corresponding arithmetic sides are two and four. **Transfer:** A two-case proof often exposes a Boolean law more clearly than a long expansion.

### Problem 7. Absorb before expanding

**Statement.** Simplify f=xy+x+z(x+y). **Origin:** Berkeley absorption pattern, independently varied expression.

**Solution.** First absorb xy into x: f=x+z(x+y). Distribute only the remaining factor to obtain x+xz+yz. Absorb xz into x, leaving f=x+yz. A check by cofactors is quick: when x=1, both original and final expressions are one; when x=0, both are yz. Expanding the original expression immediately would be valid but would create a redundant xy term that is easy to lose track of. **Transfer:** Search for a covering term before making an expression larger.

### Problem 8. Covering in both orientations

**Statement.** Simplify (x+x′y)(x+x′z), and give the dual reduction. **Origin:** Cambridge covering-pattern exercise.

**Solution.** Reduce each factor: x+x′y=x+y and x+x′z=x+z. Their product is x+yz by OR distributivity. For the dual expression, swap AND and OR, retaining literal complements: x(x′+y)+x(x′+z) becomes xy+xz=x(y+z). The dual of the final x+yz is x(y+z), as expected. Do not complement x when taking the dual; the existing prime remains where it was. **Transfer:** Duality provides a cross-check on a derivation's structure.

### Problem 9. Prove consensus with both algebra and containment

**Statement.** Prove xy+x′z+yz=xy+x′z and justify the dual theorem. **Origin:** Original two-proof consolidation of consensus.

**Solution.** Algebraically, replace yz by yz(x+x′)=xyz+x′yz. The xy term absorbs xyz and x′z absorbs x′yz. For containment, any assignment making yz=1 has y=z=1. If x=1 it satisfies xy; if x=0 it satisfies x′z. The extra term therefore adds no on-set row. Duality yields (x+y)(x′+z)(y+z)=(x+y)(x′+z). These proofs establish steady-state equality; they do not establish equality of transient waveforms. **Transfer:** Redundancy can arise through two terms jointly, without one term alone covering the removed term.

### Problem 10. Apply a theorem to a compound selector

**Statement.** Simplify H=(p+q)r+(p+q)′s+rs. **Origin:** Original compound substitution exercise.

**Solution.** Introduce t=p+q only as a temporary expression name. H=tr+t′s+rs, so consensus removes rs, leaving tr+t′s. Substitute back: H=(p+q)r+(p+q)′s. If desired, De Morgan gives the second term as p′q′s. The eliminated term is covered because t is binary even though it is not a primary input. An incorrect replacement of (p+q)′ by p+q′ would change the function. **Transfer:** Boolean laws accept compound operands, but their complement scope must survive substitution intact.

### Problem 11. Push nested complements inward

**Statement.** Reduce K=[(x+y′)(z+w)]′ to an SOP with complements only on variables. **Origin:** Cambridge nested De Morgan pattern, new expression.

**Solution.** The top node is a complemented AND, so K=(x+y′)′+(z+w)′. Each summand is now a complemented OR. Therefore K=x′(y′)′+z′w′=x′y+z′w′. Check x=0,y=1,z=1,w=0: the original first factor is zero, so the complemented product is one; the final first term is one. Check all inputs one: the original product is one and the final two terms are zero, hence both outputs are zero. Those checks supplement the general derivation; they do not replace it. **Transfer:** Complement one tree node at a time.

### Problem 12. Distinguish dual, complement, and input inversion

**Statement.** For E=x+y′z+1·w, write all three transformations. **Origin:** Original duality audit.

**Solution.** The dual is E<sup>d</sup>=x(y′+z)(0+w)=xw(y′+z). The output complement is E′=x′(y′z)′w′=x′(y+z′)w′. Input inversion gives E(x′,y′,z′,w′)=x′+yz′+w′. Complementing that last expression reproduces x(y′+z)w, the dual, confirming the general relation. The constant one became zero only in the dual; literal polarity changed in input inversion, while complementing the output required De Morgan. **Transfer:** Write three distinct operations rather than use the vague phrase "invert the expression."

### Problem 13. Count and refute self-duality

**Statement.** How many three-input self-dual functions exist? Does balanced two-input XOR qualify? **Origin:** Original advanced counting problem.

**Solution.** Eight assignments pair as 000/111,001/110,010/101,011/100. On each pair choose the first output freely, and the other must be its complement. Four choices yield 2<sup>4</sup>=16 functions. XOR on two inputs is balanced, with output vector 0,1,1,0, but the complementary pair 00/11 has equal outputs. Thus XOR is not self-dual. Majority on three inputs is self-dual because complementary vote totals sum to three, so exactly one member of each pair has at least two ones. **Transfer:** Balancedness is necessary, whereas complementary-pair opposition is the exact condition.

### Problem 14. Use duplication to expose majority

**Statement.** Simplify F=x′yz+xy′z+xyz′+xyz. **Origin:** Stanford/Berkeley majority-reduction pattern.

**Solution.** Use idempotence to supply three copies of xyz. Group x′yz+xyz=yz, xy′z+xyz=xz, and xyz′+xyz=xy. Therefore F=xy+xz+yz. The pairs cover four one rows, and their overlaps at 111 are harmless because OR is idempotent. Direct interpretation verifies the result: it is one exactly when at least two inputs are one. Replacing OR with XOR in the original duplication argument would be invalid, since duplicating a term under XOR cancels it. **Transfer:** The operation governing duplicates determines whether they can be introduced safely.

### Problem 15. Simplify a POS without losing factors

**Statement.** Simplify F=(x+y)(x+y′)(x′+z). **Origin:** Original POS combining problem.

**Solution.** The first two factors combine to x because (x+y)(x+y′)=x+yy′=x. Now F=x(x′+z)=xx′+xz=xz. A cofactor check gives zero on x=0 and z on x=1, exactly as xz does. It would be wrong to cancel the x terms from inside the original parentheses as if the expression were a product of ordinary linear polynomials. **Transfer:** Apply a known identity to a complete matching subexpression, then simplify the resulting whole expression.

### Problem 16. Determine when cancellation becomes valid

**Statement.** Does x+y=x+z force y=z? Give a counterexample and an extra assumption that makes the conclusion valid. Do the same for xy=xz. **Origin:** Original false-law problem.

**Solution.** For OR choose x=1,y=0,z=1. Both sides are one, yet y and z differ. Adding the assumption x=0 makes the premise become y=z directly. For AND choose x=0,y=0,z=1; both products are zero. Adding x=1 makes the premise become y=z. More generally, equality of the OR expressions constrains y and z only on assignments with x=0; equality of the products constrains them only on assignments with x=1. **Transfer:** Determine where the common operand hides information before attempting cancellation.

### Problem 17. Solve an XOR equation

**Statement.** Solve x⊕y=z for y and explain uniqueness. **Origin:** Original cancellation exercise.

**Solution.** XOR x with both sides: x⊕(x⊕y)=x⊕z. Associativity and x⊕x=0 give y=x⊕z. Substitution into the original equation gives x⊕x⊕z=z, verifying existence. If two values of y satisfied it, XOR cancellation would force them equal, proving uniqueness. For x=0 the solution is y=z; for x=1 it is y=z′. This behavior also shows why an OR equation would not have the same unique solution rule. **Transfer:** XOR cancellation is legitimate because XOR with a fixed value is a reversible operation.

### Problem 18. Trace parity and equality separately

**Statement.** Simplify P=x⊕y⊕x⊕1⊕y⊕z. Does it express equality of three inputs? **Origin:** Original parity tracing.

**Solution.** Reorder and regroup using XOR commutativity and associativity. The two x terms cancel; the two y terms cancel. P=1⊕z=z′. It depends only on z and cannot express equality of all three inputs. A three-input equality function is xy z+x′y′z′, with only 000 and 111 as one rows. A three-input XNOR interpreted as complement of parity is one on even parity rows 000,011,101,110, which is different. **Transfer:** "XNOR" for many inputs must be interpreted according to its stated definition, rather than assumed to mean all inputs equal.

### Problem 19. State the exact condition for OR to equal XOR

**Statement.** When may xy+x′z be replaced by xy⊕x′z? May xy+xz always be replaced similarly? **Origin:** Cornell disjoint-product pattern.

**Solution.** The first two products cannot both be one because their conjunction includes xx′. Therefore the OR and XOR agree on every assignment. For the second pair, their conjunction is xyz, which is one on 111. There OR gives one while XOR gives zero, so replacement fails. In general, if f and g never overlap then fg=0 and both combinations are one exactly on their union; if they overlap, the differing result on any overlap row refutes equality. **Transfer:** Disjointness is the necessary and sufficient condition, not simply having two SOP terms.

### Problem 20. Derive a two-input ANF from a table

**Statement.** A function has output vector 1,1,0,1 in order 00,01,10,11. Find its ANF. **Origin:** Original transform exercise.

**Solution.** Write f=c₀⊕c₁x⊕c₂y⊕c₃xy. The constant coefficient is one. The x coefficient is f(10)⊕f(00)=0⊕1=1. The y coefficient is f(01)⊕f(00)=1⊕1=0. The product coefficient is the XOR of all four outputs, 1⊕1⊕0⊕1=1. Thus f=1⊕x⊕xy. On x=0 this gives one; on x=1 it becomes y, matching both remaining rows. Its OR-style expression is x′+y. **Transfer:** ANF and SOP can represent the same function through different operation systems.

### Problem 21. Find the algebraic degree of majority

**Statement.** Show that three-input majority equals xy⊕xz⊕yz and identify its degree. **Origin:** Original ANF application.

**Solution.** Split assignments by the number of one inputs. For zero or one one, all three products are zero. For exactly two ones, precisely one pair product is one. For three ones, all three pair products are one, whose XOR is one. These cases match majority on all eight assignments. This ANF has degree two. It is not affine: affine functions have no degree-two products in their unique ANF. The OR-SOP xy+xz+yz happens to agree here, despite overlapping terms, because all three overlap simultaneously at 111 and odd parity preserves one; replacing two overlapping terms individually would still be wrong. **Transfer:** Special aggregate agreement does not justify termwise replacement rules.

### Problem 22. Construct both full selector expressions

**Statement.** A function on x,y has one rows 01 and 11. Construct it from one rows and from zero rows, then reduce. **Origin:** MIT/Berkeley completeness pattern.

**Solution.** The one-row products are x′y and xy, so their OR is (x′+x)y=y. The zero rows are 00 and 10. Their zero-selecting sums are x+y and x′+y, so their product is (x+y)(x′+y)=y+xx′=y. The literal convention reverses between the two constructions: a one in the row contributes x to the product but x′ to the zero-selecting sum. Both reduce to the same function. **Transfer:** Evaluate a supposed selector on its designated row before trusting its polarity.

### Problem 23. Expand a missing input and count coverage

**Statement.** Expand xy′ as a function of x,y,z,w into full row selectors. How many rows does it cover? **Origin:** Cambridge full-expansion pattern.

**Solution.** Multiply by (z+z′)(w+w′), each equal to one. Expansion gives xy′zw+xy′zw′+xy′z′w+xy′z′w′. These are four distinct rows, since z and w each vary independently. The product fixes two of four inputs, hence covers 2<sup>4−2</sup>=4 assignments. If a product were xy′x′, it would cover zero rows because it is contradictory; counting three written literals would not repair that contradiction. **Transfer:** Count free distinct variables after checking literal consistency.

### Problem 24. Compute and interpret two cofactors

**Statement.** For f=(x+y)(x′+z), compute its x cofactors and reconstruct it. **Origin:** CMU restriction pattern, independently chosen function.

**Solution.** At x=0, the first factor becomes y and the second one, so f₀=y. At x=1, the first becomes one and the second z, so f₁=z. Shannon gives f=x′y+xz. To check algebraically, expanding the original gives xz+x′y+yz; the extra yz is the consensus term and is redundant. The cofactor approach found the compact result without generating that third term. **Transfer:** Restriction is often an efficient route to an expression's hidden selector structure.

### Problem 25. Derive the POS form of Shannon

**Statement.** Derive the factorization of f from f₀ and f₁. Explain why reversing their factors is generally wrong. **Origin:** CMU Homework 1, item 3 reasoning pattern.

**Solution.** The proposed product is (x+f₀)(x′+f₁). Set x=0: it becomes f₀·1=f₀. Set x=1: it becomes 1·f₁=f₁. It therefore agrees with f on both input slices. The reversed product (x′+f₀)(x+f₁) instead gives f₁ at x=0 and f₀ at x=1. For f=x, the cofactors are zero and one; the reversed expression becomes x′ rather than x. **Transfer:** A sum factor activates when its standalone literal is zero, while a product branch activates when its literal is one.

### Problem 26. Decompose on two variables

**Statement.** Let f=x′y′z+x′yz′+xyz. Give its four cofactors in x,y order and verify reconstruction. **Origin:** CMU multiple-restriction pattern.

**Solution.** Restricting 00 gives z, 01 gives z′, 10 gives zero, and 11 gives z. Therefore f=x′y′z+x′yz′+xy′·0+xyz. The zero branch disappears, reproducing the original. A wrong zero-x expansion using one-x cofactors would give zero or z on those first two branches and lose both prescribed values. Restricting y first and x second gives the same four functions attached to the same assignments. **Transfer:** Keep the subscript variable order fixed during repeated decomposition.

### Problem 27. Separate syntactic occurrence from essential support

**Statement.** Find the essential inputs of f=xy+xy′+zz′. **Origin:** Original support problem.

**Solution.** Combining gives xy+xy′=x, and zz′=0. Thus f=x. Its y cofactors both equal x; its z cofactors both equal x; its x cofactors are zero and one. Only x is essential. The written expression contained three input names, but the function depends on one. Consequently its three-input table has repeated patterns even though it still has eight rows when all three named inputs are enumerated. **Transfer:** Use unequal cofactors as the exact essential-dependence certificate.

### Problem 28. Compute a context-dependent Boolean difference

**Statement.** For f=x′y+xz, determine exactly when changing x changes the output. **Origin:** CMU Boolean-difference application pattern.

**Solution.** Its zero and one cofactors are y and z, so D<sub>x</sub>f=y⊕z. When y=z=0 the output stays zero; when y=z=1 it stays one. On y=0,z=1 it follows x; on y=1,z=0 it follows x′. Thus x is essential, with sensitivity one on two of the four contexts. The difference table does not distinguish those increasing and decreasing cases; the ordered pair of cofactors does. **Transfer:** Sensitivity detects change, whereas unateness describes its direction.

### Problem 29. Derive and test the Boolean product rule

**Statement.** Derive D<sub>x</sub>(fg) using zero cofactors and show why the ordinary rule fails for f=g=x. **Origin:** CMU advanced-difference proof pattern.

**Solution.** Let d=f₀⊕f₁ and e=g₀⊕g₁, so f₁=f₀⊕d and g₁=g₀⊕e. Then f₁g₁=f₀g₀⊕f₀e⊕g₀d⊕de, because AND distributes over XOR. XOR with f₀g₀ cancels that first term, leaving D<sub>x</sub>(fg)=f₀e⊕g₀d⊕de. For f=g=x, both zero cofactors are zero and both differences are one, so the extra term alone gives one. A naive two-term rule would give zero. **Transfer:** Derive derivative-like formulas in their actual algebra instead of importing calculus.

### Problem 30. Quantify and verify containment bounds

**Statement.** Eliminate x universally and existentially from majority f=xy+xz+yz. **Origin:** CMU quantification pattern.

**Solution.** The zero cofactor is yz; the one cofactor is y+z. Their AND is yz(y+z)=yz, and their OR is yz+y+z=y+z by absorption. Hence ∀x f=yz and ∃x f=y+z. If both other votes are one, every choice of x produces a majority. If at least one is one, some choice does. If both are zero, neither choice does. These cases also establish yz≤f≤y+z. **Transfer:** Quantification retains the other inputs as variables; it is not a single Boolean answer until they too are specified or eliminated.

### Problem 31. Prove that mixed quantifiers can disagree

**Statement.** Evaluate ∀x∃y E and ∃y∀x E for E=xy+x′y′. **Origin:** Original quantifier-order example.

**Solution.** E means x and y are equal. For each fixed x there exists a matching y, so existentially eliminating y gives x+x′=1; universally eliminating x leaves one. For each fixed y, however, one value of x differs from it, so universally eliminating x gives yy′=0; existentially eliminating y leaves zero. The first statement allows the choice of y to depend on x, while the second requires one y to work for both x values. **Transfer:** Quantifier order determines which choices may depend on earlier ones.

### Problem 32. Classify semantic unateness

**Statement.** Classify x in each of xy, x′y, xy+x′y, and x⊕y. **Origin:** CMU unateness pattern, corrected semantic interpretation.

**Solution.** For xy the cofactors are zero and y; zero is contained in y, so x is positive unate and essential. For x′y they are y and zero, giving negative unateness. For xy+x′y they are both y, so x is irrelevant and satisfies both directions. For XOR they are y and y′. At y=0 the output rises when x rises; at y=1 it falls. Neither cofactor contains the other, so x is binate. **Transfer:** Both literal polarities in a representation do not prove binateness of the represented function.

### Problem 33. Use the unate-cover tautology criterion

**Statement.** Is H=xy+xz′+yz′ a tautology? Prove a general criterion for a syntactically unate SOP. **Origin:** CMU recursive-tautology pattern.

**Solution.** Set x=0,y=0,z=1, which falsifies every used literal polarity. Each product becomes zero, so H is not a tautology. In general, if each input occurs in at most one polarity and every term contains at least one literal, choose all inputs to falsify their used polarities. Every term then vanishes. If an empty product, namely constant one, is included, the OR is always one. Thus such a cover is a tautology exactly when it contains a constant-one term. **Transfer:** This criterion applies to a unate cover, not an arbitrary expression with redundant opposite polarities.

### Problem 34. Find an equivalence counterexample

**Statement.** Compare f=x+y and g=x⊕y by a miter. **Origin:** Original verification example.

**Solution.** Their outputs agree at 00,01,10 and differ at 11. Algebraically, OR is x⊕y⊕xy, so M=f⊕g=xy after XOR cancellation. The miter has precisely the satisfying assignment 11. This proves nonequivalence and explains its cause: inclusive OR retains the both-one case, whereas XOR removes it. Restricting to inputs with xy=0 would establish conditional equivalence, but would not make the fully specified functions equal. **Transfer:** Give the mismatch assignment as part of a refutation.

### Problem 35. Compare functions under a care set

**Statement.** Compare f=x+y and g=x⊕y when row 11 is unconstrained. Count valid completions of the remaining scalar table. **Origin:** MIT don't-care-specification pattern.

**Solution.** The care function is C=(xy)′. The mismatch miter is xy, hence CM=(xy)′xy=0. Both functions agree on every care row and differ only on the unconstrained row. The three fixed outputs are 0,1,1; the fourth may be zero or one, giving two completions. If row 11 were fixed to one, only OR would meet the specification; if fixed to zero, only XOR would. **Transfer:** The freedom comes from the specification, rather than from an algebraic third value.

### Problem 36. Derive a primary-input stuck-at test

**Statement.** For f=xy+x′z, find all three-input patterns detecting x stuck at zero. **Origin:** CMU sensitivity-to-testing pattern, new function.

**Solution.** Fault excitation requires healthy x=1. The sensitivity condition is D<sub>x</sub>f=y⊕z=1. Thus y,z must be 01 or 10, giving patterns 101 and 110. At 101 the healthy output is y=0 while the faulty output is z=1. At 110 the healthy output is one and the faulty output zero. With equal y,z, the fault is masked despite being excited. **Transfer:** Detection requires both the wrong constant to matter and a healthy assignment that disagrees with it.

### Problem 37. Prove a tautology recursively

**Statement.** Prove H=xy+xz+xy′z′+x′ is a tautology by restrictions. **Origin:** CMU tautology-checking example pattern.

**Solution.** Restrict x=0: the x′ term becomes one, so H₀=1. Restrict x=1: H₁=y+z+y′z′. If y=1, that expression is one. If y=0, it becomes z+z′=1. Both y cofactors of H₁ are therefore one, so H₁ is a tautology, and both x cofactors of H are tautologies. Shannon then proves H=1. Algebraically, y+z+(y+z)′=1 gives the same result. **Transfer:** A tautology requires every branch to succeed; finding one true leaf is insufficient.

### Problem 38. Recover a grouped-input representation

**Statement.** Suppose the positive-p and positive-q cofactors of f(p,q,u) are equal as functions on the common remaining domain. Show that f=(p+q)g(u)+p′q′h(u) for some g,h. **Origin:** CMU Homework 1, item 4 structural pattern.

**Solution.** Equality means f(1,q,u)=f(p,1,u) for every p,q,u. Fix p=q=1 to name the shared value g(u)=f(1,1,u). Taking p=0,q=1 forces f(0,1,u)=g(u); taking p=1,q=0 forces f(1,0,u)=g(u). Thus all three input pairs other than 00 share g. Define h(u)=f(0,0,u). The proposed expression selects h only at 00 and g at 01,10,11, proving existence. Conversely, that expression has both positive cofactors equal to g, proving the reverse implication. **Transfer:** Cofactor equality can impose a grouping of input assignments, rather than merely eliminate an input.

### Problem 39. Simplify the complement of a positive-unate function

**Statement.** If f is positive unate in x, derive f′=f₁′+x′f₀′. **Origin:** CMU Homework 1, item 5 pattern.

**Solution.** Positive unateness means f₀≤f₁, so complement reverses the containment: f₁′≤f₀′. Shannon applied to f′ gives x′f₀′+xf₁′. Replace the second product using the covered term f₁′: f₁′=xf₁′+x′f₁′, and x′f₁′ is absorbed into x′f₀′. Therefore adding it changes nothing, and the result is x′f₀′+f₁′. Check x=1 to obtain f₁′; check x=0 to obtain f₀′+f₁′=f₀′. **Transfer:** A containment relation between cofactors can remove a selector literal, but only in the justified direction.

### Problem 40. Check multiple outputs without cancelling errors

**Statement.** One two-output block always returns (0,0), while another always returns (1,1). Why is an XOR of discrepancy bits an invalid equivalence check? **Origin:** Original verification-model boundary.

**Solution.** Each corresponding output XOR is one. XORing those two discrepancies gives zero, falsely suggesting equivalence. Their OR is one, correctly indicating that at least one output differs. Generally define M=(f₁⊕g₁)+⋯+(fₖ⊕gₖ). This miter is zero on an assignment exactly when every corresponding output matches, and identically zero exactly when the vector functions are equal. With zero output coordinates, the empty OR is zero and equality is vacuous. **Transfer:** Error aggregation must mean "any error," not parity of errors.
