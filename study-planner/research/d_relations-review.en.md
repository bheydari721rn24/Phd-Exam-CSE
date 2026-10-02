### 10.1 The chapter in one connected explanation

A relation is a typed set of ordered pairs. Its logical properties constrain loops, reversed pairs, and consecutive edges. Composition asks whether a shared middle witness exists. Powers specify exact path lengths, whereas closures collect all permitted lengths and must be proved least among admissible supersets. Equivalence relations replace individual elements by indistinguishability classes. Preorders become partial orders after identifying mutual comparison. Partial orders express consistent precedence; covers compress their finite diagrams, bounds quantify over an ambient carrier, and chain/antichain theorems connect structure to scheduling. Well-foundedness supplies minimal counterexamples and validates decreasing recursive descent. Each transition adds a hypothesis that must be checked rather than assumed.

### 10.2 Seventy-two rules for precise examination reasoning

#### Types, algebra, and matrices

1. Always record the source and target carriers before checking any relation property that quantifies over them.
2. The source carrier need not equal the active domain, and the target carrier need not equal the range.
3. A total function requires exactly one target for every source; at most one describes only right-uniqueness.
4. Left-totality tests for nonempty rows, whereas relational surjectivity tests for nonempty columns.
5. A converse relation always exists, even when an inverse function does not.
6. State the composition convention explicitly; here $S∘R$ means first $R$ and then $S$.
7. With source rows and target columns, the Boolean matrix for $S∘R$ multiplies $M_R$ followed by $M_S$.
8. Boolean conjunction and disjunction compute existence; ordinary multiplication and addition count intermediate witnesses.
9. Associativity permits changing parentheses but does not permit exchanging relation order.
10. Converse reverses the composition order as well as every edge direction.
11. Composition distributes over unions on either side, but intersection equality can fail through different intermediate witnesses.
12. Relational image preserves union; image and existential inverse image need not preserve intersections or complements.

#### Logical properties and counting

13. Disprove a universal relation property with a full witness, including both its hypotheses and its failed conclusion.
14. A missing loop disproves reflexivity, while one existing loop disproves irreflexivity.
15. Having some but not all loops means the relation is neither reflexive nor irreflexive.
16. Antisymmetry permits loops and prohibits two-way edges only between distinct elements.
17. Asymmetry prohibits every two-way pair, including a loop.
18. Symmetry and antisymmetry together force all pairs to be diagonal, but do not require every diagonal pair.
19. Transitivity must be checked when its variables repeat; a two-cycle forces loops.
20. A relation with no composable edge pair is transitive by vacuity.
21. On a nonempty carrier the empty relation is transitive and asymmetric, but it is not reflexive or serial.
22. On the empty carrier all universally quantified properties in this chapter hold for the unique empty relation.
23. Irreflexivity plus transitivity implies asymmetry; antisymmetry alone does not prohibit longer cycles.
24. A symmetric transitive relation is reflexive on its active domain, and becomes reflexive on the whole carrier if seriality is added.
25. Reflexivity plus cyclicity characterizes equivalence, and reflexivity plus right-Euclideanity also characterizes it.
26. Count symmetric relations by diagonal choices and unordered pairs, not by independent choices for both directions.
27. Each unordered pair has three antisymmetric choices; allowing the fourth two-way choice violates antisymmetry.
28. Do not use local pair-choice counts for transitive relations, because transitivity couples those choices.

#### Paths and closures

29. The identity is $R⁰$; a zero-length path stays at its starting element.
30. The power $R^k$ means exactly $k$ steps, and consecutive powers need not contain one another.
31. Positive closure $R⁺$ contains cycle-induced loops but does not automatically contain every isolated vertex's loop.
32. Reflexive transitive closure is $R⁎=I_A∪R⁺$ and includes every zero-length path.
33. On a nonempty $n$-element carrier, powers through $n$ suffice for positive closure; an $n$-cycle shows why the last power may be needed.
34. For reflexive transitive closure, identity plus powers through $n−1$ suffice because identity already provides all loops.
35. A closure proof must establish both the required property and leastness among all admissible supersets.
36. An antisymmetric extension cannot be created by adding edges when two distinct vertices already compare both ways.
37. Reflexive closure commutes with symmetric closure and with transitive closure, but symmetric and transitive closure need not commute.
38. Equivalence closure is reflexive transitive reachability after adding reverse edges, including loops at isolated vertices.
39. Intersection of equivalence relations remains equivalence; union may require transitive closure.
40. Warshall's outer loop selects the newly permitted internal vertex, not a path length or an endpoint.
41. Initialize Warshall without added loops for positive closure, and with the diagonal true for reflexive transitive closure.
42. In-place Warshall is justified by the unchanged pivot row and column during a stage, not merely by empirical success.

#### Classes, orders, and diagrams

43. Two equivalence classes are either disjoint or equal; intersecting representatives do not create partially overlapping classes.
44. A quotient element is a class, and different representative names can denote the same quotient element.
45. A quotient formula must produce equal target objects for every allowed representative replacement.
46. For quotient-valued outputs, representative independence requires equivalent outputs rather than identical representatives.
47. The relation from blocks of sizes $b₁,…,b_k$ has $b₁²+···+b_k²$ pairs.
48. Equivalence relations on labelled carriers are counted by unlabelled partitions; multiply by a block-label factor only when the question supplies labels.
49. Mutual comparison in a preorder defines equivalence, and comparison between its classes is a well-defined partial order.
50. One-way directed reachability need not be symmetric, whereas mutual reachability defines strongly connected classes.
51. Positive-integer divisibility is a partial order; all-integer divisibility fails antisymmetry because signs can differ.
52. Failure of $a≼b$ does not imply $b≼a$ in a partial order because the pair may be incomparable.
53. An acyclic edge graph becomes a strict order after positive closure; acyclicity alone does not supply missing transitive edges.
54. Product order requires both coordinate comparisons, whereas lexicographic order prioritizes the first unequal coordinate.
55. The lexicographic formula using comparison plus inequality as its strict part must not be applied blindly to a preorder.
56. A Hasse edge denotes a cover, and an upward path denotes a strict comparison under this chapter's stated orientation.
57. Drawing height, horizontal placement, and edge crossings do not themselves define a poset comparison.
58. Finite cover graphs recover their order by reflexive transitive closure; infinite dense orders show why finiteness matters.
59. An order isomorphism must preserve and reflect comparison; a monotone bijection alone can turn incomparable elements into comparable ones.

#### Bounds, scheduling, and well-foundedness

60. Minimal and maximal are relative to the selected subset, whereas least and greatest require comparison with every member of that subset.
61. In a finite nonempty poset a unique minimal element is least; the implication can fail in an infinite poset.
62. Bounds must belong to the ambient carrier, while they need not belong to the subset being bounded.
63. Prove a supremum by first proving it is an upper bound and then comparing it with every other upper bound.
64. Several incomparable minimal upper bounds imply that no supremum exists; one plausible bound is not enough.
65. A subset maximum is its supremum when present, but an existing supremum may lie outside the subset.
66. The empty subset's supremum is the ambient least element, and its infimum is the ambient greatest element, when those exist.
67. A lattice gives meet and join for every pair; complete-lattice claims additionally require every subset, including empty and unbounded subsets.
68. Every lattice satisfies associativity, commutativity, idempotence, and absorption, but distributivity needs an additional property.
69. Under unit durations and unlimited processors, optimal dependency time equals poset height measured in vertices; limited processors or unequal durations change the model.
70. The minimum antichain-partition count equals height, the minimum chain-partition count equals width, and $n≤hw$ relates the two.
71. Finite acyclicity gives well-foundedness, while finite irreflexivity without acyclicity does not.
72. A well-founded induction or termination argument must identify a genuine decreasing relation and keep every recursive argument inside its declared carrier.

### 10.3 A decision procedure for difficult questions

| Question type | A reliable sequence of actions | Worked examples |
|---|---|---|
| Classify a relation | Fix the carrier; inspect loops; inspect reverse pairs; inspect all two-edge chains; show a witness for every failure. | Problems 8–14. |
| Compute a composition | Write source, middle, and target types; enumerate middle witnesses; collapse duplicate endpoints; check matrix orientation. | Problems 4–7. |
| Count constrained relations | Separate diagonals and unordered pairs; identify independent choices; check whether transitivity destroys independence. | Problems 2 and 15. |
| Compute a closure | State positive or zero-length convention; preserve directions; apply the appropriate leastness construction; check isolated vertices and cycles. | Problems 16–23. |
| Construct a quotient | Prove equivalence; identify distinct blocks; check every representative replacement; distinguish target equality from representative equality. | Problems 24–29. |
| Analyze a poset | Establish its axioms; find strict comparisons and covers; read upward paths; distinguish incomparable from reversed pairs. | Problems 30–34 and 40. |
| Find a supremum or infimum | List ambient bounds; test leastness or greatestness among them; inspect missing carrier elements and empty subsets. | Problems 35–39 and 45. |
| Prove an optimal schedule | State durations and processor assumptions; produce a feasible schedule; certify a matching lower bound using a chain. | Problems 41–42. |
| Prove a minimum chain cover | Produce a valid matching or chain partition; supply an antichain of the same size or another maximum-matching certificate. | Problems 33 and 43. |
| Validate descent or a generalized theorem | Identify the omitted hypothesis; inspect cycles, domain guards, and representative-equivalent elements; use a precise counterexample if needed. | Problems 44 and 46. |

### 10.4 Final error checklist

Before accepting an answer, check the direction of every edge and matrix index, the carrier of every bound and quantifier, the distinction between exact and arbitrary path length, the presence of isolated vertices, the scope of every finite hypothesis, the independence of every quotient representative, and both sides of every “if and only if.” A proof that computes a candidate must still establish its claimed extremality. A diagram must state its orientation and display the mathematical structure actually asserted in the text. These checks support rigorous preparation; they are not a promise about a future question whose assumptions are unknown.
