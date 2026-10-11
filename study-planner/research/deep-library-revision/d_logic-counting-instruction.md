## Mathematical bridge: from formula semantics to examination calculations

The definitions of implication and quantification become calculation methods only after the objects being counted have been specified. The following derivations connect the preceding university-source instruction to the question bank. They count labelled interpretations; changing to unlabelled structures would require identifying isomorphic structures and is a different problem.

### A. Three different counting spaces

For $k$ independent propositional atoms there are $2^k$ input valuations. A Boolean function chooses one output bit for each such input, so there are $2^{2^k}$ Boolean functions. These are not interchangeable counts. On a fixed domain of $n$ objects, a unary predicate chooses a subset and therefore has $2^n$ interpretations; a binary relation chooses a subset of $D\times D$ and has $2^{n^2}$ interpretations. A free-variable assignment for a fixed structure is another object: $k$ independently assignable free variables have $n^k$ assignments.

For two Boolean atoms, the four inputs are 00, 01, 10 and 11. The conjunction has exactly one satisfying input but is just one of sixteen possible Boolean functions. For a two-object domain, there are four unary predicates and sixteen binary relations. These numerical examples identify the exponent's meaning rather than relying on memorized formulas.

### B. Quantifiers as matrix operators

Represent $R(x,y)$ by an entry $r_{xy}$ of a zero-one matrix. Fixing $x$ selects one row. Existential quantification over $y$ takes the OR of that row; universal quantification takes its AND. Outer quantification then combines the resulting row values. Thus

$$\forall x\exists yR(x,y)=\bigwedge_x\bigvee_y r_{xy},$$

while $\exists y\forall xR(x,y)$ first takes the AND down each column and then ORs the column results. The first asks whether all rows are nonempty; the second asks whether some column is full. A full column implies all rows are nonempty, but the identity matrix on two or more objects shows the reverse implication fails.

The quantifier order records a dependency rather than the order in which a computer happens to loop. In the first statement, each row may select a different target. In the second, the one selected column must work for all rows. Negating the first expression yields an OR of rowwise ANDs of negated entries, which is exactly the existence of an empty row.

### C. Why the row product works, and when it fails

For $a$ labelled inputs and $b\ge1$ labelled targets, a row can choose any nonempty subset of the targets in $2^b-1$ ways. Since rows control disjoint ordered pairs, row choices are independent and the total relation count is $(2^b-1)^a$. Requiring exactly one target gives $b^a$; requiring at most one gives $(b+1)^a$.

Column restrictions destroy this unconstrained product. For example, requiring a function to be onto forces every target column to be used. On equal finite domain and codomain sizes $n$, a total injective function has $n!$ choices instead of $n^n$. On unequal sizes, injectivity yields the falling product $b(b-1)\cdots(b-a+1)$ when $a\le b$, and zero when $a>b$. A statement about row existence alone must not silently inherit any of these column conditions.

### D. Exact failure counts and overlap

If each row has $b$ bits, the unrestricted relation count is $2^{ab}$. Its all-nonempty subset has $(2^b-1)^a$ members, so the number with at least one empty row is their difference. Exactly $t$ empty rows requires choosing their locations and making every other row nonempty:

$$\binom at(2^b-1)^{a-t},\qquad0\le t\le a.$$

Summing over $t\ge1$ gives the complementary count. By contrast, choosing a marked empty row and freely filling the other rows gives $a\cdot2^{b(a-1)}$. That counts a relation once for every empty row it has. The error is not arithmetic: the procedure constructs marked relations, whereas the question asks for unmarked relations. Inclusion-exclusion is an alternative correction when a convenient complement is unavailable.

### E. Implication constraints on a function table

Let $G$ and $H$ be fixed Boolean functions on the same input set. Requiring both $G\Rightarrow F$ and $F\Rightarrow H$ means $G(u)\le F(u)\le H(u)$ for every input $u$. If an input has $G(u)=1,H(u)=0$, the constraints are inconsistent and there are no functions $F$. Otherwise, inputs of type (1,1) force output one; inputs of type (0,0) force output zero; and inputs of type (0,1) leave a free output bit. If there are $t$ inputs of that last type, exactly $2^t$ functions qualify.

This is a pointwise proof: a function table is reconstructed uniquely from its independent output choices. An atom absent from $G,H$ still belongs to the specified input space of $F$, so each old row splits into two when that atom is added. The number of free rows consequently doubles; the number of qualifying functions is squared. Ignoring the unused atom is harmless for equivalence of formulas but wrong when counting functions with a stated arity.

### F. Structural models versus truth-functional laws

For a fixed finite first-order structure, evaluating a sentence is a finite computation, and a matrix gives an exact representation of a binary relation. Counting all structures of a fixed finite size can refute or confirm a property on that size. It does not establish that the property holds on every size, or on infinite structures. The general row-counting formula is justified by a bijection valid for arbitrary positive sizes; its finite enumeration is only a supporting check.

Equivalence laws must likewise preserve the assignment space and binding scope. The implication $A\Rightarrow B$ is equivalent to $\neg B\Rightarrow\neg A$, not generally to its converse. Quantifier movement requires checking whether the variable occurs free in the other operand. If a rewrite changes a free occurrence into a bound one, it changes the problem being solved rather than simplifying it.

### G. A complete written solution has two proof obligations

A claimed count needs both a construction and an exclusion argument. Explain how each valid object is generated, why every valid object can be generated, and why none is generated twice. A claimed universal truth needs an exhaustive table or an argument valid for arbitrary inputs. A claimed failure needs a complete countervaluation or a fully specified structure, followed by evaluation of the premises and conclusion in that model.

Rejecting a distractor also requires identifying its actual defect. An equivalent DNF is not false merely because a question requests CNF: it is the wrong representation. A false formula requires a counterexample. A wrong count may count a marked witness, omit an existence condition, or impose injectivity. Naming the defect and giving a small example makes the solution reusable in a different examination question.
