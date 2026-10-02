The following problems are grouped by method, not by increasing intimidation. Read each solution as a short lesson: identify the object and hypotheses, carry out the argument, then inspect the stated trap. **Original** means authored for this chapter. **Course-derived** identifies the source of the mathematical exercise pattern; instances and explanations are independently written. None is a request to test the student before reading.

### Problem 1. A carrier changes a verdict

**Original; method: inspect the declared type.** Let $R={(1,u),(2,u)}$. Compare the relation from ${1,2}$ to ${u,v}$ with the relation from ${1,2,3}$ to ${u,v}$. Is either a total function or a surjection?

**Solution.** Each listed first coordinate has exactly one output, so both relations are right-unique. The first carrier has no unused input, making its relation a total function. The second leaves 3 without an output, making its relation only a partial function. Both have range ${u}$, so neither is surjective onto ${u,v}$. Reducing the target carrier to ${u}$ would change the surjectivity verdict. The pair set alone does not settle properties that quantify over carriers.

### Problem 2. Counting typed relations and functions

**Course-derived: Cambridge, exercise 3; extended counting.** For a three-element source and a two-element target, count all relations, left-total relations, partial functions, and total functions. Also count ternary relations on carriers of sizes 2, 3, and 4.

**Solution.** There are six binary pair positions, giving $2⁶=64$ relations. Each of three rows may choose any of three nonempty target subsets, giving $3³=27$ left-total relations. A partial-function row has three choices, namely no output or either target, so there are also 27 partial functions. These equal numerical counts represent different families. A total-function row has two choices, giving $2³=8$. A ternary relation is a subset of a Cartesian product with $2·3·4=24$ triples, giving $2²⁴$ possibilities. Being ternary does not force one output per input pair.

### Problem 3. Why relational images lose intersections

**Original; method: distinguish witnesses.** Let $R={(a,z),(b,z)}$, $X={a}$, and $Y={b}$. Compute the images needed to test intersection preservation. Test inverse-image preservation too.

**Solution.** Both $R[X]$ and $R[Y]$ equal ${z}$, but $X∩Y$ is empty and its image is empty. Thus the relational-image inclusion can be strict. For inverse images, choose $T={(p,u),(p,v)}$ and disjoint target sets ${u},{v}$. Each inverse image is ${p}$, whereas the inverse image of the empty intersection is empty. A function's inverse image avoids this failure because one input cannot witness two different target values. Relations have no such uniqueness condition.

### Problem 4. Compose through a common middle carrier

**Course-derived: Cambridge, exercise 1.** Let $A={1,2,3}$, $B={u,v,w}$, $C={x,y}$, $R={(1,u),(1,v),(2,w),(3,v)}$, and $S={(u,x),(v,x),(v,y)}$. Compute $S∘R$ and its Boolean matrix.

**Solution.** From input 1, the middle objects $u,v$ reach $x$, and $v$ also reaches $y$. Input 2 reaches only $w$, which has no outgoing $S$ edge, so it contributes no pair. Input 3 reaches $v$ and therefore reaches both targets. The result is ${ (1,x),(1,y),(3,x),(3,y) }$. In the stated row and column orders, the output matrix rows are $(1,1)$, $(0,0)$, $(1,1)$. Two middle witnesses for $(1,x)$ still produce one relation pair; Boolean disjunction does not count them twice.

### Problem 5. Composition is not commutative

**Original; method: find an endpoint pair.** On ${a,b,c}$ let $R={(a,b)}$ and $S={(b,c)}$. Compare the two compositions.

**Solution.** Following $R$ then $S$ gives the single chain $a→b→c$, so $S∘R={(a,c)}$. Following $S$ first reaches $c$, where no $R$ edge starts, so $R∘S$ is empty. Both compositions are well-typed, yet unequal. Associativity concerns grouping three steps; it says nothing about exchanging two steps.

### Problem 6. Composition does not distribute over intersection

**Original; method: compare shared and separate witnesses.** From ${a}$ to ${b,c}$ take $R={(a,b)}$ and $T={(a,c)}$. From ${b,c}$ to ${z}$ take $S={(b,z),(c,z)}$. Compare $S∘(R∩T)$ with $(S∘R)∩(S∘T)$.

**Solution.** The input intersection is empty because the two edges differ, so its composition is empty. Each separate composition contains $(a,z)$, one through $b$ and the other through $c$. Their intersection therefore contains that pair. The right side permits different middle witnesses; the left side requires a middle edge in both input relations. The analogous inclusion always holds, but equality requires additional conditions.

### Problem 7. Converse identities by pair membership

**Course-derived: Cambridge, exercise 5.** Prove that converse preserves intersection and union and reverses composition.

**Solution.** A pair $(b,a)$ is in $(R∩S)^{−1}$ exactly when $(a,b)$ belongs to both $R$ and $S$. This is exactly membership in $R^{−1}∩S^{−1}$. Replace “both” by “at least one” to obtain the union identity. For composition, $(c,a)$ belongs to $(S∘R)^{−1}$ precisely when some $b$ satisfies $aRbSc$. Reversing the two edges gives $cS^{−1}bR^{−1}a$, which is membership in $R^{−1}∘S^{−1}$. The order reversal is compelled by the witness chain, not by a memorized typographic rule.

### Problem 8. Classify a finite relation with repeated vertices

**Course-derived: Cambridge, exercise 2.** On ${a,b,c}$ let $R={(a,a),(a,b),(b,a),(c,c)}$. Determine all seven properties in the definition table.

**Solution.** Reflexivity fails because $(b,b)$ is missing; irreflexivity fails because $(a,a)$ exists. Symmetry holds because the only off-diagonal pair has its reverse. Antisymmetry and asymmetry both fail on the distinct pair $a,b$. Transitivity fails because $bRaRb$ would require $bRb$, which is absent. Seriality holds: $a$ reaches itself or $b$, $b$ reaches $a$, and $c$ reaches itself. Inspecting only three distinct vertices would have missed the transitivity failure.

### Problem 9. A vacuous property is still a property

**Original; method: inspect an implication's antecedent.** On ${a,b,c}$ classify $R={(a,b)}$, and compare it with the empty relation on the same carrier.

**Solution.** The one-edge relation is irreflexive, antisymmetric, and asymmetric. It is transitive because its only target, $b$, has no outgoing edge, so no two-edge chain exists. It is not symmetric, reflexive, or serial. The empty relation is additionally symmetric, since no edge can violate the implication. Both remain nonreflexive on this nonempty carrier. If the carrier is empty instead, reflexivity and seriality become vacuously true as well; statements must specify the carrier.

### Problem 10. A parity relation with a complete proof

**Course-derived: Stanford, Binary Relations I.** On the integers define $aRb$ when $a+b$ is even. Prove equivalence and determine the classes.

**Solution.** For any integer $a$, $a+a=2a$, so reflexivity holds. If $a+b$ is even, commutativity makes $b+a$ even, proving symmetry. If $a+b=2r$ and $b+c=2s$, subtract $2b$ from their sum to obtain $a+c=2(r+s−b)$, proving transitivity. The integers $r+s−b$ remain integers, which matters to the definition of evenness. Two numbers have an even sum exactly when their parities agree, so the classes are the even integers and the odd integers. Symmetry alone would not have justified the final claim of equivalence.

### Problem 11. Locate the hidden assumption in a false proof

**Course-derived: Stanford, Problem Set 3, Problem Two.** A proposed proof chooses arbitrary $aRb$, reverses it by symmetry, and obtains $aRa$ by transitivity. It concludes that every symmetric transitive relation is reflexive. Explain the defect and repair the statement.

**Solution.** The argument proves a loop only for elements with an outgoing edge. An isolated element may offer no $b$ to choose. The empty relation on a singleton is a counterexample: symmetry and transitivity hold but its loop is absent. Adding seriality guarantees a witness for every element and makes the argument valid. Alternatively, restrict the carrier to the active domain; the resulting partial equivalence relation becomes an equivalence relation. Choosing arbitrary elements under extra hypotheses cannot establish a claim about all elements without those hypotheses.

### Problem 12. Cyclicity and right-Euclideanity

**Course-derived: Stanford, Binary Relations II and Problem Set 3, Problem Three.** Give complete arguments that reflexivity plus either alternative property characterizes equivalence. Give a right-Euclidean relation that is not symmetric.

**Solution.** For cyclicity, $aRa$ and $aRb$ imply $bRa$, so symmetry follows. Then $aRbRc$ implies $cRa$ by cyclicity and $aRc$ by symmetry. Conversely, transitivity gives $aRc$ and symmetry reverses it, proving cyclicity of an equivalence relation. For right-Euclideanity, the pair of hypotheses $aRb$ and $aRa$ gives $bRa$. Given $aRbRc$, use $bRa$ and $bRc$ with common source $b$ to obtain $aRc$. Conversely, $aRb$ and $aRc$ give $bRaRc$ by symmetry, hence $bRc$ by transitivity. On ${a,b}$, $R={(a,b),(b,b)}$ is right-Euclidean: every source's outgoing set is ${b}$, and $bRb$ exists. It is not symmetric because $(b,a)$ is missing. Reflexivity was essential to the characterization.

### Problem 13. Seriality does not create a strict order

**Course-derived: Oxford, exercise 4.5; extended distinction.** Construct a finite relation that is irreflexive, antisymmetric, and serial. Explain why no finite nonempty strict partial order is serial.

**Solution.** On ${a,b,c}$ take the directed cycle $a→b→c→a$. No loops or reverse pairs occur, and every vertex has an outgoing edge, so all requested properties hold. It is not transitive: $aRbRc$ lacks $aRc$. A finite nonempty strict partial order has a maximal element by applying the minimal-element argument to its dual. That maximal element has no outgoing strict comparison, contradicting seriality. The construction is possible only because transitivity was not one of the requested conditions.

### Problem 14. A rational equivalence with a nonstandard description

**Course-derived: Stanford, Problem Set 3, Problem One.** Let $H$ be the rationals having some representation with odd nonzero denominator. On the real numbers define $x∼y$ when $y−x∈H$. Prove equivalence and identify $[0]$.

**Solution.** Zero has denominator 1. If $p/q∈H$, its negative has the same odd denominator. Adding $p/q$ and $r/s$ produces $(ps+rq)/(qs)$, whose denominator is odd, so $H$ is closed under addition and subtraction. These facts prove reflexivity, symmetry, and transitivity of the difference relation. The class of zero is exactly $H$ by substituting zero into the definition, and every class is a translate $x+H$. The number $3/2$ is not in $H$: if it equalled $p/q$ with odd $q$, cross multiplication would make the odd integer $3q$ equal to the even integer $2p$. The word “odd” describes the existence of an odd-denominator representation, not the parity of an arbitrary unreduced denominator.

### Problem 15. Count properties on four labelled elements

**Course-derived: Oxford, §4.6.** Compute the counts of reflexive, symmetric, antisymmetric, asymmetric, and reflexive symmetric relations on four elements. Count relations that are both symmetric and antisymmetric.

**Solution.** There are four diagonals and six unordered distinct pairs. Reflexive relations have 12 free off-diagonal entries, giving $2¹²=4096$. Symmetric relations have ten binary choices, giving $2¹⁰=1024$. Antisymmetric relations have four binary diagonal choices and six ternary pair choices, giving $2⁴3⁶=11664$. Asymmetric relations fix the diagonal and leave the ternary choices, giving $3⁶=729$. Reflexive symmetric relations give $2⁶=64$. A symmetric antisymmetric relation can contain only loops, so there are $2⁴=16$. None of these counts silently includes transitivity.

### Problem 16. Exact powers of a cycle

**Course-derived: Oxford, exercise 4.6; changed instance.** On ${a,b,c}$ take $R={(a,b),(b,c),(c,a)}$. Compute $R²$, $R³$, $R∘R^{−1}$, $R⁺$, and $R⁎$.

**Solution.** Two steps give $(a,c),(b,a),(c,b)$, while three steps return to the starting vertex, so $R³=I_A$. The converse moves one step backwards; following it and then $R$ gives exactly the identity. All vertex pairs are reachable in one, two, or three positive steps, so $R⁺=A×A$, and adding zero-length paths changes nothing. The powers are periodic rather than increasing. Truncating the positive closure after $R²$ would omit every loop.

### Problem 17. A tight finite closure bound

**Course-derived: Cambridge, exercise 6.** Why does a directed $n$-cycle require the $Rⁿ$ term for positive closure, while a directed $n$-vertex chain does not?

**Solution.** In the cycle, returning to the starting vertex in positive length first occurs after $n$ edges. Earlier powers therefore miss its diagonal pair. In a chain, every positive path moves strictly forward and uses at most $n−1$ edges; no cycle creates a diagonal pair. Both examples obey the general $n$ bound, but the cycle shows it cannot be uniformly reduced for $R⁺$. For $R⁎$, identity supplies all diagonal pairs, and the remaining distinct-endpoint paths need at most $n−1$ edges.

### Problem 18. Trace Warshall through a cycle

**Original; method: pivot invariant.** Start on ${a,b,c,d}$ with $R={(a,b),(b,c),(c,a)}$, leaving $d$ isolated. Process pivots in alphabetical order and list the newly added pairs at each stage.

**Solution.** With internal vertex $a$ allowed, $c→a→b$ adds $(c,b)$. Allowing $b$ uses incoming edges from $a,c$ and the outgoing edge to $c$, adding $(a,c)$ and $(c,c)$. Allowing $c$ then makes every ordered pair among $a,b,c$ reachable; the new pairs are $(a,a),(b,a),(b,b)$. No edge involving $d$ can be formed, so the final pivot adds nothing. Positive closure is the full square of ${a,b,c}$, with nine pairs. Reflexive transitive closure additionally has $(d,d)$, giving ten. A zero-length convention should be stated before interpreting a diagonal entry.

### Problem 19. A single pass with the wrong loop order fails

**Original; method: refute an algorithmic shortcut.** Consider the loop order $i,j,k$ with all indices increasing and one pass over each entry. Use vertices numbered 0 through 3 and edges $0→2$, $2→3$, $3→1$ to show failure.

**Solution.** When row 0, column 1 is processed, no middle index yet witnesses reachability: row 0 lacks an edge to 3, and row 2 does not yet contain reachability to 1. Later, processing row 0, column 3 adds $0→3$ through 2. Later still, processing row 2, column 1 adds $2→1$ through 3. But the already processed entry $(0,1)$ is not revisited, so the positive path $0→2→3→1$ is missed. Warshall's outer-pivot order revisits all endpoint entries whenever a new internal vertex is permitted and avoids this defect.

### Problem 20. The order of closures matters

**Course-derived: Cambridge, exercises 9–10.** On ${a,b,c}$ use $R={(a,b),(a,c)}$ to compare $s(t(R))$ and $t(s(R))$. Then determine its equivalence closure.

**Solution.** No edge starts at $b$ or $c$, so $t(R)=R$. Symmetrizing gives four edges, from $a$ to each other vertex and back. It lacks $(b,c)$ and all loops. Symmetrizing first permits paths between every pair and positive closed paths at every vertex, so $t(s(R))=A×A$. The equivalence closure is therefore also $A×A$. For an isolated fourth vertex, positive closure of the symmetrized relation would still omit that vertex's loop; reflexive closure would be required to complete the equivalence relation.

### Problem 21. When can a partial-order extension exist?

**Course-derived: Cambridge, exercise 10; full criterion.** Determine exactly when a relation on a finite carrier has a partial-order superset on that same carrier, and describe the least such superset.

**Solution.** A directed cycle involving at least two distinct vertices is impossible in any partial-order extension: transitivity gives comparisons in both directions between distinct vertices, contradicting antisymmetry. If no such cycle exists, take $R⁎$. It is reflexive and transitive by construction. Two opposite positive paths between distinct vertices would create a prohibited cycle, so it is antisymmetric. Thus $R⁎$ is a partial order. Every partial-order superset contains the identity and every finite input path, so it contains $R⁎$, proving leastness. Original self-loops are allowed. The criterion distinguishes harmless reflexive loops from nontrivial directed cycles.

### Problem 22. Closure of prime-multiple steps

**Course-derived: Cambridge, exercises 8–10.** On positive integers let $aRb$ when $b=pa$ for a prime $p$. Describe the positive and reflexive transitive closures and its equivalence closure.

**Solution.** A positive path multiplies by one or more primes, so its endpoint ratio is an integer at least 2. Conversely, every such ratio factors into primes, supplying a path. Thus $R⁺$ is proper divisibility on positive integers, and $R⁎$ is divisibility including equality. After reversing edges as well, every integer is connected to 1 by successively deleting its prime factors. Hence the equivalence closure has a single class, all positive integers. Positivity excludes complications involving zero and signs; a different carrier would require a fresh argument.

### Problem 23. Equivalence intersection and union

**Course-derived: Cambridge, exercise 7.** On ${a,b,c}$ let $E$ have blocks ${a,b},{c}$ and $F$ have blocks ${a},{b,c}$. Compute their intersection and the equivalence closure of their union.

**Solution.** Both relations contain every loop. Their only off-diagonal pairs are respectively the two directions between $a,b$ and between $b,c$, so the intersection is $I_A$. The union has a path $a→b→c$ but omits $(a,c)$, proving it is not itself transitive. Positive closure connects all three vertices in both directions and keeps the existing loops, yielding $A×A$. Intersection refines the partitions to singleton blocks; closing the union merges them to one block.

### Problem 24. Classes, quotient objects, and pair counts

**Original; method: recover a relation from blocks.** A six-element carrier is partitioned into blocks ${a,b,c},{d,e},{f}$. Write the quotient and count the relation's pairs. Is $[a]$ the same kind of object as $a$?

**Solution.** The quotient is the three-element set whose elements are the three displayed blocks. Inside each block every ordered pair is present, including loops, while no cross-block pair exists. The pair count is $3²+2²+1²=14$. The class $[a]$ equals ${a,b,c}$ and is also $[b]$ and $[c]$; it is a set, whereas the original symbol $a$ denotes one carrier element. Counting different representative names would incorrectly produce six quotient elements.

### Problem 25. Count equivalence relations into exactly two classes

**Course-derived: Oxford, partition-counting pattern; extended derivation.** On five labelled elements, count equivalence relations with exactly two classes and all equivalence relations.

**Solution.** Choose a nonempty proper subset as one block. There are $2⁵−2=30$ choices, but each partition is counted twice because either block could be chosen first. Therefore there are 15 two-block partitions. The Stirling recurrence gives the row for five elements as $1,15,25,10,1$ for one through five blocks, summing to $B₅=52$. The two-block count is not the total count. Labelling the two blocks would restore the factor of two and instead count onto functions to a labelled two-element target.

### Problem 26. Quotient maps need representative independence

**Course-derived: Cornell, Lecture 7.** Modulo 6, decide whether the formulas $ḡ([a])=$ parity of $a$, $h̄([a])=a²$, and $k̄([a])=[a²]$ define maps. The middle map targets the integers; the last targets classes modulo 6.

**Solution.** Equivalent integers differ by a multiple of 6 and hence have equal parity, so the first map is well-defined. The second fails: 1 and 7 represent the same class but their squared integers are 1 and 49. For the third, if $a−b=6t$, then $a²−b²=(a−b)(a+b)$ is divisible by 6. The squared outputs therefore define the same class, so the last map is well-defined. The target's equality notion determines whether output equality means integer equality or quotient-class equality.

### Problem 27. Fractions, zero denominators, and a binary operation

**Original; method: track cancellation and both representatives.** Explain why allowing denominator zero breaks the cross-product equivalence, and prove addition is well-defined for positive-denominator fraction classes.

**Solution.** With zero denominators allowed, $(1,1)$ relates to $(0,0)$ and $(0,0)$ relates to $(2,1)$ because both cross-products are zero. But $(1,1)$ does not relate to $(2,1)$, so transitivity fails. For valid denominators, let $(p,q)∼(p′,q′)$ and $(r,s)∼(r′,s′)$. Then $pq′=p′q$ and $rs′=r′s$. Addition produces $(ps+rq,qs)$. Cross multiplication with the primed result gives $(ps+rq)q′s′=psq′s′+rqq′s′$. Substitute the two assumed identities to obtain $(p′s′+r′q′)qs$. The outputs are equivalent, and both output denominators are positive. Checking only one representative would leave half of the well-definedness obligation unproved.

### Problem 28. Collapse a preorder into a partial order

**Course-derived: Oxford, preorder example; original quotient extension.** On subsets of ${1,2,3}$ let $X P Y$ mean $|X|≤|Y|$. Describe the preorder quotient and its order.

**Solution.** Cardinality comparison is reflexive and transitive. It is not antisymmetric: ${1}$ and ${2}$ compare both ways but differ. Mutual comparison means equal cardinality, producing four classes, sizes 0, 1, 2, and 3. The quotient order compares these sizes numerically and is the four-element chain. It is well-defined because replacing a subset by another of the same size does not change an inequality. This quotient keeps the information the preorder can distinguish and removes the information it cannot.

### Problem 29. Strong components and one-way reachability

**Original; method: distinguish two closures.** With edges $a→b$, $b→a$, $b→c$, and $c→d$, find mutual-reachability classes and their quotient order. Contrast the equivalence closure of the original edge relation.

**Solution.** The strongly connected components are ${a,b}$, ${c}$, and ${d}$. Reachability orders them as a three-element chain, with the first preceding both later components. Neither $c$ nor $d$ can reach the first component. Ignoring edge directions instead connects all four vertices, so the equivalence closure has just one class. Directed mutual reachability preserves separate components that undirected connectivity merges. A raw directed edge relation need not be reflexive or transitive, so it is not itself this component order.

### Problem 30. Strictness from a definition of integer order

**Course-derived: Stanford, Problem Set 3, checkpoint and Problem Four.** Define $a≺b$ when $b=a+k$ for a positive integer $k$. Prove it is a strict partial order, without assuming the usual order laws as the proof.

**Solution.** A self-comparison would give $a=a+k$ with positive $k$, forcing $k=0$, a contradiction. For two comparisons, write $b=a+k$ and $c=b+l$ with positive integers $k,l$. Substitution gives $c=a+(k+l)$, and the sum is positive, proving transitivity. Irreflexivity plus transitivity implies asymmetry by the general theorem, so the relation is a strict order. The proof does not presume transitivity of the symbol it is defining; it derives it from positive-integer addition.

### Problem 31. Product and lexicographic comparisons

**Course-derived: Oxford, §8.2 and exercise 8.2.** Compare $(1,5)$ and $(2,4)$ under the two orders on $ℕ²$. Then compare $(2,4)$ and $(2,7)$.

**Solution.** In the product order, the first pair moves upward in its first coordinate and downward in its second, so neither tuple is below the other. In the lexicographic order, the first coordinate 1 is smaller than 2 and immediately settles the comparison: $(1,5)$ is smaller. For equal first coordinates 2, the second coordinates 4 and 7 decide both product and lexicographic comparison, so $(2,4)$ lies below $(2,7)$ in both. Priority and componentwise dominance are distinct definitions, not two drawings of one order.

### Problem 32. A Hasse diagram is a cover graph

**Course-derived: Stanford, Problem Set 3, Problem Five.** Determine the cover relations for natural-number order and power-set inclusion. Explain why the cover relation itself need not be transitive.

**Solution.** Under the usual natural-number order, $b$ covers $a$ exactly when $b=a+1$. A larger gap has an intermediate natural number; a gap of one has none. Under inclusion, $Y$ covers $X$ exactly when $X⊂Y$ and $|Y∖X|=1$. Two or more new elements allow an intermediate set; exactly one allows no intermediate. The cover relation on numbers includes $0⋖1$ and $1⋖2$ but not $0⋖2$, so it is not transitive. Transitivity is recovered by closure, not by the raw cover edges.

### Problem 33. Recover divisibility order and its extrema

**Original; method: inspect covers and upward paths.** For divisors of 12, list covers, maximal and minimal elements, height, width, a minimum antichain partition, and a minimum chain partition.

**Solution.** The carrier is ${1,2,3,4,6,12}$. Covers are $1⋖2$, $1⋖3$, $2⋖4$, $2⋖6$, $3⋖6$, $4⋖12$, and $6⋖12$. All other strict divisibility pairs are recovered by upward paths. The unique minimal and least element is 1; the unique maximal and greatest is 12. A longest chain is $1,2,4,12$, so height is 4. The layers ${1},{2,3},{4,6},{12}$ partition into four antichains, proving the minimum antichain count. The two chains ${1,2,4,12}$ and ${3,6}$ partition the carrier, so width is at most 2; the incomparable pair ${2,3}$ attains 2. Thus this is also a minimum two-chain partition.

### Problem 34. Unique minimal need not mean least

**Original; method: identify the finite hypothesis.** Prove the finite implication and give an infinite counterexample.

**Solution.** In a finite nonempty poset, begin at any element $x$ and move downward while possible. Termination gives a minimal element $m≼x$. If the poset has only one minimal element, every such descent ends there, so that element lies below every $x$ and is least. For the infinite counterexample, take a disjoint union of the integers and a new element $p$. Retain the usual integer order and compare $p$ only with itself. Every integer has a smaller integer, so none is minimal; $p$ is the unique minimal element. But $p$ is incomparable with every integer and is not least. Finiteness supplied the termination step that fails here.

### Problem 35. Bounds are ambient objects

**Course-derived: Oxford, exercise 8.4; changed instance.** In positive integers ordered by divisibility, find the upper-bound set, lower-bound set, supremum, and infimum of ${8,12}$. Is either bound a maximum or minimum of that subset?

**Solution.** An upper bound must be divisible by both numbers, so the upper bounds are the positive multiples of 24. The number 24 divides each such bound and itself bounds both inputs, making it their supremum. A lower bound divides both inputs, so the lower bounds are ${1,2,4}$, with greatest member 4 in divisibility order. Neither 24 nor 4 belongs to ${8,12}$; neither input divides the other, so the subset has no maximum or minimum. Numerically larger is not the definition of larger in this poset, although lcm and gcd here align with numerical extremality among the relevant bounds.

### Problem 36. Several minimal upper bounds, no supremum

**Course-derived: Oxford, exercise 8.5; fully specified instance.** Let the carrier contain all subsets of ${1,2,3,4}$ except the two-element subsets, ordered by inclusion. Find the upper bounds of ${ {1},{2} }$ and determine whether a supremum exists.

**Solution.** Any upper bound must contain both 1 and 2, but ${1,2}$ is missing. The upper bounds in the carrier are ${1,2,3}$, ${1,2,4}$, and ${1,2,3,4}$. The first two are incomparable minimal upper bounds. No upper bound lies below both, so no supremum exists. The carrier has a greatest element, yet it is not a lattice. Having a maximum for the whole carrier does not supply least upper bounds for every pair.

### Problem 37. A supremum in one carrier and none in another

**Course-derived: Oxford, §8.5.** For $S={q∈ℚ:0<q and q²<2}$, explain why the real supremum is $√2$ and no rational supremum exists.

**Solution.** Every member is less than $√2$, making it an upper bound in the reals. For any real $a<√2$, choose a rational between $max(a,0)$ and $√2$; it belongs to $S$ and exceeds $a$, so $a$ is not an upper bound. The needed density fact follows from the Archimedean property: for $u<v$, choose positive integer $n$ with $n(v−u)>1$ and integer $k=⌊nu⌋+1$; then $u<k/n<v$. Thus $√2$ is the real supremum. A rational upper bound $m$ cannot equal the irrational $√2$ and must be larger. Density supplies a rational $m′$ strictly between them. That smaller rational is still an upper bound, disproving leastness of $m$. The proof checks membership in the ambient carrier instead of treating a real limit as automatically rational.

### Problem 38. Supremum without a maximum in lexicographic order

**Course-derived: Oxford, exercise 8.6.** In lexicographically ordered $ℕ²$, find the supremum of $S={(0,n):n∈ℕ}$ and decide whether it has a maximum.

**Solution.** Every member has a larger member $(0,n+1)$, so no maximum exists. An upper bound cannot have first coordinate 0, because any fixed second coordinate is exceeded. Every pair whose first coordinate is at least 1 is an upper bound. The least of those in lexicographic order is $(1,0)$, so it is the supremum. This answer depends on zero belonging to the natural numbers; using positive naturals in the second coordinate would change its least value.

### Problem 39. Empty sets and lattice completeness

**Original; method: apply universal quantification correctly.** Determine the supremum and infimum of the empty subset in the power-set lattice of a finite set $U$. Explain why ordinary real order is not a complete lattice.

**Solution.** Every subset of $U$ is both an upper and lower bound of the empty family. The least upper bound is therefore the least element, the empty set. The greatest lower bound is the greatest element, $U$. In ordinary real order the empty set has no supremum because there is no least real number; the whole real carrier also has no real upper bound. Either failure disproves complete-lattice completeness. The theorem that bounded nonempty real subsets have suprema is a different and weaker condition.

### Problem 40. An order-preserving bijection can fail to be an isomorphism

**Course-derived: Oxford, §8.6; original counterexample.** Compare the identity map from a two-element antichain to a two-element chain. Then exhibit a genuine divisor/power-set isomorphism.

**Solution.** The identity map preserves every source comparison because those comparisons are only equalities. It is bijective, but the chain has a strict comparison that the source does not, so it fails order reflection and is not an isomorphism. For divisors of 30, map a divisor to the subset of ${2,3,5}$ consisting of its prime factors. The map is bijective because 30 is squarefree, and one divisor divides another exactly when its factor set is included. Both directions hold, so this map is an order isomorphism. Cardinality and forward monotonicity alone would not prove that.

### Problem 41. Unit-time scheduling with a sharp lower bound

**Course-derived: MIT, §§7.7–7.9; original task graph.** Six unit tasks have dependencies $A≺C$, $A≺D$, $B≺D$, $C≺E$, $D≺E$, and $D≺F$. Give a linear extension and an optimal unlimited-processor schedule. Explain the effect of one processor.

**Solution.** One legal listing is $A,B,C,D,E,F$; each dependency points forward. Levels are ${A,B}$, then ${C,D}$, then ${E,F}$. Each level consists of mutually independent tasks, and every input of a task finishes in an earlier level. A chain such as $A,C,E$ requires three slots, so the three-level schedule is optimal with unlimited processors. With one processor, six unit tasks require six slots, attained by the linear extension. Height remains a lower bound, but processor capacity prevents attaining it. The graph states precedence, not simultaneous resource availability.

### Problem 42. Chain–antichain bounds and subsequences

**Course-derived: MIT, §7.9.** Show that any poset with 25 elements has a chain or an antichain of size at least 5. Apply the reasoning to increasing and decreasing subsequences of a sequence of 25 distinct numbers.

**Solution.** If both height and width were at most 4, the level partition would have at most four antichains of at most four elements, hence at most 16 elements, a contradiction. More generally $25≤hw$ makes at least one of $h,w$ at least 5. For the sequence, put an order on positions: $i≼j$ when $i=j$, or when $i<j$ and the value at $i$ is smaller than the value at $j$. Reflexivity, antisymmetry, and transitivity hold. A chain, read in position order, is an increasing subsequence. An antichain, read in position order, is decreasing because values are distinct and an increasing pair would be comparable. Thus one of the two subsequence types has length at least 5. Distinctness is essential to this strict formulation.

### Problem 43. Use matching to certify a minimum chain partition

**Original; method: construct matching and antichain certificates.** For the six-task poset of Problem 41, use comparisons $A≺C$, $C≺E$, and $B≺D$ as matching links. Find a chain partition and prove it is minimum.

**Solution.** On left/right copies, the links are $A_LC_R$, $C_LE_R$, and $B_LD_R$. Their left endpoints are distinct and right endpoints are distinct, so they are a matching even though the original vertex $C$ appears on both sides. They produce chains ${A,C,E}$, ${B,D}$, and ${F}$, giving three chains. This is a valid partition but it is not minimum. Add the fourth link $D_LF_R$, whose left and right copies are both unused in the matching. The new partition is ${A,C,E}$ and ${B,D,F}$. The incomparable pair ${C,D}$ forces every chain partition to use at least two chains, so the displayed two-chain partition is minimum and the width is 2. An arbitrary matching establishes a feasible partition; maximum size requires an optimality argument such as this antichain certificate.

### Problem 44. Well-foundedness and a recursive descent

**Course-derived: Cambridge, pp. 40–42; original compact recursion.** On $ℕ²$, order argument pairs lexicographically. A recursive procedure on $(m,n)$ may call $(m,n−1)$ when $n>0$, or $(m−1,n+7)$ when $m>0$. Prove that recursive descent terminates. Explain why a directed two-cycle invalidates a claim based only on irreflexivity.

**Solution.** The natural-number order is well-founded, and choosing a minimal first coordinate and then a minimal second coordinate proves well-foundedness of its lexicographic product. The first call decreases the second coordinate while preserving the first; the second decreases the first regardless of its larger second coordinate. Both are strict decreases in that well-founded order, so an infinite call chain is impossible. Nonnegative guards keep the calls inside the carrier, and any branch performing no call terminates its descent. On a two-cycle $a→b→a$ there are no loops, but the nonempty subset ${a,b}$ has no predecessor-free element. Thus irreflexivity alone gives neither well-foundedness nor termination.

### Problem 45. Lattice identities and a distributivity failure

**Original; method: use the order definition of operations.** Prove absorption in a lattice and show precisely how distributivity fails in the five-element diamond with bottom $0$, top $1$, and incomparable middle elements $a,b,c$.

**Solution.** The join $a∨b$ lies above $a$. Hence $a$ is a lower bound of the pair $a,a∨b$, and any common lower bound lies below $a$ because $a$ itself is in the pair. Their greatest lower bound is therefore $a$, proving $a∧(a∨b)=a$. In the diamond, the join of any two different middle elements is 1 and their meet is 0. Consequently $a∧(b∨c)=a∧1=a$, but $(a∧b)∨(a∧c)=0∨0=0$. The two sides differ because $a≠0$. A lattice need not inherit the distributive laws of Boolean algebra.

### Problem 46. Extending a formula to preorders can break it

**Original; method: stress-test an omitted hypothesis.** On ${a,b,c}$ let the base preorder have equivalence blocks ${a,b}$ and ${c}$, with no comparisons between the blocks. Define its proposed strict part by comparison plus inequality, and apply the lexicographic formula on pairs. Show that the resulting relation is not transitive.

**Solution.** The proposed strict part relates $a$ to $b$ and $b$ to $a$, although these elements are equivalent in the preorder. Consequently $(a,a)$ relates lexicographically to $(b,a)$, and $(b,a)$ relates to $(a,c)$, both through unequal first-coordinate comparisons. But $(a,a)$ does not relate to $(a,c)$: the first coordinates are equal, so the formula requires $aPc$ in the second coordinate, which is false. This is a concrete failure of transitivity. Removing equality from a preorder's relation does not automatically produce an asymmetric strict order. The poset hypothesis, or an appropriately defined asymmetric strict part, prevents the return to an equivalent but unequal first coordinate.
