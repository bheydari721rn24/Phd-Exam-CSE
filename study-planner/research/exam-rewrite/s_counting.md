## Teaching through formulas and conceptual decisions

### Choose the object before the formula

An ordered sample of$r$ distinct objects from$n$ has $n!/(n-r)!$ outcomes. Forgetting order gives $\binom nr$ because every unordered subset has exactly$r!$ orderings. If repetition is allowed, ordered sequences have$n^r$ outcomes, while unordered multisets have $\binom{n+r-1}r$. These are different sample spaces; a uniformly drawn sequence does not induce a uniform law on multisets.

### Allocate with lower and upper bounds

Nonnegative integer solutions of $x_1+\cdots+x_k=N$ number $\binom{N+k-1}{k-1}$. Lower bounds$x_i\ge a_i$ are removed by shifting to$y_i=x_i-a_i$. Upper bounds need exclusion. If every$x_i\le b$, inclusion-exclusion gives

$$\sum_{j=0}^k(-1)^j\binom kj\binom{N-j(b+1)+k-1}{k-1},$$

with a term zero when its adjusted sum is negative. The shift is$b+1$, because violation begins at$b+1$, not$b$.

### Count occupancy and adjacency without duplicating objects

Distributing$n$ distinct objects to$k$ labeled boxes gives$k^n$ assignments. Requiring every box nonempty gives $\sum_{j=0}^k(-1)^j\binom kj(k-j)^n$. For unlabeled nonempty boxes, divide this surjection count by$k!$ because permuting nonempty box labels acts freely. Empty boxes or repeated geometric symmetries can destroy that constant-orbit assumption.

For binary strings of length$n$ with$r$ isolated ones, position the zeros first. They create$n-r+1$ gaps; choose$r$ distinct gaps, giving $\binom{n-r+1}r$. For adjacent specified objects in a permutation, merge them into a block and multiply by internal block order. Dividing by rotations is safe for arrangements of distinct objects, but repeated symbols can create shorter rotational orbits.

## Formula and conceptual problem bank

### Question 1. Ordered without replacement

How many ordered length-three samples of distinct objects can be formed from seven labeled objects?

**A.** 21

**B.** 35

**C.** 210

**D.** 343

**Answer: C.**

There are7 choices for the first object,6 for the second and5 for the third, giving210. The35 count forgets order;343 allows repetition. Each three-element subset has six different orders, so $\binom73\cdot3!=35\cdot6=210$ checks the result.

### Question 2. Multiset permutations

How many different strings can be formed by permuting the letters of BANANA?

**A.** 20

**B.** 60

**C.** 120

**D.** 720

**Answer: B.**

There are six positions, three indistinguishableAs, two indistinguishableNs and oneB. Divide $6!$ by $3!2!$, obtaining60. Dividing by the number of repeated letter types is insufficient; internal permutations within each group generate the same string.720 treats every copy as distinguishable.

### Question 3. Positive allocations

How many positive integer solutions satisfy $x+y+z=10$?

**A.** 28

**B.** 36

**C.** 45

**D.** 66

**Answer: B.**

Shift $u=x-1,v=y-1,w=z-1$ to get nonnegative solutions with sum7. Stars and bars gives $\binom{7+2}2=36$. Using66 counts nonnegative solutions of the original sum and permits zeros. The shift subtracts one from each of three variables, not only once from the total.

### Question 4. Upper bounds

How many nonnegative integer solutions satisfy $x+y+z=7$ with each variable at most3?

**A.** 6

**B.** 12

**C.** 15

**D.** 36

**Answer: A.**

Unrestricted solutions number $\binom92=36$. A violation$x\ge4$ shifts that variable by4 and leaves sum3, giving $\binom52=10$; three variables contribute30. Two simultaneous violations need at least8 and are impossible. Thus the count is $36-30=6$. The bounded generating polynomial gives the same value; the stated upper bound3 excludes values starting at4.

### Question 5. Onto assignments

How many functions from four labeled objects to three labeled boxes use every box?

**A.** 12

**B.** 24

**C.** 36

**D.** 81

**Answer: C.**

Use inclusion-exclusion: $3^4-\binom31 2^4+\binom32 1^4=81-48+3=36$. Alternatively the occupancy must be2,1,1: choose the doubled box in3 ways, its two objects in6 ways, and assign the remaining objects in2 ways, again36. The box labels matter.

### Question 6. Unlabeled nonempty groups

How many partitions of four labeled objects into three nonempty unlabeled groups exist?

**A.** 3

**B.** 6

**C.** 12

**D.** 36

**Answer: B.**

Every partition has one doubleton and two singleton groups. Choose the doubleton in $\binom42=6$ ways. Equivalently divide the36 onto assignments to three labeled boxes by $3!=6$. Because all boxes are nonempty and distinct by their members, each unlabeled partition has exactly six labelings.

### Question 7. No adjacent ones

How many binary strings of length eight contain exactly three ones, no two adjacent?

**A.** 20

**B.** 35

**C.** 56

**D.** 64

**Answer: A.**

There are five zeros and hence six gaps, including both ends. Put one1 in each of three selected gaps, yielding $\binom63=20$. The answer56 chooses arbitrary three positions and permits adjacency. The gap method also proves impossibility when the number of ones exceeds the number of available gaps.

### Question 8. A probability by combinations

A committee of three is drawn uniformly from five women and four men. What is the probability of exactly two women?

**A.** 5/21

**B.** 10/21

**C.** 1/2

**D.** 2/3

**Answer: B.**

The denominator is $\binom93=84$ equally likely committees. Favorable committees number $\binom52\binom41=10\cdot4=40$. The probability is40/84=10/21. Independent sequential selection probabilities require updating the remaining counts; a committee combination count avoids order duplication.

### Question 9. Specified adjacency

Five distinct objects are uniformly permuted. What is the probability that two specified objects are adjacent?

**A.** 1/5

**B.** 2/5

**C.** 1/2

**D.** 4/5

**Answer: B.**

Merge the specified pair into a block, leaving four distinct units with $4!$ orders. The pair has two internal orders, so the favorable count is $2\cdot4!$. Divide by $5!$ to obtain2/5. If the internal order were fixed, the probability would be1/5; the question permits both.

### Question 10. Circular distinct objects

How many circular orders of six distinct objects exist when rotations are identified but reflections remain different?

**A.** 60

**B.** 120

**C.** 360

**D.** 720

**Answer: B.**

Fix one object as an anchor; arrange the other five clockwise, giving $5!=120$. Equivalently every orbit of linear listings has six rotations because all objects are distinct. Identifying reflections as well would divide by another2 and give60, which is not the stated convention.

### Question 11. A guaranteed collision

What smallest number of objects guarantees that some one of seven boxes contains at least four objects?

**A.** 22

**B.** 23

**C.** 28

**D.** 29

**Answer: A.**

Without a four-object box, each box contains at most3, so at most $7\cdot3=21$ objects can be placed. The22nd forces the desired occupancy. The21-object placement with exactly3 per box shows sharpness. Seven times four is sufficient but not the smallest guaranteed count.

### Question 12. Repeated unordered selection

How many multisets of size four can be chosen from three types?

**A.** 12

**B.** 15

**C.** 27

**D.** 81

**Answer: B.**

A multiset is determined by nonnegative type counts summing to4. Stars and bars gives $\binom{4+3-1}{3-1}=\binom62=15$. The81 count is for ordered selections with repetition. Each multiset has a different number of sequence realizations when multiplicities differ, so a uniform sequence does not make these fifteen multisets equally likely.

<!-- CHALLENGE-BANK -->

### Question 13. Challenge: Lower and upper bounds together

How many integer solutions satisfy$x_1+x_2+x_3+x_4=12$ with$1\le x_i\le5$?

**A.** 65

**B.** 80

**C.** 85

**D.** 165

**Answer: C.**

Shift$y_i=x_i-1$ to nonnegative variables summing to8 with upper bound4. Unrestricted count is$\binom{11}3=165$. A violation$y_i\ge5$ leaves sum3 and count$\binom63=20$; there are four possible violating variables. Two violations need sum at least10 and are impossible. Thus165-4(20)=85. Applying upper-bound exclusion before accounting for the lower-bound shift can use the wrong forbidden threshold.

### Question 14. Challenge: Uniform sequences versus multisets

Three independent fair binary digits are sampled. What is the probability that the induced multiset contains two zeros and one one?

**A.** 1/4

**B.** 3/8

**C.** 1/2

**D.** 2/3

**Answer: B.**

There are eight equally likely ordered strings. The desired multiset has three realizations:001,010,100, so probability is3/8. The four possible multisets are not uniformly distributed: the all-zero and all-one multisets each have one realization, while the two mixed multisets each have three. Dividing by the number of multisets therefore changes the sampling law.

## Applicable formulas and examination notes

### 1. Order and replacement

Ordered distinct samples use $n!/(n-r)!$; unordered distinct samples use $\binom nr$; ordered repeated selections use$n^r$. For7 objects and3 distinct picks, these first two counts are210 and35. State the counted object before selecting a formula.

### 2. Identical copies

Fixed multiplicities$n_1,\ldots,n_k$ among$N$ positions give $N!/\prod n_i!$. BANANA gives $6!/(3!2!)=60$. Divide by the factorial of each multiplicity, not merely by the number of repeated letters.

### 3. Positive versus nonnegative

For positive$k$ variables summing to$N$, subtract1 from every variable and use $\binom{N-1}{k-1}$. Nonnegative variables use $\binom{N+k-1}{k-1}$. Inconsistent lower bounds give zero rather than a negative factorial.

### 4. Upper-bound shift

For$x_i\le b$, a bad variable begins at$b+1$. Shift by$b+1$ in inclusion-exclusion. For three variables summing to7 with bound3, unrestricted36 minus three bad counts of10 gives6; two bad variables are impossible.

### 5. Surjections

Onto maps from$n$ labeled objects to$k$ labeled boxes number $\sum_{j=0}^k(-1)^j\binom kj(k-j)^n$. For$n=4,k=3$, the answer is36. Missing a box is an event, and missing-box events overlap.

### 6. Unlabeled boxes

For exactly$k$ nonempty groups of labeled objects, divide the onto count by$k!$. All groups being nonempty ensures each partition has exactly$k!$ labelings. Allowing empty boxes introduces stabilizers and invalidates a blind division.

### 7. Isolated positions

Binary strings with$r$ nonadjacent ones have $\binom{n-r+1}r$ arrangements. There are$n-r+1$ gaps among the zeros. Select distinct gaps; allowing several ones in one gap violates isolation.

### 8. Uniform committees

For$r$ selected from groups of sizes$a,b$, exactly$j$ from the first group has count $\binom aj\binom b{r-j}$ out of $\binom{a+b}r$. The ratio is justified by uniform sampling of subsets, not by an unstated independent model.

### 9. Adjacency blocks

Two specified distinct objects adjacent in$n$ permutations have $2(n-1)!$ favorable orders, probability$2/n$. If their order is fixed, remove the factor2. A chain of overlapping adjacency constraints may not behave like independent blocks.

### 10. Circular symmetry

Distinct objects modulo rotation give $(n-1)!$ orders. Keeping versus identifying reflections is a separate convention. With repeated symbols, rotational orbits can have different sizes, so dividing every linear count by$n$ can fail.

### 11. Pigeonhole threshold

To force at least$r$ objects in one of$k$ boxes, the sharp unrestricted threshold is $k(r-1)+1$. Construct the balanced counterexample with$r-1$ per box to prove that one fewer is insufficient.

### 12. Multisets are not uniform sequence outcomes

Multisets of size$r$ from$k$ types number $\binom{k+r-1}r$. A multiset with counts$n_i$ has $r!/\prod n_i!$ sequence realizations. Different multiplicities yield different induced probabilities when sequences are drawn uniformly.

<!-- BOUNDARY-NOTES -->

### 13. Vandermonde decomposition

$\sum_j\binom aj\binom b{r-j}=\binom{a+b}r$ partitions all $r$-subsets by their first-group count. Terms with inadmissible indices are zero. Restricting the summation to a smaller range counts an additional constraint, not the full identity.

### 14. Weighted subset counts

$\sum_{j=0}^n j\binom nj=n2^{n-1}$ counts a subset with one distinguished included element. A second distinct ordered distinguished element gives $\sum j(j-1)\binom nj=n(n-1)2^{n-2}$. Replacing $j(j-1)$ by $j^2$ requires adding the one-element term.

### 15. Collision probability complement

For $r$ independent uniform choices from $n$ types, no collision has probability $n!/[ (n-r)!n^r]$ when $r\le n$. Collision probability is one minus that value. Independence of choices does not mean the pairwise collision events are independent.
