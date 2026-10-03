## Teaching through formulas and conceptual decisions

### Construct a conservation law from one transition

If a move changes an integer quantity$Q$ by a multiple of$m$, the residue$Q\bmod m$ is preserved. Toggling two bits changes the number of ones by$-2,0$ or2, preserving parity. A target with different parity is impossible; matching parity alone need not prove reachability because there may be additional constraints. A conservation law proves a necessary condition unless sufficiency is independently established.

For a checkerboard domino covering, every tile covers one square of each color. Removing two same-color corners from an8 by8 board leaves unequal color counts and is impossible to tile. Counting total area as even is a weaker invariant that fails to detect this obstruction.

### Choose the exact loop checkpoint

For a prefix-sum loop with checkpoint before processing entry$i$, the invariant is$s=\sum_{j=0}^{i-1}a_j$. The empty prefix gives$s=0$ at$i=0$. Assignment uses old-state values: `s = s + a[i]; i = i + 1;` preserves the relationship because the right-hand prefix grows by exactly the term just added. At exit$i=n$, the invariant turns into the required full sum. A sum invariant alone does not establish termination; a bound on$i$ and a ranking$n-i$ supply that separate proof.

### Count recursive structure through constructors

A full binary tree has either one leaf or an internal root with two full children. If each child satisfies$L=I+1$, the parent satisfies$L=L_1+L_2=(I_1+1)+(I_2+1)=I+1$. For a full$k$-ary tree the same accounting yields$L=(k-1)I+1$. A tree allowing one-child internal nodes does not satisfy this leaf formula; the constructor premise controls the identity.

For exponentiation by squaring, establish the invariant$yb^e=a^n$ for iterative state$y,b,e$. If$e$ is odd, move one factor$b$ into$y$ before halving the remaining exponent; then square$b$. Whether the final unused square is executed affects an exact multiplication count. The proof of the returned value and the count of executed operators are distinct tasks.

## Formula and conceptual problem bank

### Question 1. Parity obstruction

A move toggles exactly two distinct bits in a five-bit word. Starting00000, which target is impossible?

**A.** 11000

**B.** 10100

**C.** 11110

**D.** 01000

**Answer: D.**

The number of ones changes by an even amount under every move, so its parity remains even. The target01000 has one1 and odd parity, making it impossible. Each other target has even parity and is actually reachable here by pairing its set positions into toggles. The invariant excludes the target without enumerating all move sequences.

### Question 2. Checkerboard covering

From an8 by8 board, remove its two diagonally opposite corner squares. Can the remainder be tiled by1 by2 dominoes?

**A.** Yes, because62 is even.

**B.** No, because the color counts differ.

**C.** Yes, because the corners are far apart.

**D.** No, because its area is odd.

**Answer: B.**

Opposite corners of an even-by-even board have the same checkerboard color. Removing both leaves30 squares of that color and32 of the other. Every domino covers exactly one of each, so equality of color counts is necessary and violated. Even remaining area62 is insufficient; D also reports the wrong parity.

### Question 3. Safety without inductiveness

Integer states start at$x=0$ and transition$x\mapsto x+2$. The property$x\ne1$ holds on every reachable state. Why does it fail as an inductive invariant over all integer states?

**A.** It fails initially.

**B.** The state$x=-1$ satisfies it but transitions to1.

**C.** Every reachable state violates it.

**D.** The transition decreases$x$.

**Answer: B.**

The initial state0 satisfies the property, and reachable states are nonnegative even integers. But inductive preservation quantifies over every state satisfying the proposed assertion, including unreachable$-1$. Its successor1 violates the assertion. Strengthening to$x\ge0$ and$x$ even supplies a closed inductive set.

### Question 4. Prefix checkpoint

Before processing index$i$, a loop has summed array entries0 through$i-1$. For$a=[2,5,-1,4]$ and$i=3$, what is the sum variable?

**A.** 5

**B.** 6

**C.** 10

**D.** 11

**Answer: B.**

The processed prefix contains2,5,-1, summing to6. The element at index3 is not yet included. Including4 would give10, the post-processing value. This difference is the exact control-point distinction encoded by the invariant; an array value and the sum of its prefix are different quantities.

### Question 5. Binary-tree identity

A full binary tree has17 internal nodes. How many leaves does it have?

**A.** 16

**B.** 17

**C.** 18

**D.** 34

**Answer: C.**

Full means each internal node has exactly two children. The identity$L=I+1$ gives18 leaves. An edge count verifies it: total edges$2I$ equals total nodes minus1,$I+L-1$, so$L=I+1$. If one-child nodes were permitted, the formula would not follow.

### Question 6. Full ternary tree

A full ternary tree has10 internal nodes. How many leaves are there?

**A.** 11

**B.** 20

**C.** 21

**D.** 30

**Answer: C.**

Every internal node has exactly three children, so$3I=I+L-1$. Rearranging gives$L=2I+1=21$. Thirty counts edges, not leaves. The plus-one originates in the tree identity that edge count is node count minus one.

### Question 7. Structural concatenation

Lists$A,B$ have lengths4 and7. A structurally recursive append copies every node of$A$ and reuses$B$. How many new list nodes are allocated?

**A.** 4

**B.** 7

**C.** 11

**D.** 28

**Answer: A.**

The empty-$A$ base returns$B$ without allocation. Each constructor of$A$ allocates one new node and recurses on its tail, so exactly four new nodes are created. The resulting list length is11, but the seven nodes of$B$ are shared rather than copied. Allocation count follows the implementation contract, not just output length.

### Question 8. Accumulator invariant

An iterative reverse has processed the prefix$[1,2,3]$ and still has$[4,5]$ remaining. What is its front-consing accumulator?

**A.** [1,2,3]

**B.** [3,2,1]

**C.** [5,4]

**D.** [5,4,3,2,1]

**Answer: B.**

Each processed element is pushed to the front, so successive accumulator states are[],[1],[2,1],[3,2,1]. The invariant relates the accumulator to the reverse of the processed prefix, not to the whole input yet. The final complete reverse appears only after the remaining two elements have been processed.

### Question 9. Exponentiation operation count

Recursive powering has bases$p(0)=1,p(1)=a$. For$n>1$, compute$p(\lfloor n/2\rfloor)$ once, square it, and multiply by$a$ if$n$ is odd. How many multiplications compute$p(13)$?

**A.** 3

**B.** 5

**C.** 6

**D.** 7

**Answer: B.**

The nonbase exponents are13,6,3, each contributing one square. Odd13 and3 contribute one additional multiplication each, for$3+2=5$. The base1 returns$a$ without multiplication. With a different base or an iterative implementation performing a final unused square, the exact count changes; those are different algorithms.

### Question 10. Lexicographic ranking

A process decreases$j$ when$j>0$. When$j=0$ and$i>0$, it decreases$i$ and resets$j$ to an arbitrary finite nonnegative value. Both indices are nonnegative. Which ranking proves termination?

**A.** $i+j$

**B.** Lexicographic$(i,j)$ with$i$ primary.

**C.** $j$ only.

**D.** $i-j$

**Answer: B.**

When$j$ decreases, the primary component$i$ stays fixed and the lexicographic pair decreases. On reset,$i$ strictly decreases, so the pair decreases regardless of the new$j$. The sum can increase during reset. Nonnegative lexicographic pairs are well founded, so there is no infinite descent under these rules.

### Question 11. A well-founded codomain

Which quantity alone is insufficient to prove termination even if it strictly decreases and stays positive?

**A.** A positive integer.

**B.** A positive real number.

**C.** A nonnegative integer.

**D.** A finite ordered state rank.

**Answer: B.**

The positive real sequence1,1/2,1/4,... decreases strictly forever without reaching zero. Integer rankings cannot have such an infinite bounded-below descent. Therefore real-valued strict progress needs an extra discrete gap or another termination argument; positivity alone is insufficient.

### Question 12. Finite checking limit

An invariant checker exhaustively validates every input up to size8 for an unbounded algorithm. What conclusion follows?

**A.** The property holds for all sizes.

**B.** The tested instances pass, but an unbounded proof is still required.

**C.** The algorithm must terminate on all inputs.

**D.** Every alternative invariant is false.

**Answer: B.**

Exhaustive testing certifies only the finite domain actually enumerated, assuming the checker itself is correct. A counterexample might first occur at size9 or later. An induction proof or another general argument is needed for unbounded validity. Finite checks are useful error detectors but do not supply missing quantified proof steps.

<!-- CHALLENGE-BANK -->

### Question 13. Challenge: Count a specific iterative powering trace

An iterative power algorithm starts$y=1,b=a,e=13$. While$e>0$, multiply$y$ by$b$ if$e$ is odd, then always square$b$, then set$e=\lfloor e/2\rfloor$. How many multiplications execute?

**A.** 5

**B.** 6

**C.** 7

**D.** 8

**Answer: C.**

The exponent states are13,6,3,1, four iterations. Every iteration squares$b$, contributing four multiplications. Odd states13,3,1 also multiply$y$, adding three. Total7. The last square is executed even though its result is unused after$e$ becomes0. A recursive algorithm stopping at exponent1 can perform only5 multiplications; exact counts depend on the specified control flow, not just the shared mathematical method.

### Question 14. Challenge: A modular linear invariant

States are pairs modulo5. The only move adds$(1,2)$ to a pair. Starting$(0,0)$, which target is unreachable?

**A.** (1,2)

**B.** (2,4)

**C.** (3,4)

**D.** (4,3)

**Answer: C.**

The quantity$2x-y$ modulo5 is invariant because a move changes it by$2-2=0$. The first, second and fourth targets give residue0, and they occur after1,2,4 moves. For(3,4), the residue is2, so it is excluded. Here the reachable orbit has five states and the explicit move construction verifies sufficiency for the other listed targets; invariant agreement alone would not prove sufficiency in a more general system.

## Applicable formulas and examination notes

### 1. Residue invariance

Compute$Q_{next}-Q_{old}$ and show it is divisible by$m$. Toggling two bits preserves one-count parity. A matching residue is only necessary unless a separate construction proves every matching state reachable.

### 2. Color accounting

A domino covers one square of each checkerboard color. Removing two same-color corners leaves30 versus32 squares, ruling out a covering. Even area is a weaker condition and cannot replace the color invariant.

### 3. Reachable versus inductive

A safety property can hold on all reachable states yet fail closure on unreachable states satisfying it. For$x\ne1$ under$x+2$, unreachable$-1$ breaks preservation. Strengthen with parity and nonnegativity instead of assuming reachability during the induction step.

### 4. Invariant obligations

Check initialization, one-step preservation and exit implication separately. Prefix sums use$s=\sum_{j<i}a_j$ at the guard. A property true after the body may not hold before the body, so specify the checkpoint.

### 5. Termination obligation

For a bounded prefix loop, use$n-i$ as a decreasing nonnegative integer. The sum identity proves the result if exit occurs; the ranking proves exit. Total correctness needs both, plus defined memory accesses and arithmetic.

### 6. Assignment old-state meaning

In `x=x+y; y=x-y;`, the second right-hand expression reads the updated$x$, not its original value. For simultaneous mathematical updates, preserve old values explicitly. Incorrect substitution order can destroy a claimed invariant.

### 7. Full-tree count

For full$k$-ary trees,$L=(k-1)I+1$ and edge count is$kI$. Full binary gives$L=I+1$. The constructor requirement excludes unary internal nodes; arbitrary binary trees have different leaf bounds.

### 8. Recursive allocation

Appending a singly linked list by copying its first argument allocates one node per element in that argument and shares the second. Result length and new storage count differ. Complexity depends on the sharing and copying contract.

### 9. Generalized accumulator

Reverse-with-accumulator correctness is$\operatorname{revAcc}(L,A)=\operatorname{concat}(\operatorname{reverse}(L),A)$ under list concatenation. Generalizing to arbitrary$A$ supports the recursive step; proving only the empty-accumulator case can leave an unusably weak induction hypothesis.

### 10. Powering count

With bases0 and1 returning directly, powering$n\ge1$ uses$\lfloor\log_2n\rfloor$ squares and$\operatorname{popcount}(n)-1$ extra multiplications.13 therefore costs5. Other base and final-square conventions change exact counts while preserving asymptotic logarithmic depth.

### 11. Lexicographic descent

Nonnegative pair$(i,j)$ with$i$ primary decreases when$j$ drops or$i$ drops with arbitrary finite reset of$j$. The sum need not decrease. The ranking codomain and ordering are essential parts of the argument.

### 12. Testing boundary

Finite exhaustive checks establish the enumerated cases and can expose errors in a proof. They do not justify an all-input induction step or certify unbounded numerical stability. Record the exact tested domain beside the result.

<!-- BOUNDARY-NOTES -->

### 13. Permutation parity

A transposition changes permutation parity; a product of two transpositions preserves it. For a sliding puzzle, include the blank's permitted motion and board width in the invariant rather than using tile permutation parity alone. A physical move and an arbitrary label swap are different operations.

### 14. Mutual recursion

Use a joint specification for mutually recursive functions and a measure decreasing across every call edge. Decrease on only one of the functions' recursive paths is insufficient. A same-size cross-call can require an additional phase component in a lexicographic measure.

### 15. Fairness is not a ranking

An invariant can prove safety without showing a desired action eventually occurs. A nondeterministic scheduler may keep choosing an unproductive permitted transition unless a fairness assumption is stated. Distinguish termination, deadlock freedom and eventual progress.
