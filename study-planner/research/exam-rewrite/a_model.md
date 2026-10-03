## Teaching through formulas and conceptual decisions

### Translate the representation into a numerical input length

For a positive integer $N$, unsigned binary length is $L=\lfloor\log_2N\rfloor+1$. Therefore $2^{L-1}\le N<2^L$. A loop running $N$ times can take exponentially many steps in $L$, even though it is linear in the numeric value. Unary encoding instead has length proportional to $N$; the same loop then has linear complexity in its input length. Pseudo-polynomial complexity is a statement about this mismatch, not a statement that every numeric loop is slow.

If an array contains $n$ values each represented in $b$ bits, payload length is $nb$ bits. Reading a value is constant time only in a model where it fits in a word and that word is an accessible primitive. Reading an arbitrarily long integer is not a constant-time primitive in a bit model. Multiplying two $b$-bit integers by the ordinary digit algorithm performs quadratic bit work, even though a language presents multiplication as one expression.

### Separate addressability, payload and operation support

A memory with $M$ individually addressable positions needs at least $\lceil\log_2M\rceil$ address bits. Representing every integer from0 through$M$ needs $\lceil\log_2(M+1)\rceil$ value bits, which can differ at a power of two. Neither statement grants constant-cost arithmetic on an object occupying many words. A word-RAM assumption specifies a word width, allowed operations and memory access costs together.

### Derive information and output lower bounds

A binary comparison decision tree of height $h$ has at most $2^h$ leaves. Distinguishing $K$ possible outcomes requires $h\ge\lceil\log_2K\rceil$. Sorting distinct labeled keys requires $K=n!$, but selecting one of$n$ possible positions uses a different outcome count. An explicit output of$m$ words costs at least proportional to$m$ writes. Returning a pointer to an already stored object does not write the object again; output representation changes the lower-bound argument.

## Formula and conceptual problem bank

### Question 1. A power-of-two boundary

How many bits represent the positive integer1024 in ordinary unsigned binary without leading zeros?

**A.** 9

**B.** 10

**C.** 11

**D.** 1024

**Answer: C.**

The highest set bit represents $2^{10}$, and its position counts from zero. The representation has that bit plus ten lower positions, hence11 bits. The floor-log formula gives $\lfloor\log_2 1024\rfloor+1=11$. Ten bits represent at most1023. The address space of1024 positions is a different question and needs ten address bits.

### Question 2. Address versus length

A memory has1024 positions indexed0 through1023. Which pair gives the minimum index bits and the bits needed to store its length1024?

**A.** (10,10)

**B.** (10,11)

**C.** (11,10)

**D.** (11,11)

**Answer: B.**

The1024 possible indices fit in ten bits. The length is the numeric value1024 and needs eleven bits. The two quantities differ precisely because the length lies one above the largest index. Assigning the same bit count to both confuses number of available values with the largest represented value.

### Question 3. Binary numeric iteration

An algorithm performs exactly $N$ constant-cost iterations on a positive $L$-bit integer $N$. Its worst-case count as a function of $L$ is which?

**A.** $\Theta(L)$

**B.** $\Theta(L^2)$

**C.** $\Theta(2^L)$

**D.** $\Theta(\log L)$

**Answer: C.**

The greatest $L$-bit value is $2^L-1$, and the least is $2^{L-1}$. Thus even the minimum for that length is exponential in $L$. Counting iterations gives tight order $2^L$. This classification assumes the problem grants constant-cost loop operations; adding bit-cost arithmetic cannot make it linear in $L$.

### Question 4. Array payload

An array has200 signed values stored in fixed16-bit slots. Ignore headers and padding. What is its payload in bytes?

**A.** 200

**B.** 400

**C.** 1600

**D.** 3200

**Answer: B.**

The payload is $200\cdot16=3200$ bits. Divide by eight bits per byte to obtain400 bytes. Choice3200 reports bits as bytes. Choice200 assumes one byte per value. The calculation counts physical fixed-width storage, not the number of decimal digits printed for each value.

### Question 5. Matrix input parameter

For an $n\times n$ matrix of fixed-width entries, scanning every entry once takes what order in the number $M$ of entries?

**A.** $\Theta(\sqrt M)$

**B.** $\Theta(M)$

**C.** $\Theta(M^2)$

**D.** $\Theta(\log M)$

**Answer: B.**

There are $M=n^2$ entries and one visit per entry, giving $\Theta(n^2)=\Theta(M)$. A quadratic statement in the side length is linear in the entry count. ChoiceC substitutes $M$ for $n$ without translating the parameter definition. Complexity labels are meaningless unless the input-size variable is defined.

### Question 6. Bit-cost multiplication

The ordinary schoolbook method multiplies two $b$-bit integers. Under a bit-operation model, what is its asymptotic worst-case work?

**A.** $\Theta(1)$

**B.** $\Theta(b)$

**C.** $\Theta(b^2)$

**D.** $\Theta(2^b)$

**Answer: C.**

Each of$b$ multiplier bits contributes a shifted partial product involving up to$b$ multiplicand bits. Ordinary accumulation also fits within quadratic bit work, yielding $\Theta(b^2)$ for this method. A source-level multiplication operator is not a constant-time bit primitive. Faster multiplication algorithms change the algorithm; they do not change this schoolbook count.

### Question 7. Decision-tree capacity

A binary comparison tree must distinguish70 possible answers. What minimum worst-case depth follows solely from leaf capacity?

**A.** 6

**B.** 7

**C.** 35

**D.** 70

**Answer: B.**

Six levels provide at most64 leaves, insufficient for70 distinguishable answers. Seven levels provide128, so the necessary lower bound is $\lceil\log_2 70\rceil=7$. Capacity alone does not construct an algorithm attaining it under every comparison restriction. The linear options mistake one outcome per comparison for exponential branching.

### Question 8. Sorting a small distinct input

What comparison lower bound follows for sorting five distinct keys?

**A.** 5

**B.** 6

**C.** 7

**D.** 10

**Answer: C.**

There are $5!=120$ possible relative orders. A binary comparison tree needs at least120 leaves, so its height is at least $\lceil\log_2 120\rceil=7$. Six levels distinguish only64 orders. Ten is the number of unordered key pairs, which is not the information-theoretic lower bound and need not all be compared.

### Question 9. Sparse versus dense reading

A simple graph has $n$ vertices and $m$ edges. Ignoring vertex-label bit lengths, which pair describes scanning an adjacency matrix and adjacency lists respectively?

**A.** $\Theta(n),\Theta(m)$

**B.** $\Theta(n^2),\Theta(n+m)$

**C.** $\Theta(m),\Theta(n^2)$

**D.** $\Theta(n+m),\Theta(nm)$

**Answer: B.**

The matrix stores $n^2$ cells whether edges exist or not. Lists require visiting$n$ list headers and a total proportional to$m$ edge entries, twice$m$ for an undirected graph. That constant does not change the order. The vertex-header cost matters even for an edgeless graph, so $\Theta(m)$ alone is incomplete.

### Question 10. Explicit output size

An algorithm emits all ordered pairs of distinct elements from an $n$-element input, each pair as an explicit constant-size record. What worst-case output lower bound follows?

**A.** $\Omega(n)$

**B.** $\Omega(n\log n)$

**C.** $\Omega(n^2)$

**D.** $\Omega(\log n)$

**Answer: C.**

There are $n(n-1)$ ordered pairs. Each record requires at least one fixed-cost emission under the stated model, so the output alone imposes $\Omega(n^2)$ for $n\ge2$. If pairs were represented implicitly by a generator, this lower bound would apply to fully consuming the generator, not constructing its handle. The explicit-output premise is essential.

<!-- CHALLENGE-BANK -->

### Question 11. Challenge: Growing arithmetic objects

Begin with integer$x=2$ and square it six times exactly. How many bits are needed for the final positive integer?

**A.** 6

**B.** 32

**C.** 64

**D.** 65

**Answer: D.**

After$k$ squarings,$x=2^{2^k}$. At$k=6$, the final value is$2^{64}$, whose unsigned representation needs65 bits because the top bit is position64. Six source-level multiplications do not imply six constant-time word operations on a64-bit machine; the final value already exceeds its unsigned maximum. This separates operation count, operand growth and representability.

### Question 12. Challenge: Capacity measured in input bits

A table allocates$100W$ fixed-size cells for a binary-encoded20-bit positive capacity$W$. What largest cell count is possible?

**A.** 2000

**B.** 1048575

**C.** 104857500

**D.** 104857600

**Answer: C.**

The greatest20-bit value is$2^{20}-1=1048575$. Multiplying by100 gives104857500 cells. The20-bit encoding length does not mean the capacity is20. Using$2^{20}$ instead would choose a value needing21 bits. Allocation is pseudo-polynomial in numeric$W$ and can be exponential in its length even before the cells are initialized.

## Applicable formulas and examination notes

### 1. Binary length

For $N\ge1$, use $\lfloor\log_2N\rfloor+1$. At powers of two, include the leading bit:1024 needs11 bits. Zero requires a separately specified encoding convention, so do not apply the logarithm formula to zero.

### 2. Address range

$M$ indexed positions0 through$M-1$ need $\lceil\log_2M\rceil$ address bits. A stored count ranging0 through$M$ needs $\lceil\log_2(M+1)\rceil$. The distinction appears at powers of two and often supplies an off-by-one distractor.

### 3. Numeric versus encoded time

If $N$ has $L$ binary bits, a count proportional to$N$ is $\Theta(2^L)$ in the worst case for fixed length. A unary representation has length $\Theta(N)$ instead. Always identify the encoding before classifying a numeric bound as polynomial.

### 4. Payload accounting

$n$ fixed$b$-bit values occupy $nb$ bits before overhead. For20016-bit values, this is400 bytes. Word alignment, headers and padding must be included only when specified; printed numeric magnitude is not storage width.

### 5. Bit versus word arithmetic

Ordinary multiplication of two$b$-bit values costs $\Theta(b^2)$ bit operations. In a word model, multiplication of values fitting supported words may count as one primitive. Unbounded integers spanning multiple words invalidate that shortcut.

### 6. Matrix parameter conversion

For side length$n$, entry count is $M=n^2$. A full scan is quadratic in$n$ and linear in$M$. Translate the function when changing parameters instead of carrying its old exponent to the new variable.

### 7. Comparison leaf bound

Binary comparisons require $h\ge\lceil\log_2K\rceil$ for$K$ distinguishable outputs. Sorting distinct keys uses $K=n!$; an arbitrary query may use a smaller outcome space. A leaf-count lower bound need not be achievable by every allowed comparison family.

### 8. Representation-specific graph reading

Adjacency matrices have $\Theta(n^2)$ cells; adjacency lists have $\Theta(n+m)$ words with fixed labels. Even if$m=0$, reading all vertex headers costs linear time. The same graph does not force the same input length under both representations.

### 9. Output lower bounds

Explicitly emitting$n(n-1)$ constant-size pairs costs $\Omega(n^2)$. An implicit pointer or lazy iterator is a different output contract. Compare algorithms only after making their output obligations identical.

### 10. An adversarial unseen position

To determine whether an arbitrary unsorted array contains a designated value, a negative answer may require reading all$n$ positions: an unread position could contain it. This proves a linear worst-case access bound, while a positive answer can finish earlier.

<!-- BOUNDARY-NOTES -->

### 11. Instance, best and worst costs

Worst-case cost at size $n$ is a maximum over all admissible instances of that size, while best-case cost is a minimum. An expected cost additionally needs a stated distribution or random algorithm. A measured favorable input is not evidence of a uniform worst-case bound.

### 12. Array interface versus implementation

Constant-time indexed access does not make insertion at an arbitrary position constant time. A contiguous implementation may shift a linear suffix. Allocation, initialization and copying are separate costs, even when a language expresses them as one operation.

### 13. Pseudo-polynomial capacity

A table with $nW$ entries is polynomial in numeric capacity $W$, but $W$ can be exponential in its binary length. If $W$ uses $L$ bits, the table can have order $n2^L$ entries. The encoding and numeric range determine whether the polynomial claim is appropriate.
