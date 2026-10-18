# Original Iranian Examination Reconstructions

These two English reconstructions were checked against rendered original PDF pages in the pinned repository archive. The solutions are independently derived; no official answer-key verification is claimed. The mathematical tree, edge order, labels, option order and interval endpoints are retained. Screening selected recent CE files does not mean every MS/PhD archive has been exhausted; no unverified doctoral question is added merely to fill a category.

## Authentic 1. MS Computer Engineering1403, Question68

**Source.** Repository commit `bdadf6e2c9cadc4772ae137a96a3da753c7cfd08`; `Exams/MS/CE/1403/Daftarche-Soalat-Konkur-Arshad-Computer-1403 (konkurcomputer.ir).pdf`; printed/PDF page15, booklet164C. SHA256 `ad6b3b405c49f239a794243f303209ef45e66912a9739b938ab9fe3fe645cb66`.

**Question.** For the depicted game tree, alpha-beta search is used to find an optimal move. Which listed nodes are pruned? The complete ordered tree is `MAX(MIN(MAX(8,2),A=MAX(B=5,C=3)),D=MIN(15,E=MAX(F=4,G=7)))`.

1. C and G.
2. E, F and G.
3. A, B and C.
4. No node is pruned.

**Solution.** At the left MIN child, the first MAX child evaluates8and2and returns exact8. That MIN node now has beta8. Its second child$A$is a MAX node. The leaf$B=5$does not reach beta8, and neither does$C=3$. Thus neither leaf is pruned; $A$has exact value5and the left MIN returns$\min(8,5)=5$. The root's incumbent alpha becomes5.

The right MIN node$D$first evaluates terminal15. Since15is greater than inherited alpha5, the remainder of$D$cannot be discarded. It passes beta15to$E$. At MAX node$E$, the first leaf$F=4$does not reach15. The inherited alpha5does not make this a cutoff: at MAX, a beta threshold must be reached, not merely an alpha threshold. The leaf$G=7$is also evaluated and remains below15. Hence$E=7$, $D=\min(15,7)=7$and the exact root value is7.

The visited terminal sequence is8,2,5,3,15,4,7. Every shown node is entered; no node is pruned, so option4is correct under the usual left-to-right search of the shown order. Pruning$G$after seeing$F=4$would confuse MIN's cutoff direction with MAX's. Pruning$A$after its first leaf5would compare against an invented threshold5before the root's left subtree had even finished.

## Authentic 2. MS Computer Engineering1404, Question69

**Source.** Repository commit `bdadf6e2c9cadc4772ae137a96a3da753c7cfd08`; `Exams/MS/CE/1404/Daftarche-Soalat-Konkur-Arshad-Computer-1404 (konkurcomputer.ir).pdf`; printed/PDF page16, booklet335C. SHA256 `909e4efaaad96f4d39e526104bc9dc6de6d52be11fd7716e583476b0e62ff654`.

**Question.** Alpha-beta search prunes branches in the displayed adversarial tree. For which ranges may the leaf values4and15be changed while leaving exactly the same branches pruned? Replace these two leaves by$x$and$y$respectively. The ordered tree is `MAX(10,MIN(MAX(x,3,2),MAX(7,1)),MIN(MAX(y,6),MAX(20,23)))`.

1. $x\in(-\infty,10]$ and $y\in(10,20]$.
2. $x\in(-\infty,10]$ and $y\in(10,\infty)$.
3. $x\in(3,10]$ and $y\in(10,\infty)$.
4. $x\in(3,10]$ and $y\in(10,20]$.

**Solution.** First inspect the original$x=4,y=15$case rather than guess from the options. The terminal10sets root alpha10. The middle MIN child first evaluates `MAX(4,3,2)`, which returns4after all three leaves. Since $4\le10$, the entire sibling `MAX(7,1)` is pruned. The last MIN child evaluates `MAX(15,6)=15`. It is not rejected because $15>10$. Its second MAX child then sees20, which reaches inherited beta15and prunes23. These are the original pruned branches.

For the first condition, `MAX(x,3,2)` always examines its three leaves in this context, because no finite beta has yet restricted that MAX node. Its result is $\max(x,3)$. To retain the cut of `MAX(7,1)`, require $\max(x,3)\le10$. Since3already satisfies this threshold, the condition is exactly$x\le10$, with **no lower bound3**. Equality10still cuts under the standard nonstrict rule.

After this branch, the root incumbent remains10. The last MIN child's first MAX result is$\max(y,6)$. To enter its second MAX child rather than cut that entire subtree, require $\max(y,6)>10$, equivalent to$y>10$. Its beta is then$y$. To preserve the subsequent cut of23after visiting20, require $20\ge y$. Combining these requirements gives$10<y\le20$.

Thus option1is correct. At$y=10$, both20and23would be skipped, changing the pruned set. At$y>20$, the leaf20would no longer justify skipping23. At$x=10$, the original middle cut remains valid. For arbitrarily negative$x$, the first MAX result is3and the same middle cut still occurs. The root value is allowed to change with$y$; the question asks to preserve the pruned branches, not to preserve the original numerical root value15.
