# Minterms, Maxterms, and Logic Minimization

## Reviewed courses and learning contract

This chapter combines five genuinely read written university sources. Four complementary primary courses are MIT 6.004 (Chris Terman), Cambridge Digital Electronics (Ian J. Wassell), Stanford EE108A (Philip Levis; reader by William J. Dally), and Cornell ECE2300 (Christopher Batten). Columbia CSEE E6861 (Steven Nowick) supplies the fifth, advanced treatment of chart reduction and exact cyclic covering. The [reading and selection audit](../reviews/g_kmap-sources.html) records precise ranges, candidate-pool limits and corrections; the complete references appear at the end.

You should already know Boolean operators, De Morgan’s laws and binary positional notation. The goal here is to turn a verbal specification into an exact Boolean function, simplify it under an explicit cost model, and prove that the result satisfies both its logical requirements and any stated hazard constraints. Every index uses the declared variable order. Unless another objective is stated, “minimum SOP” means fewest product terms, then fewest literal occurrences among those covers; “minimum POS” uses sum factors followed by literals. This objective does not automatically equal minimum transistor count, delay, power or multilevel gates.

The chapter contains a full derivation-based lesson, original diagrams, exact animations, an adjustable four-variable laboratory, 84 fully solved questions and 80 complete review rules. The three archive questions are explicit revisits; one is a convention-sensitive tutorial. Independent finite verification supports the written examples and algorithms, but does not guarantee a score on every unseen question.

## Specification, index order, and canonical forms

### A function starts with a contract

A completely specified Boolean function of n inputs assigns one output bit to every one of its $2^n$ input rows. A combinational implementation must produce that bit after the stated settling conditions. The algebra is not the specification: two different expressions can denote the same function. Conversely, two similar-looking maps can denote different functions if they use different bit orders.

For four inputs in order A,B,C,D, the decimal index is

$$i=8A+4B+2C+D.$$

A is the most significant bit and D the least significant. Input 1010 therefore has index 10. Reordering variables changes indices while the symbolic function remains the same. Do not interpret a list of minterm indices before reading its variable order. A K-map will rearrange where rows appear on paper; it does not change their numerical meaning.

### Minterms select one row; maxterms exclude one row

For a binary row $b_1\ldots b_n$, its **minterm** contains every variable exactly once in an AND product. Use the uncomplemented variable when its row bit is one and its complement when its bit is zero. The product is one on that row only. Its indexed **maxterm** is the OR of every variable, using the opposite literal polarity; it is zero on that row only. For index 10:

$$m_{10}=A\overline B C\overline D,$$

$$M_{10}=\overline A+B+\overline C+D.$$

Evaluate at 1010: each minterm literal is one, and each maxterm literal is zero. At another row at least one bit differs, so the minterm becomes zero and the maxterm becomes one. Therefore $M_i=\overline{m_i}$. This is the fastest polarity check: an indexed maxterm must vanish at its own index, not at the complemented index.

If O is the one-set and Z its complement within all n-bit rows, the canonical representations are

$$F=\sum_{i\in O}m_i=\prod_{j\in Z}M_j.$$

The sum and product signs denote Boolean OR and AND, not ordinary integer addition or multiplication. A canonical SOP, also called canonical DNF here, includes a minterm for every one row. A canonical POS, also called canonical CNF, includes a maxterm for every zero row. General SOP/DNF and POS/CNF need not contain all variables in every term. Canonical uniqueness is relative to the fixed variable list and order; it is not a statement that all equivalent simplified formulas are unique.

<!-- FIGURE:polarity -->

### Worked example 1: the requested form matters

Let $F=(A\Rightarrow C)\land(A\Leftrightarrow B)$. Equivalence forces A=B. When both are zero, C may be zero or one, giving rows 000 and 001. When both are one, implication forces C=1, giving 111. Thus

$$F=\sum m(0,1,7)=\prod M(2,3,4,5,6).$$

The canonical SOP can be compressed to $\overline A\overline B+ABC$, but that expression does not answer a request for a canonical maxterm product. This same distinction appears in the authentic PhD question in the problem bank. Check function, form and variable order independently.

### Missing-variable expansion and constant cases

To expand a product missing C, multiply by $C+\overline C=1$. For example,

$$A\overline B=A\overline B C+A\overline B\overline C.$$

Each missing variable doubles the represented rows. If a product fixes r of n coordinates, it covers $2^{n-r}$ minterms and has r literals. The dual expansion for a sum uses $(P+X)(P+\overline X)=P$. Apply the identity only with Boolean operations; it is not an identity of ordinary real arithmetic. An empty OR is zero and an empty AND is one. Consequently a function with no one rows has an empty canonical SOP, whereas a function with no zero rows has an empty canonical POS. These edge cases are part of the definition, not exceptions to be patched afterward.

## Cubes and Karnaugh-map geometry

### The subcube interpretation

A cube pattern uses 0, 1 and a dash. A dash means that input coordinate is free, not an electrical unknown. Pattern `0-1-` fixes A=0 and C=1, so its product is $\overline A C$ and its cells are 2,3,6,7. It is a valid implicant of a fully specified function only when every one of those cells is in O. Equivalently, its product P satisfies $P\Rightarrow F$ on all rows.

Why must a group have a power-of-two size? Every free coordinate doubles the number of independent assignments, so k free coordinates give $2^k$ cells. The converse is false: a set of four cells need not be a cube. Set {0,1,2,4} varies three bit coordinates and omits several combinations. Nor may a group include a specified zero. Both cardinality and coordinate closure are required.

### Gray order preserves single-bit adjacency

The four-variable map uses AB on the rows and CD on the columns, each ordered 00,01,11,10. Consecutive labels differ in one bit, including the cyclic last-to-first pair. Cells are adjacent when their input rows differ in exactly one coordinate. Horizontal and vertical neighbors—including wrap-around—therefore correspond to legal two-cell cubes. Diagonal cells generally differ in two coordinates and cannot be combined simply because their squares touch at a corner.

<!-- FIGURE:gray -->

### Worked example 2: the four corners are one cube

For $O=\{0,2,8,10\}$, the corner labels are 0000,0010,1000,1010. A and C vary; B=D=0 remain fixed. Thus the four corners form the cube `-0-0` and

$$F=\overline B\overline D.$$

There is no need for four individual minterms. The wrapping geometry merely visualizes the same free-coordinate proof. If one corner were a specified zero, the four-cell group would be invalid. If it were DC, the group might be allowed, depending on the external contract.

<!-- FIGURE:corners -->

### How to read a group without a polarity error

List the row bits of every included cell, retain only coordinates that stay constant, and discard varying coordinates. For an SOP one-group, fixed zero gives a complemented literal and fixed one gives a positive literal. For a POS zero-group, reverse those polarities so that the resulting sum is zero on all grouped rows. Overlap is legal and sometimes necessary: an OR does not double-count a row like numerical addition would. A group need not cover a new row to be algebraically valid, but a group with no new obligation may be unnecessary under the optimization objective.

For five variables, use two corresponding four-variable planes; cells in the same position on the two planes differ in the plane variable. Matching groups can merge across the planes, eliminating that variable. For six variables, four planes may be arranged in Gray order, but groups must also be subcubes in the plane coordinates. A visually rectangular set in an arbitrary drawing is not enough. Beyond small maps, explicit cube algorithms avoid relying on human geometric intuition.

## Prime candidates, essentials, and exact minimum covers

### Maximal cubes are candidates, not the answer

A **prime implicant** is a valid cube that cannot be expanded by freeing any additional fixed coordinate. “Prime” refers to maximal inclusion, not largest cardinality among all primes. Several primes of different sizes may coexist. An **essential prime** owns at least one required one row not covered by any other prime. That row is a witness forcing the prime into every prime cover.

Under the stated two-level term/literal objective, restricting the search to primes loses no optimum. Start with any valid product. If it is not prime, expand it to a containing valid cube. The expansion still avoids specified zeros, does not uncover any one row, uses no extra product term and weakly decreases literal count. Repeating must terminate because only finitely many coordinates can be freed. Expanding every term yields a prime cover with no worse cost; duplicates can be removed. This proof depends on the cost model. It is not a proof that a particular set of primes is globally minimum, nor a general theorem for arbitrary technology-specific costs.

### Worked example 3: essentials prove a lower bound

Consider $F=\overline A B+AC$ in three variables. Its one-set is {2,3,5,7}. The prime set is `01-`, `1-1`, `-11`, corresponding to $\overline A B$, AC and BC. Row 2 is covered only by `01-`, and row 5 only by `1-1`, so both are essential. Together they cover all required rows. Any cover needs at least these two primes; their two-term four-literal cover attains the lower bound. BC is prime but nonessential and unnecessary for ordinary functional minimization. It becomes important under a hazard constraint later.

### A chart makes the obligation explicit

Our prime chart places candidate cubes in rows and required minterm indices in columns. Mark a cell when its row candidate covers its column minterm. A column with one mark forces its owner. Select that owner, delete all columns it covers and solve the residual chart. Do not add DC indices as required columns. Textbooks may transpose the table, so memorize the set relation rather than phrases such as “delete the dominant row.”

<!-- FIGURE:chart -->

**Candidate dominance:** if candidate P covers every residual obligation covered by Q and P costs no more, Q can be discarded while preserving at least one optimum. **Obligation dominance:** if the candidates capable of satisfying u form a subset of those capable of satisfying v, satisfying u guarantees v; remove v, the easier requirement. Equal candidates can be reduced to one representative when only an optimum value is wanted. If every tied optimum expression must be returned, preserve their alternatives or reconstruct them afterward. A prime forced only after discretionary pruning is not necessarily essential in the original chart.

### Worked example 4: no essentials, two optima, and a greedy failure

For $O=\{0,2,3,4,5,7\}$ in three variables, every prime is a pair and every one row has two owners. There are no essentials. The complete prime list is

`0-0`, `01-`, `-00`, `1-1`, `-11`, `10-`.

Two primes can cover at most four rows, so three are necessary. The covers {`-00`,`01-`,`1-1`} and {`0-0`,`-11`,`10-`} each cover all six and have cost (3,6). Choosing `-00` and `-11` first leaves 2 and 5, which cannot share any valid cube; two additional primes are needed. The resulting four-prime cover is irredundant, yet nonminimum. Largest-group-first is therefore a heuristic, not a certificate.

### Petrick’s method is a covering formula

Give each prime P a **selection variable** $s_P$. This variable says that the candidate is included; it is not an input signal of F. For every required row j, OR the selection variables of its owners; AND the clauses for all required rows:

$$\mathcal P=\prod_{j\in O}\left(\sum_{P:j\in P}s_P\right).$$

A selection satisfies this formula exactly when it covers every required row. Multiply out using Boolean idempotence $s_P^2=s_P$ and absorption $S+ST=S$. Products encode subsets of candidates, and absorption deletes supersets. Evaluate the stated cost on the remaining selections; do not treat ordinary polynomial coefficients as relevant. If literals are the secondary objective, two equally small selections may have different cost. Enumeration of all candidates and all nondominated selections gives an exact result, although intermediate output can be exponential.

### Worked example 5: a weighted residual choice

For covering clauses $(P+Q)(Q+R)(P+R)$, Boolean multiplication gives $PQ+PR+QR$. No single candidate satisfies every clause, so each two-candidate selection is minimum in term count. If their literal weights are 2,3,5, the totals are 5,7,8; PQ is the unique lexicographic optimum. A candidate with a larger residual coverage set may still be a bad replacement if its cost is larger. Both geometry and the objective are needed for a valid dominance argument.

## Don’t-cares and product-of-sums minimization

### Three disjoint sets, not three output voltages

An incompletely specified function partitions input rows into required ones O, required zeros Z and optional rows D. A realization H is valid when $H=1$ on O and $H=0$ on Z. Its value on D may be chosen to simplify implementation. SOP candidates may use $O\cup D$ but must intersect O to be useful; DC-only intermediate cubes do not create coverage obligations. Different minimum realizations can disagree on D without violating the specification.

### Worked example 6: choosing a completion

In two variables, let O={1}, Z={2}, D={0,3}. The cube `0-` yields $\overline A$, while `-1` yields B. Both have one term and one literal, satisfy row 1 and avoid row 2, yet disagree on the optional rows. Neither is “the true value of the don’t-care.” The optimized circuit chooses a completion. If a later environment requires output zero at row 0, $\overline A$ becomes invalid while B remains valid.

Marking BCD codes 10–15 optional requires an external input/use guarantee. It does not imply those patterns cannot occur briefly during an asynchronous multi-bit transition. Binary 7 to 8 changes all four bits and may visit intermediate codes as paths settle. Specify sampling or qualification behavior before interpreting a steady-state DC specification as a physical safety claim.

### POS: solve the complement, then negate

To minimize POS, cover Z with products for $\overline F$, using the same optional set D. Complement each product into a sum and combine them by AND. A zero cube `-0-0` gives product $\overline B\overline D$ in the complement and factor B+D in F. Mixing the one-set and zero-set conventions is the most common POS polarity error.

### Worked example 7: majority in two forms

Three-input majority has $O=\{3,5,6,7\}$ and $Z=\{0,1,2,4\}$. Its minimum SOP is $AB+AC+BC$. In the complement, each weight-one zero row forces its corresponding two-zero cube, yielding $\overline F=\overline A\overline B+\overline A\overline C+\overline B\overline C$. Therefore

$$F=(A+B)(A+C)(B+C).$$

Both forms have three two-literal components in their respective two-level models. They are not canonical because each component omits a variable. Their canonical forms still contain four three-literal components each. Canonical expansion, functional minimization and gate realization are three separate stages.

<!-- FIGURE:pos -->

## Quine–McCluskey from generation to exact covering

### Phase one: enumerate every prime

Begin with binary patterns for every index in $O\cup D$. Grouping by number of ones speeds comparisons, but correctness depends on the merge condition: two patterns have identical dash positions and differ in exactly one fixed bit. Replace that bit by a dash, mark both parents as combined and deduplicate the child. After a generation, uncombined patterns are prime candidates. Continue until no child remains. Remove DC-only terminal cubes from the useful candidate list, but allow them during generation because they can help form a later useful cube.

The condition is necessary: patterns `01-0` and `11-0` merge to `-1-0`; patterns `0-10` and `01-0` have unequal free-position masks and cannot merge directly. Their union does not contain every combination required by a larger subcube. Merely counting one character difference after ignoring dashes invents unauthorized rows.

### Why iterative merging is complete

Every valid cube with at least one free position can be split along that position into two valid half-cubes. Both halves are subsets of the allowed set. Induct on the number of free positions: zero-free cubes are initial allowed rows; if every valid k-free cube is generated, the two halves of a valid (k+1)-free cube are generated and meet the merge condition. Thus every valid cube is eventually generated. Uncombined terminal cubes are exactly the maximal ones. Deduplication changes neither this argument nor the set of primes; failing to mark all parents, however, can incorrectly report a nonprime as prime.

### Worked example 8: generation is not cover selection

For O={0,2,8,10}, start with 0000,0010,1000,1010. First merges include `00-0`, `10-0`, `-000` and `-010`. The first two can merge to `-0-0`, as can the last two. Keep one copy and mark every contributing parent. No further valid expansion exists. The single prime covers all obligations, so selection is trivial here. In a cyclic chart, generation still finds every prime but does not by itself choose the minimum cover: the chart/Petrick phase remains necessary.

<!-- FIGURE:qm -->

### Exact reference implementation

The following small educational implementation generates primes and enumerates covers. It is intended for bounded functions, not large industrial synthesis. Its set-based cost and truth-row checks make the reasoning visible. The laboratory uses the same mathematical contract but an independently written implementation; verification compares both with separate truth-table enumeration.

```python
from itertools import combinations

def merge(a, b):
    if [i for i, x in enumerate(a) if x == '-'] != \
       [i for i, x in enumerate(b) if x == '-']:
        return None
    changed = [i for i, (x, y) in enumerate(zip(a, b)) if x != y]
    if len(changed) != 1:
        return None
    i = changed[0]
    return a[:i] + '-' + a[i + 1:]

def prime_patterns(n, on, dc):
    current = {format(i, f'0{n}b') for i in set(on) | set(dc)}
    terminal = set()
    while current:
        used, following = set(), set()
        for a, b in combinations(sorted(current), 2):
            child = merge(a, b)
            if child is not None:
                used.update((a, b))
                following.add(child)
        terminal.update(current - used)
        current = following
    return terminal  # filter DC-only cubes before building the chart
```

There are $3^n$ possible cube patterns before function-specific filtering. Cover search can have exponentially many subsets of primes. These counts explain why exact small examples are tractable while arbitrary large exact synthesis is not. An algorithm being systematic does not make its worst-case cost polynomial. Heuristics may be useful in a different setting; they should not be mislabeled exact proofs in an examination solution.

## Hazards, constrained cost, and shared implementation

### Vertex correctness and transition correctness differ

A truth table checks settled endpoints. A static-one hazard is a possible 1–0–1 excursion when one input changes and both settled endpoints require one. In a two-level SOP with stable other inputs, an adjacent required-one pair must lie in a common selected product to remove that risk for arbitrary positive path delays. A product independent of the changing input remains asserted throughout the transition. A chart for hazard-free SOP must therefore cover both vertex obligations and the relevant adjacency-edge obligations.

### Worked example 9: consensus is redundant but useful

For $F=\overline A B+AC$, set B=C=1. A’s change transfers responsibility between two products. With unequal paths, both may temporarily be zero. The consensus BC covers both adjacent endpoint rows 011 and 111 and is independent of A. Adding it gives

$$F=\overline A B+AC+BC.$$

The added term changes no settled row: insert $A+\overline A$ into BC, distribute, and absorb the two parts into the originals. Nevertheless, the additional gate can be necessary for transition correctness. A minimum functional SOP and a minimum hazard-free SOP solve different constrained problems. The static-zero dual adds a consensus **sum** to a two-level POS; multilevel dynamic hazards and simultaneous input changes require additional analysis.

<!-- FIGURE:hazard -->

### Worked example 10: an exact delay trace

Use $F=AB+\overline A C$, initially A=B=C=1 and settled. Let A fall at time zero. Inverter delay is three units; each AND and the OR have delay one. Under transport delay, AB falls at time 1, the inverter rises at time 3, and the other product rises at time 4. The OR consequently falls at time 2 and rises at time 5. The low pulse lasts three units. A stable BC product removes this gap. An inertial model can reject pulses based on its specified threshold; do not silently substitute that physical assumption into a transport calculation.

### A real archive question exposes the missing convention

MSc CE 1405 Q78 specifies zeros {2,3,4,10,11,12,13,14} and DC rows {0,1}; the required ones are {5,6,7,8,9,15}. The required single-bit one-edges are (5,7), (6,7), (7,15), (8,9). If only transitions whose endpoints are both in O must be protected, two-level **prime** SOP and lexicographic term/literal cost force $\overline A BD$, $\overline A BC$, BCD and $\overline B\overline C$, giving cost (4,11). A twelve-literal alternative preserves care-row behavior and these required edges while not being minimum under that declared cost. The bank explains the printed question’s ambiguity instead of pretending that hazard freedom alone selects a unique option.

There is a further contract distinction: the four-term realization assigns DC rows 0 and 1 to one, creating the realized-one edge (1,5). No selected term covers both of those rows. If DC-to-care transitions must also be protected, add $\overline A\overline C D$ as a bridge, or choose a different completion. Assigning both DC rows zero and using $A\overline B\overline C$ in place of $\overline B\overline C$ gives a four-term twelve-literal realization whose full realized-one graph has every edge protected. The (4,11) result is therefore not an unconditional hazard-free claim over all completed rows. This example demonstrates why both the care-set contract and the allowed transition set must be stated.

### Mapping and sharing need their own objective

A SOP can be implemented by NAND gates in both stages via De Morgan; a POS has the NOR–NOR dual. Inverter availability, gate fan-in, tied pins, output polarity and shared subexpressions alter costs. A two-level expression optimum does not prove a minimum arbitrary gate network. For $F=AB+AC$ and $G=AB+BC$, a PLA can share AB and use three distinct products, whereas separate lists contain four product occurrences. There are still four product-output connections. A shared cube must avoid the zero-set of every output it feeds. Do not share a visually similar term whose truth rows violate one output.

## Fully solved mathematical and conceptual questions

Read the lesson before attempting practice. Solutions are expandable and become visible automatically in print. Tasks include explicit index conversions, all optimal SOP/POS covers, DC completions, prime-chart proofs, lower bounds, dominance counterexamples, parity/threshold families, hazard timing, shared products and genuine archive questions. Difficulty labels are author judgments, not measured calibration scores. Course-inspired questions are independently written; authentic questions are labeled with their exact original page and provenance.

<!-- INCLUDE:problems -->

## Complete summary and examination rules

<!-- INCLUDE:review -->

## Adjustable exact-cover laboratory

Enter required ones and optional don’t-cares as decimal indices from 0 through 15. Every other row is required zero; the variable order is A,B,C,D. Choose SOP or POS. The laboratory enumerates all valid cubes, identifies primes and every minimum cover under the chapter’s term/literal objective, and animates the first optimal cover. The displayed zero or one at a DC cell is the selected completion, not an extra requirement. Empty sets are accepted. Invalid indices, duplicates and overlapping O/D sets are rejected.

<!-- LAB:kmap -->

Inspect Gray labels, covered obligations, candidate patterns and the exact cost at each checkpoint. Playback is a visual teaching aid; paused steps and the table provide the mathematical evidence. A cover’s lack of missing vertices does not by itself certify hazard freedom. This lab solves functional SOP/POS only; hazard examples use explicitly augmented edge constraints in the lesson and animations.

## References and reading ranges

1. Massachusetts Institute of Technology — Chris Terman. **6.004 Computation Structures**, Spring 2017. [Lecture 4 written annotations](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c4/c4s1/), slides 1–4 and 10–20 read in depth; implementation context 21–29 screened.
2. University of Cambridge — Ian J. Wassell. **Digital Electronics**, 2025–26. [Combined lecture slides](https://www.cl.cam.ac.uk/teaching/2526/DigElec/combined_25.pdf), pages 21–43; [Examples Paper 1](https://www.cl.cam.ac.uk/teaching/2526/DigElec/examples_25_1.pdf), all three pages, March 2025. Formula polarity was visually checked where extraction lost overbars.
3. Stanford University — Philip Levis, **EE108A**, Winter 2008; William J. Dally, reader author, copyright 2002–2006. [Reader, Chapters 1–12](https://web.stanford.edu/class/archive/ee/ee108a/ee108a.1082/reader/ch1to12.pdf), Chapter 6, PDF pages 83–105. Historical terminology and primality errors are corrected in the independently authored lesson.
4. Cornell University — Christopher Batten. **ECE2300 / ENGRD2300 Digital Logic and Computer Organization**, Fall 2026. [T03 Boolean Algebra](https://www.csl.cornell.edu/courses/ece2300/handouts/ece2300-T03-bool-algebra.pdf), all 26 pages, revision 2026-09-08. Original figures are not reproduced.
5. Columbia University — Steven Nowick. **CSEE E6861**, Handout 5, 21 January 2016. [The Quine–McCluskey Method](https://www.cs.columbia.edu/~cs6861/handouts/quine-mccluskey-handout.pdf), all 15 pages. Exact covering is extended with explicit secondary literal cost and preservation of all tied alternatives.
6. Iranian examination archive — [Phd-Exam-CSE, pinned Exams tree](https://github.com/bheydari721rn24/Phd-Exam-CSE/tree/bdadf6e2c9cadc4772ae137a96a3da753c7cfd08/Exams). MSc CS 1405 Q99, PDF page 22; PhD CS 1405 Q22, PDF page 8; MSc CE 1405 Q78, PDF page 16. Independent English adaptations and answers; one convention-sensitive tutorial; not official answer keys or newly unique archive items.

All diagrams, model code, prose and original questions in this chapter are independently authored. The source audit states the finite research boundary and the evidence record stores document fingerprints without redistributing the original university PDFs.
