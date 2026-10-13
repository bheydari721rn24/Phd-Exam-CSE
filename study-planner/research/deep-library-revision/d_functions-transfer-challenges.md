## Ten solved synthesis challenges

These independently authored challenges extend the authentic and course-derived bank. Their solutions retain the labelled carriers, quantified conditions and exact objects counted. Each is accompanied by a model of its own function or construction, rather than an unrelated example.

### Challenge 1. Onto maps with an upper bound on each fiber

**Question.** Count surjections from six labelled inputs to three labelled targets when no target has more than three antecedents.

**Solution.** Each fiber is nonempty, each size is at most three and their sum is six. The only unordered size profiles are (3,2,1) and (2,2,2). For the first profile, the three different sizes can be assigned to the three named targets in 3!=6 ways. For each assignment, distribute the six input labels in $6!/(3!2!1!)=60$ ways. This contributes 360. For the second profile all sizes agree, so there is only one labelled size assignment and $6!/(2!2!2!)=90$ input distributions. The total is $360+90=450$.

There is a useful independent subtraction. Unrestricted surjections to three targets number $3^6-3\cdot2^6+3=540$. The only excluded onto profile is (4,1,1); choose its four-element target fiber in three ways and assign inputs in $6!/4!=30$ ways, removing 90 maps. This gives 450 again. A size-five fiber cannot be onto three targets because only one input remains for two required nonempty fibers. Dividing the equal-size profile by 3! would incorrectly remove distinct labelled input assignments.

### Challenge 2. Count inverse pairs in two different directions

**Question.** A has two labelled elements and B four. Count pairs $f:A\to B$, $g:B\to A$ with $g\circ f=\operatorname{id}_A$. Then obtain the same count by first fixing g.

**Solution.** The left identity forces f injective. There are $4\cdot3=12$ injections. For each f, g is forced on its two image points and independently chooses either A-point at each of two unused B-points. The total is $12\cdot2^2=48$.

For the second count, write the two fiber sizes of g as r and 4−r. A right inverse f of this fixed g chooses one representative from each, yielding r(4−r). There are $\binom{4}{r}$ maps g with the first named fiber of size r. Thus
$$\sum_{r=1}^{3}\binom{4}{r}r(4-r)=4\cdot3+6\cdot4+4\cdot3=48.$$
The maps with r=0 or r=4 contribute zero because a target is missed. For g-fibers of sizes 1 and 3, the three sections select the unique first-fiber input and one of the other three. This agrees with the reverse-map identity, but the opposite pair identity $f\circ g=\operatorname{id}_B$ is impossible on these sizes: it would inject four B-elements into two A-elements.

### Challenge 3. Multiplicities of the direct-image and preimage operators

**Question.** Let A={0,1,2,3}, B={a,b,c,d}, and f have output tuple (a,a,b,c). Classify the two power-set operators and count their ambiguities.

**Solution.** The attained fibers have sizes 2,1,1; d is unused. The direct-image map I_f is neither injective nor onto. Its domain has 16 subsets, while its image contains exactly the eight subsets of {a,b,c}. The singleton subsets {0} and {1} have the same image {a}; target subset {d} is never attained.

For a target subset T contained in {a,b,c}, each included fiber must contribute a nonempty subset. The count of antecedent subsets is three when a is included, and one when a is omitted, because the a-fiber has $2^2-1=3$ nonempty subsets and the other fibers have one. In particular T={a,b} has the three antecedents {0,2}, {1,2}, {0,1,2}. Summing over all eight T gives $4\cdot3+4\cdot1=16$, exhausting the input subsets.

The preimage map P_f is also neither injective nor onto. It reaches the eight unions of whole attained fibers, so it never reaches {0} alone. Each reached saturated subset has exactly two antecedent target subsets: include or omit the unused label d, which changes no preimage. For example {a,b} and {a,b,d} both have preimage {0,1,2}. These multiplicities concern functions between power sets, rather than inverse functions of f.

### Challenge 4. Monotone endpoints and the number of attained values

**Question.** Count weakly increasing maps from an eight-element chain to a five-element chain with first output 1 and last output 5. Classify them by image size, and count those that are onto.

**Solution.** The endpoint constraints require positive counts for 1 and 5. Subtract one from each: five residual nonnegative counts sum to six. Stars and bars gives $\binom{10}{4}=210$ functions.

For image size k, choose k−2 attained interior labels from {2,3,4}. The k selected multiplicities must all be positive and sum to eight, giving $\binom{7}{k-1}$ vectors. The four image-size counts are therefore
$$k=2:7,\qquad k=3:3\cdot21=63,\qquad k=4:3\cdot35=105,\qquad k=5:35.$$
Their sum $7+63+105+35=210$ verifies the partition. Exactly the last case is onto, so there are 35 onto functions. The endpoints already force two attained labels; using $\binom{5}{k}$ would choose the image without retaining this constraint. Strict increase is impossible from eight inputs to five targets, but weak increase allows the repeated values that make all these counts positive.

### Challenge 5. When an affine rule descends between quotient sets

**Question.** For integers a,b, determine when the rule $[x]_4\mapsto[ax+b]_6$ is well-defined. Classify all distinct induced affine maps for a,b modulo six.

**Solution.** Two representatives of one input class differ by a multiple of four. Their outputs differ by a multiple of 4a. Representative independence is therefore equivalent to $6\mid4a$. Necessity already follows by comparing x and x+4; sufficiency follows by multiplying this divisibility by any integer. Cancelling the greatest common divisor two gives $3\mid a$.

Modulo six the allowed slopes are 0 and 3. With a=0 every input class maps to the constant target [b]_6. With a=3, even representatives map to [b]_6 and odd representatives to [b+3]_6. These are two distinct target classes, each with two input classes in its fiber. For each of six b-values, the constant and two-image maps are different; the twelve choices give twelve distinct functions. The value at [0]_4 distinguishes b and the value at [1]_4 distinguishes the two slopes.

No induced map is onto all six targets, and no such map is injective on all four inputs. A numerical check on the chosen representatives 0,1,2,3 alone cannot establish well-definedness: the forbidden slope a=1 gives different target classes for equivalent representatives 0 and 4. The commuting quotient diagram must respect every representative.

### Challenge 6. Fixed points and transpositions in an involution

**Question.** On eight labelled points, count involutions with exactly two fixed points, and then count all involutions. Distinguish these from permutations with exactly two transpositions.

**Solution.** With exactly two fixed points, six labels move and must form three disjoint pairs. Choose the fixed labels in $\binom{8}{2}=28$ ways. The pairing count on six labels is $6!/(2^3\cdot3!)=15$. The result is $28\cdot15=420$.

For all involutions, let j be the number of transpositions. The count for j is $8!/[2^j j!(8-2j)!]$ for j=0,…,4. These values are 1, 28, 210, 420, 105, summing to 764. The factors remove within-pair order, pair order and irrelevant ordering of the fixed labels. Exactly two transpositions means j=2 and leaves four fixed points, giving 210, not 420.

The squared identity forces every orbit length to divide two, so no omitted longer-cycle cases belong in the sum. On a particular moved pair (u,v), f(u)=v and f(v)=u; reversing the displayed pair does not change either assignment. Fixed points and transpositions are two different counts, linked by the equation $\text{fixed}+2j=8$.

### Challenge 7. Determine the least positive idempotent power

**Question.** On {0,…,6}, let f have output tuple (1,2,2,4,3,4,5). Find the least positive k for which $f^{2k}=f^k$ and describe that power.

**Solution.** One component has 0→1→2→2, so its cycle is the loop at 2. The other has the cycle 3↔4, with 5→4 and 6→5. The largest entry distance is H=2, attained at 0 and 6; the cycle-length least common multiple is L=2. For positive k, idempotence requires k≥2 to reach every cycle and k even to fix both points of the two-cycle on the next k steps. The least value is k=2.

Compute two applications at each input:
$$f^2=(2,2,2,3,4,3,4).$$
Its image is {2,3,4}, and each of these points is fixed by f². Therefore a second application of f² changes nothing, proving the identity directly. The original f is not idempotent: f²(0)=2 while f(0)=1. Its third power is also not idempotent, because on the two-cycle an odd power still exchanges 3 and 4. The even cycle divisibility condition cannot be replaced by the entry-distance bound alone.

### Challenge 8. Cycle structure under powers

**Question.** Count permutations on seven labelled points with one 3-cycle and one 4-cycle. Determine their order, the order of their square, and the number of fixed points of their sixth power.

**Solution.** Choose the three labels for the 3-cycle in $\binom{7}{3}=35$ ways. Their cyclic arrangements number (3−1)!=2. The four remaining labels have (4−1)!=6 cyclic arrangements. Thus the count is $35\cdot2\cdot6=420$. The two cycles have different lengths, so exchanging their displayed order produces no extra factor and no division by two is needed.

The permutation order is lcm(3,4)=12. Squaring a cycle of length ell splits it into gcd(ell,2) cycles of length ell/gcd(ell,2). The 3-cycle remains one 3-cycle; the 4-cycle becomes two 2-cycles. Hence the square has order lcm(3,2)=6, also $12/\gcd(12,2)$.

For the sixth power, 3 divides six, so all three points of the 3-cycle are fixed. Four does not divide six, so none of the four other points is fixed: those points are exchanged in pairs. Exactly three fixed points remain. Counting cycles of a power and counting its fixed points are separate questions; a shorter nontrivial cycle is not a fixed point.

### Challenge 9. Count inner maps whose composite is bijective

**Question.** Fix $g:B\to C$ with |B|=6, |C|=3 and labelled fiber sizes 1,2,3. For a three-element labelled A, count maps $f:A\to B$ making $g\circ f$ bijective. Then repeat with a four-element A, requiring the composite onto.

**Solution.** In the first case each C-value must occur exactly once in the composite. Assign the three C-labels to the three A-inputs in 3!=6 ways. For each assignment choose one g-antecedent in the corresponding fiber, giving $1\cdot2\cdot3=6$ choices. Thus there are $6\cdot6=36$ inner maps. Every such f is injective because its values lie in different disjoint g-fibers. It need not be onto all six B-points.

For four inputs the onto composite has fiber profile (2,1,1). If target j is doubled, there are $4!/2!=12$ placements of its composite labels. Actual B-output choices contribute $r_j^2\prod_{i\ne j}r_i$. Summing the three cases yields
$$12\cdot(1\cdot2\cdot3)(1+2+3)=432.$$
As an independent omission calculation, start with $6^4$ choices of B-values, subtract $(5^4+4^4+3^4)$ for missing a g-fiber, and restore $(1^4+2^4+3^4)$ for using only one fiber. This gives $1296-962+98=432$. The triple intersection is empty. Ordinary onto counts to three equally weighted labels would ignore the different numbers of available B-antecedents.

### Challenge 10. Inverse branches and a restricted real domain

**Question.** Let $f(x)=(x-2)^2+3$. Classify the real-to-real declaration, then find and verify the inverse when the domain is $(-\infty,2]$ and codomain is $[3,\infty)$.

**Solution.** On all reals, f(0)=f(4)=7, so the map is not injective. Its image is [3,∞), so it misses target 2 and is not onto the real codomain. Merely solving its equation with a plus/minus sign gives two potential antecedents, not an inverse function.

On the restricted domain x≤2, the quantity 2−x is nonnegative. If f(u)=f(v), equality of the squares of 2−u and 2−v implies 2−u=2−v and u=v. For every y≥3, the input $2-\sqrt{y-3}$ lies at most at 2 and maps to y. Thus the restricted declaration is bijective, with
$$h(y)=2-\sqrt{y-3},\qquad y\ge3.$$
For x≤2, $\sqrt{(x-2)^2}=|x-2|=2-x$, so h(f(x))=x. For y≥3, substituting h(y) gives f(h(y))=y. The alternative positive branch would lie at least at 2 and generally outside the restricted domain. Domain and codomain determine which algebraic branch is valid; they are part of the inverse theorem, not afterthoughts.
