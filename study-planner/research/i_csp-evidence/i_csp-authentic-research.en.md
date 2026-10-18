# CSP authentic examination research

Date:2026-10-18. All answers below are independently derived, not official-key verified.

## Bounded scope

84 PDFs; no CSP hits because relevant pages contain raster exam scans, with searchable watermarks only. This is not an all-question reading claim.
MS CE1400-1405 PDF pages13-18, followed by enlarged original pages for selected questions and rejected candidates.
PhD CE1405 pages16-18, CE1404 page16, CE1403 page16 were inspected; these sampled pages concern machine learning/databases, not usable CSP questions. No PhD CSP item verified in this bounded pass.

The first three records are the strongest chapter-ready items. The fourth is a qualified tree-CSP supplement because the original stem omits the tree premise.

## MS_CE_1404_Q75

Source: Exams/MS/CE/1404/Daftarche-Soalat-Konkur-Arshad-Computer-1404 (konkurcomputer.ir).pdf; PDF/printed page18; booklet335C; question75.
Pinned commit: `bdadf6e2c9cadc4772ae137a96a3da753c7cfd08`.
SHA256: `909e4efaaad96f4d39e526104bc9dc6de6d52be11fd7716e583476b0e62ff654`.

A CSP has variables X,Y,Z,W, with D(X)={1,2,3}, D(Y)={1,2,3,4}, D(Z)={1,2,3}, and D(W)={2,3}. Its constraints are X != Y, Z = W, X + W <= 4, and Z != 3. Which updated domains result after applying arc consistency?

1. {'X': [1, 2], 'Y': [1, 2, 3], 'Z': [2], 'W': [2]}
2. {'X': [1, 2], 'Y': [1, 2, 3, 4], 'Z': [2], 'W': [2]}
3. {'X': [1, 2, 3], 'Y': [1, 2, 3, 4], 'Z': [2], 'W': [2]}
4. {'X': [1, 2, 3], 'Y': [2, 3, 4], 'Z': [1, 2], 'W': [2]}

Independently derived answer: option2.

1. First apply the unary constraint Z != 3, obtaining D(Z)={1,2}. Unary filtering is node consistency; it must precede, or be included in, the propagation process.
2. Under Z=W, Z=1 has no supporting W because W has only 2 and 3. Delete Z=1. Conversely W=3 has no supporting Z after the unary deletion, so delete W=3. Thus Z=W=2.
3. Under X+W<=4 and W=2, X=3 has no support because 3+2=5>4. Both X=1 and X=2 retain the support W=2. Therefore D(X)={1,2}.
4. For X != Y, Y=1 has support X=2; Y=2 has support X=1; and each of Y=3,4 has support X=1 or2. Thus no Y value is removed. In particular Y=4 is not constrained by X+W<=4: that relation has scope (X,W), not (X,Y).
5. All remaining directed arcs have support: each X has a distinct Y, every Y has a distinct X, X+2<=4 for both X values, W=2 has an X support, and equality is satisfied by Z=W=2. This is a fixed point, not just one incomplete pass.
6. The six complete solutions are (X,Y,Z,W)=(1,2,2,2),(1,3,2,2),(1,4,2,2),(2,1,2,2),(2,3,2,2),(2,4,2,2). These provide an independent completeness check for the surviving values in this particular instance; in general arc consistency alone is not a global solution test.

## MS_CE_1404_Q73

Source: Exams/MS/CE/1404/Daftarche-Soalat-Konkur-Arshad-Computer-1404 (konkurcomputer.ir).pdf; PDF/printed page17; booklet335C; question73.
Pinned commit: `bdadf6e2c9cadc4772ae137a96a3da753c7cfd08`.
SHA256: `909e4efaaad96f4d39e526104bc9dc6de6d52be11fd7716e583476b0e62ff654`.

In the illustrated map-coloring CSP, regions D and E have already been colored D=yellow and E=red. Which statement is correct?

1. The degree heuristic selects A, B, or C as the next variable, with no preference among them.
2. The MRV heuristic selects B or C as the next variable, with no preference between them.
3. The degree heuristic selects A as the next variable.
4. The LCV heuristic selects A as the next variable.

Independently derived answer: option1.

1. Translate the map into the exact adjacency graph. A borders B,C,D,E; B borders A,C,E; C borders A,B,D; D borders A,C,E; E borders A,B,D. D and E are already assigned.
2. The usual degree heuristic for selecting the next variable counts constraints on other unassigned variables. The remaining graph on A,B,C is a triangle. Each of A,B,C has exactly two unassigned neighbors, so degree alone leaves a three-way tie. This proves option1.
3. Counting original graph degrees instead would give A degree4 and B,C degree3, but those totals include constraints to already assigned variables. That is the distractor behind option3; it is not the residual-degree rule used to break search ties.
4. Under the usual three-color palette {red,yellow,green}, constraints from D=yellow and E=red leave A={green}, B={yellow,green}, C={red,green}. Thus MRV would select A, not B or C. More generally, with a common palette of k>=3 containing these two distinct colors, A has k-2 remaining values, while B and C have k-1. The printed stem does not explicitly specify palette size; the correct degree answer does not depend on fixing it to exactly3.
5. LCV ranks candidate values after a variable has been selected; by itself it does not select a variable named A. Option4 confuses variable ordering with value ordering.
6. If three colors are used, A=green forces B=yellow and C=red, consistent with all eight edges and fixed D,E. This final coloring is a teaching check, not an additional fact printed in the question.

## MS_CE_1402_Q74

Source: Exams/MS/CE/1402/Daftarche-Soalat-Konkur-Arshad-Computer-1402 (konkurcomputer.ir).pdf; PDF/printed page15; booklet934C; question74.
Pinned commit: `bdadf6e2c9cadc4772ae137a96a3da753c7cfd08`.
SHA256: `16a7ad4fc6a39fb16cd5a1156604457c0b2523ebb4f3e9a2b21c16521529bb4a`.

A CSP is solved by backtracking search, with AC-3 executed at every search node. Which statement is correct?

1. If at some stage one variable has an empty set of allowed values, the CSP has no solution.
2. During one AC-3 execution, every edge of the constraint graph is processed at most d times, where d is the size of the variable domains.
3. If at some stage all variables have nonempty allowed-value sets, the CSP certainly has a solution.
4. If an allowed value is removed from a variable by AC-3, the final search answer will certainly assign that value to that variable.

Independently derived answer: option2.

**Scope qualification.** The work-bound statement uses the standard directed-arc AC-3 interpretation, with initial domain size at most d and one initial copy of each directed arc. An undirected edge represents two directed arcs, giving at most2d total directed revisions rather than literally d for both directions combined. The printed Persian says graph edge; the customary textbook interpretation is an arc. The empty-domain conclusion must be scoped to the current backtracking node.

1. Fix one directed arc (Xi,Xj). It is initially queued once. Later it is queued when D(Xj) shrinks, because Xi values may have lost their support in Xj. Domain values are deleted and never restored during one AC-3 invocation.
2. If D(Xj) initially has at most d values, it can shrink at most d-1 times while remaining nonempty. A final deletion to the empty set stops the invocation immediately in the usual algorithm. Thus (Xi,Xj) is processed at most1+(d-1)=d times before successful termination; failing runs cannot add another successful continuation. This is the intended statement in option2.
3. The count is per AC-3 invocation, not across all nodes of backtracking, where domains are restored and many invocations occur. With e binary undirected edges there are2e directed arcs; each REVISE scans at most d^2 pairs, leading to the usual O(e d^3) naive upper bound.
4. Option1 incorrectly promotes a current-branch contradiction to an assertion about the original CSP. A domain wipeout means no solution extends the assignments at this node; backtracking can still find a solution in another branch.
5. A fully specified example demonstrates that scope distinction. Let X,Y,Z have domains{0,1}. Let Rxy={(0,0),(1,0),(1,1)}, Rxz={(0,0),(1,0),(1,1)}, and require Y!=Z. The initial CSP is arc consistent. Under branch X=0, propagation forces Y=Z=0 and then produces a wipeout. Nevertheless (X,Y,Z)=(1,0,1) and(1,1,0) solve the original CSP.
6. Option3 is false: a triangle of pairwise inequality constraints with every domain{0,1} is arc consistent, since either value has the opposite value as support on each edge; yet the triangle cannot be two-colored.
7. Option4 reverses the meaning of sound deletion. A removed value cannot participate in any complete solution extending the current branch. It is not a promised eventual assignment; after backtracking restores domains, a value may be available in another branch, but that is a different local problem.

## MS_CE_1405_Q74

Source: Exams/MS/CE/1405/Q135A-Arshad1405-[www.konkur.in].pdf; PDF/printed page15; booklet135A; question74.
Pinned commit: `bdadf6e2c9cadc4772ae137a96a3da753c7cfd08`.
SHA256: `e59f06c321cc0b1630f90b6dda4e2b9f61cf163c63c71c83b5deb4082495b42b`.

When solving a CSP by performing the arc-consistency check in reverse order, with n variables each able to take d values, what is the time order of the complete algorithm?

1. O(n^d)
2. O(nd)
3. O(n+d)
4. O(nd^2)

Independently derived answer: option4.

**Scope qualification.** The printed stem does not explicitly state that the constraint graph is a tree. Its phrase reverse-order arc consistency invokes the standard tree-structured CSP algorithm. O(nd^2) is valid under that intended structural premise, not for a general cyclic CSP. Preserve this qualification in the chapter instead of silently adding a tree premise to the source translation.

1. Under the standard intended tree-CSP interpretation, root the constraint tree and choose an order in which each parent precedes its children. There are n-1 edges.
2. Process each nonroot variable in reverse order, revising the arc from its parent to that child. A parent value must have at least one supporting child value. At most d parent values are compared with at most d child values, so one revision costs O(d^2). Over n-1 edges this is O(nd^2).
3. The reverse-order sweep establishes directional consistency. If the root domain remains nonempty, choose a root value and assign each child a compatible value in the forward order. The retained parent values have supports, and disjoint subtrees have no cross-edge constraints, so no backtracking is necessary.
4. With naive support scanning, forward assignment costs at most O(nd), and constructing the order costs O(n). Consequently O(n)+O(nd^2)+O(nd)=O(nd^2), matching option4.
5. The structural condition matters. A cyclic graph can be arc consistent while unsatisfiable, as shown by the two-color triangle; one reverse sweep does not make arbitrary CSPs solvable in this polynomial time. This authentic item should therefore be introduced as an explicitly qualified tree-CSP question rather than evidence for a general complexity claim.

## Independent checks

The four-variable numerical question was solved for all720 permutations of the six initial directed arcs; every queue order reached the same domains. Revision counts ranged from6 to8.
All six complete solutions, the unique three-color map completion, and the two branch-counterexample solutions were independently enumerated in the JSON report.

## Excluded candidates

MS CE1401Q80: no selection heuristic is explicitly stated, and a ternary constraint makes unstated degree/tie conventions material. Do not attach an unqualified unique answer.
MS CE1400Q80: scanned choices need broader interpretation checks; no independently unambiguous key accepted in this pass.
