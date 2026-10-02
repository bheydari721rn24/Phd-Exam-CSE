# Computation Models and Input Size

*Data Structures and Algorithms · Chapter 1 · student-approved English edition · 16 fully worked problems*

## 1. Boundary, prerequisites, and reviewed sources

An algorithmic claim has meaning only after we say what the input is, how it is represented, which operations are allowed, and what resources are charged. This chapter builds those choices from first principles. It distinguishes an abstract problem from an algorithm and an implementation; defines bit length, word count, and natural structural parameters; develops a precise word-RAM convention; contrasts bit-cost and comparison models; and derives conditional input and output lower bounds. The later chapters on asymptotic notation and loop analysis will formalize growth classes and count complicated execution paths. Here, small operation counts are used only to clarify the model.

Prerequisites are integers, logarithms, arrays, basic set/function language, and mathematical induction. Five *written* university course texts were read for the relevant portions: MIT 6.006 Lecture 1 and Recitation 1; CMU 15-451 Lecture 3; Princeton's algorithm-analysis slides by Kevin Wayne; Stanford CS161 Lecture 1; and Berkeley CS170's knapsack lecture. They contribute different checks: MIT provides the problem and machine definitions; CMU tests word-size assumptions; Princeton contrasts machines and resources; Stanford motivates digit length; Berkeley exposes the numeric-value versus encoding-length trap. The project's source audit records exact links, pages, comparisons, and limits. The examples below are independently written, including those inspired by a course's *reasoning type*.

## 2. Four distinct objects: problem, instance, algorithm, and program

A **computational problem** specifies which outputs are correct for each admissible input. Formally, for an input domain <span class="math-inline">X</span> and output domain <span class="math-inline">Y</span>, a relation <span class="math-inline">R ⊆ X × Y</span> defines the problem: <span class="math-inline">(x,y) ∈ R</span> means <span class="math-inline">y</span> is an acceptable answer for input <span class="math-inline">x</span>. If exactly one output is allowed per input, the problem is a function. If several answers are allowed, it is a search relation. For example, “return any pair of equal keys, or report that no pair exists” can allow several correct pairs.

An **instance** is one particular input <span class="math-inline">x</span>. An **algorithm** is a finite description of a procedure that, for every admissible instance, terminates and returns an allowed answer. A deterministic algorithm chooses one output for each input, even if the relation permits many. A **program** implements the algorithm in a language and on a platform. The same abstract algorithm can be implemented with different data structures; changing a data structure may change its actual operation count. A benchmark measures one program on selected instances and hardware. It cannot, by itself, prove a worst-case statement about every possible input.

The problem statement must state exceptional inputs. Does an empty array count? If no requested element exists, is the answer a sentinel or an error? Are keys distinct? Is arithmetic exact or modular? Are graph vertices labeled <span class="math-inline">0,…,V−1</span>? Without these choices, “correct” is underspecified. A cost analysis should begin with a contract:

<div class="formula-block">Input domain → valid output relation → representation → charged operations → resource bound.</div>

The arrows show a dependency, not a theorem: later claims depend on the earlier choices. In particular, two algorithms solving the same abstract problem may receive inputs in different representations. Their resource functions cannot be compared fairly until conversion costs and available preprocessing are specified.

## 3. What is the size of an input?

### 3.1 Encoding length is the fundamental measure

Computers receive finite encodings. If <span class="math-inline">enc(x)</span> is a binary string representing instance <span class="math-inline">x</span>, its **bit length** is <span class="math-inline">N = |enc(x)|</span>. Any statement that an algorithm is “polynomial in its input length” must ultimately refer to a comparable encoding measure. A reasonable encoding is unambiguous, decodable, and does not conceal an enormous object in a symbol whose storage is declared free. Including or omitting a fixed-size header changes length by a constant; changing binary integers to unary can change it by an exponential factor.

For a nonnegative integer <span class="math-inline">U</span> in ordinary binary without leading zeros,

<div class="formula-block"><span class="math-inline">bitlen(U) = 1</span> if <span class="math-inline">U = 0</span>; otherwise <span class="math-inline">bitlen(U) = ⌊log₂ U⌋ + 1</span>.</div>

Proof: for <span class="math-inline">U ≥ 1</span>, the highest nonzero bit has index <span class="math-inline">k = ⌊log₂ U⌋</span>, since <span class="math-inline">2<sup>k</sup> ≤ U &lt; 2<sup>k+1</sup></span>. Its positions are <span class="math-inline">0,…,k</span>, so there are <span class="math-inline">k+1</span> bits. Thus a capacity <span class="math-inline">U = 2<sup>m</sup></span> has only <span class="math-inline">m+1</span> bits. An algorithm taking time proportional to <span class="math-inline">U</span> can take exponentially many steps relative to the number of bits describing this *one* number.

An array of <span class="math-inline">n</span> fixed-width <span class="math-inline">w</span>-bit elements occupies <span class="math-inline">nw</span> data bits, plus any length/format metadata. If <span class="math-inline">w</span> is fixed independently of <span class="math-inline">n</span>, bit length and element count are proportional. If values can grow with <span class="math-inline">n</span>, the total bit length may instead be <span class="math-inline">Θ(n log n)</span> or larger. For variable-length fields, a parser also needs boundaries, such as length prefixes or delimiters; writing simply “the sum of all value lengths” assumes a framing convention. A useful explicit accounting is

<div class="formula-block"><span class="math-inline">N = L<sub>header</sub> + </span><math class="math-limits" display="inline" aria-label="sum from i equals 1 to n"><munderover><mo largeop="true">∑</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover></math><span class="math-inline">(L<sub>delimiter,i</sub> + bitlen(a<sub>i</sub>))</span>.</div>

The displayed sum is an accounting identity under a chosen serialization; it is not a claim that every encoding has the same header or delimiter lengths.

### 3.2 Structural parameters are useful but must be defined

Algorithm courses often write <span class="math-inline">n</span> for the number of array elements, <span class="math-inline">V</span> and <span class="math-inline">E</span> for vertices and edges, or <span class="math-inline">r,c</span> for matrix dimensions. These are **parameters** of the instance, not automatic synonyms for its bit length. For a dense <span class="math-inline">r × c</span> matrix of fixed-width numbers, there are <span class="math-inline">rc</span> entries and <span class="math-inline">Θ(rcw)</span> data bits. A scan of an <span class="math-inline">n × n</span> matrix reads <span class="math-inline">n²</span> entries; saying that the input has size <span class="math-inline">n</span> would silently discard a square factor.

An adjacency-list graph with <span class="math-inline">V</span> vertex records and <span class="math-inline">E</span> stored directed-edge records needs <span class="math-inline">Θ(V+E)</span> *word cells* when each identifier fits in one word and standard list metadata is included. An adjacency matrix has <span class="math-inline">V²</span> Boolean entries. Packed bits can occupy <span class="math-inline">Θ(V²)</span> bits; a simple one-word-per-entry implementation occupies <span class="math-inline">Θ(V²)</span> words. A graph with <span class="math-inline">V=1000, E=1500</span> therefore has different storage and scan costs under these two encodings. The graph itself is neither “an input of size <span class="math-inline">V</span>” nor automatically “an input of size <span class="math-inline">V²</span>.”

### 3.3 A diagram of the accounting layers

<figure class="logic-diagram model-diagram"><svg viewBox="0 0 900 320" role="img" aria-label="Input representation passes from abstract instance to encoded bits to machine words and charged operations"><defs><marker id="model-arrow" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="#426f8a"/></marker></defs><rect x="25" y="34" width="180" height="76" rx="10" fill="#edf3fa" stroke="#829db2"/><text x="45" y="67" font-size="19">Abstract instance</text><text x="45" y="91" font-size="15">array, graph, integer</text><rect x="256" y="34" width="180" height="76" rx="10" fill="#f0f5e9" stroke="#9aac88"/><text x="277" y="67" font-size="19">Encoding</text><text x="277" y="91" font-size="15">N bits</text><rect x="487" y="34" width="180" height="76" rx="10" fill="#fcf2e9" stroke="#c0a485"/><text x="508" y="67" font-size="19">Machine storage</text><text x="508" y="91" font-size="15">words of w bits</text><rect x="718" y="34" width="160" height="76" rx="10" fill="#f3edf9" stroke="#a894bb"/><text x="736" y="67" font-size="19">Execution</text><text x="736" y="91" font-size="15">charged steps</text><path d="M208 72 H248" stroke="#426f8a" stroke-width="2.6" marker-end="url(#model-arrow)"/><path d="M439 72 H479" stroke="#426f8a" stroke-width="2.6" marker-end="url(#model-arrow)"/><path d="M670 72 H710" stroke="#426f8a" stroke-width="2.6" marker-end="url(#model-arrow)"/><text x="35" y="167" font-size="18">Example: n values with b-bit entries</text><text x="35" y="199" font-size="17">Data: n·b bits</text><text x="35" y="231" font-size="17">Aligned storage: n·ceil(b/w) words</text><text x="35" y="263" font-size="17">Scan: n reads if each value occupies one word</text><text x="35" y="295" font-size="16">Costs depend on encoding and permitted operations.</text></svg><figcaption>The arrows distinguish information size, storage layout, and execution cost. The diagram scrolls horizontally on narrow screens. A bit or multiword value cannot always be processed in one step.</figcaption></figure>

### 3.4 Changing the encoding can change the complexity claim

Binary and unary representations of an integer <span class="math-inline">U</span> have radically different lengths: binary uses <span class="math-inline">bitlen(U)</span> bits, whereas the unary string consisting of <span class="math-inline">U</span> copies of `1` uses <span class="math-inline">U</span> symbols. A method with <span class="math-inline">U</span> steps is linear in the unary input length but can be exponential in the binary input length. This is why a statement such as “the algorithm is polynomial” must name the encoding. Standard complexity analyses of ordinary numerical inputs normally assume binary or another positional encoding with comparable length; silently switching to unary can manufacture a misleading efficiency claim. The parser and representation conversion are part of the computation when inputs arrive in a different format.

## 4. A precise word-RAM model

### 4.1 Words, addresses, and primitive steps

Fix a machine word width <span class="math-inline">w</span> bits. Memory consists of addressable words; a word stores one unsigned integer in <span class="math-inline">{0,…,2<sup>w</sup>−1}</span>, or another bit pattern with a stated interpretation. A primitive step operates on a constant number of words. The conventional instruction set includes word-sized addition, subtraction, comparison, bitwise Boolean operations, conditional branching, and access to an addressed memory word. Courses sometimes also permit word multiplication and division in one step; this chapter will **state explicitly** when relying on either. Overflow, signedness, and shifts are not automatically exact unbounded-integer arithmetic.

To address <span class="math-inline">n</span> distinct word cells numbered <span class="math-inline">0,…,n−1</span> with a single word, there must be at least <span class="math-inline">n</span> distinct bit patterns: <span class="math-inline">2<sup>w</sup> ≥ n</span>, equivalently <span class="math-inline">w ≥ ⌈log₂ n⌉</span> for <span class="math-inline">n ≥ 2</span>. Storing the **value** <span class="math-inline">n</span> in one unsigned word is a slightly stronger requirement, <span class="math-inline">2<sup>w</sup> ≥ n+1</span>. For a program that allocates more than <span class="math-inline">n</span> cells, the width must cover its highest address, not just the initial input. An often useful idealization is <span class="math-inline">w = Θ(log N)</span> for input bit length <span class="math-inline">N</span>, with the explicit assumption that all word-sized keys and allocated addresses fit. A physical computer instead has a fixed word width and a finite address space; asymptotic analysis describes a family of sufficiently sized ideal machines.

The running time <span class="math-inline">T(x)</span> counts executed primitive steps on a particular input <span class="math-inline">x</span>. For a size function <span class="math-inline">s(x)</span>, the worst-case function is

<div class="formula-block formula-steps"><div><span class="math-inline">T<sub>worst</sub>(n) = max{T(x) :</span></div><div><span class="math-inline">x admissible, s(x)=n}</span></div></div>

This definition assumes that the maximum exists.

If there are no instances of exactly size <span class="math-inline">n</span>, leave that exact-size value undefined or declare a separate convention. A cumulative definition over <span class="math-inline">s(x) ≤ n</span> is another option when that family is nonempty. A supremum replaces a maximum when a nonempty family has no attained largest runtime; an unbounded supremum can be infinite. It does not automatically assign a meaningful nonnegative runtime to an empty family. Best-case time uses a minimum and does not establish performance on difficult inputs. Average-case time requires a probability distribution over instances; it cannot be inferred from “typical” intuition alone. Space can count peak extra cells, total cells including input, or bits. Always name the convention. A procedure using <span class="math-inline">n</span> extra machine words consumes <span class="math-inline">nw</span> bits of payload before allocator overhead.

### 4.2 Array access, allocation, and the interface/implementation distinction

For a static contiguous array of <span class="math-inline">n</span> one-word elements, a valid indexed read or write has constant primitive-step cost: compute base-plus-index and access the resulting address, assuming the arithmetic and address fit in words. That does **not** imply construction of an initialized array is constant time. If every one of <span class="math-inline">n</span> cells must become zero, there are <span class="math-inline">n</span> writes (or an equivalent bulk operation whose cost must be charged). Similarly, reading a single given entry is different from reading every entry.

An abstract **interface** says which operations an object supports; a **data structure** implements them. A static-array interface may provide `get_at(i)` and `set_at(i,x)` for legal indices. A dynamic array adds a changing length and may occasionally reallocate, so the cost of `append` needs another analysis. A linked list also provides a sequence but does not thereby gain constant-time access to its <span class="math-inline">i</span>-th element. The operation name alone is never a cost proof.

### 4.3 Why unbounded integers break the shortcut

Suppose <span class="math-inline">n</span> positive <span class="math-inline">w</span>-bit integers are multiplied exactly. Their product can require close to <span class="math-inline">nw</span> bits. For example, multiplying <span class="math-inline">n</span> copies of <span class="math-inline">2<sup>w−1</sup></span> gives <span class="math-inline">2<sup>n(w−1)</sup></span>, whose binary representation has <span class="math-inline">n(w−1)+1</span> bits. Once the intermediate result spans more than one word, a multiplication of it by another factor is **not** the primitive multiplication of two words. A loop with <span class="math-inline">n−1</span> source-level multiplication statements therefore does not prove <span class="math-inline">Θ(n)</span> word-RAM time for exact big-integer arithmetic. Merely emitting the output requires enough words to hold it.

One could instead stipulate **modular word arithmetic**, in which every product is reduced modulo <span class="math-inline">2<sup>w</sup></span>; then each word multiplication can be constant time, but the computed function differs from exact integer multiplication. An **unbounded unit-cost RAM** declares arithmetic on arbitrary-size integers constant time. That model is mathematically definable but can undercharge enormous values. A **bit-cost model** counts operations on bits or charges multiword arithmetic according to operand lengths. No model is automatically “the real computer”; choose one that preserves the distinctions needed for the claim.

## 5. Restricted models and why lower bounds depend on them

In the **comparison model**, the algorithm may learn about opaque keys only by comparing them; a comparison provides an outcome such as less/equal/greater. The model is appropriate when keys have no usable structure beyond order. A word-RAM algorithm for bounded integer keys can additionally use the key as an array index, perform arithmetic, and inspect bits. It may therefore answer some questions using operations unavailable to a comparison algorithm. A lower bound proved for comparisons cannot be transferred to every word-RAM algorithm merely because both manipulate an array.

Consider repeated membership queries for keys from <span class="math-inline">{0,…,U−1}</span>. A direct-address Boolean table supports a query with one indexed read after preprocessing, but it allocates <span class="math-inline">U</span> entries and must establish their initial state. Calling the query “constant time” without charging preprocessing and space is incomplete. If <span class="math-inline">U</span> is exponentially larger than the number of stored keys, direct addressing may be a poor total-resource choice. In a comparison-only setting, that same array-index operation is disallowed because an opaque key cannot be interpreted as an address.

Here is a small decision-tree argument. Let <span class="math-inline">b≥2</span> and <span class="math-inline">q≥1</span> be integers. Suppose a comparison-based procedure must distinguish <span class="math-inline">q</span> possible answers and each charged comparison has at most <span class="math-inline">b</span> possible outcomes. A depth-<span class="math-inline">d</span> decision tree has at most <span class="math-inline">b<sup>d</sup></span> leaves, so correctness requires <span class="math-inline">b<sup>d</sup> ≥ q</span>, or <span class="math-inline">d ≥ ⌈log<sub>b</sub> q⌉</span>. For yes/no tests, <span class="math-inline">b=2</span>; for an order comparison with less/equal/greater, <span class="math-inline">b≤3</span>. This is a lower bound only if the answers really require distinguishable leaves and the model has no other way to obtain the relevant information. It says nothing about an algorithm allowed to address memory with integer keys. A full sorting lower bound is deferred to the sorting chapter.

A lower bound also depends on **how input arrives**. For an unsummarized random-access array, a read-all argument works if one admissible input has the following property: changing any one still-unread entry, while leaving the others unchanged, can change the required answer. A deterministic correct algorithm must read every entry on that input to exclude the indistinguishable alternative. Merely saying that every coordinate can matter on some input is weaker and is not this adversary proof. A stream has another access restriction: reaching a late entry may itself require consuming its prefix. When a sorted array is already resident in random-access memory, locating a query need not read every position; when a precomputed summary accompanies the data, an answer may be even quicker. State the interface and preprocessing cost before invoking a “must read the input” argument.

## 6. Numeric parameters and pseudo-polynomial behavior

Suppose an algorithm creates one state for each integer capacity <span class="math-inline">0,…,U</span> and spends a constant number of word operations per state. Its state count is <span class="math-inline">U+1</span>, and its running time is at least proportional to that count. If <span class="math-inline">U=2<sup>m</sup></span>, the capacity itself has <span class="math-inline">m+1</span> binary digits, while the table has <span class="math-inline">2<sup>m</sup>+1</span> states. Thus “polynomial in <span class="math-inline">U</span>” is not equivalent to “polynomial in the number of bits used to describe <span class="math-inline">U</span>.” An algorithm polynomial in the numerical values of its numeric inputs and the number of items, but not necessarily in the binary encoding length, is called **pseudo-polynomial**.

For a knapsack-style input with <span class="math-inline">n</span> weights each at most <span class="math-inline">U</span> and a capacity <span class="math-inline">U</span>, a straightforward fixed-width encoding has <span class="math-inline">O(n log(U+1) + log(n+1))</span> bits for these fields, ignoring additional values and fixed framing. A table with <span class="math-inline">n(U+1)</span> states can grow exponentially in <span class="math-inline">log U</span>. This observation does **not** prove that every algorithm for the problem is slow; it classifies the specified table-based method. Nor does it say that an instance with <span class="math-inline">U</span> near <span class="math-inline">n</span> is impractical: the relationship among parameters matters.

## 7. Conditional lower bounds from information access and output

An input-access lower bound requires an adversarial argument, not a slogan. Suppose the task asks whether **every** bit in an unsummarized <span class="math-inline">n</span>-bit array is zero. If a deterministic algorithm stops without reading position <span class="math-inline">j</span> after seeing zeros elsewhere, two inputs remain indistinguishable to it: the all-zero array and the same array with bit <span class="math-inline">j</span> changed to one. The required outputs differ, so the algorithm cannot be correct on both. On the all-zero input it must inspect all <span class="math-inline">n</span> bits. If the machine reads <span class="math-inline">w</span> packed bits per word, the same argument gives at least <span class="math-inline">⌈n/w⌉</span> word reads, not necessarily <span class="math-inline">n</span> reads. The granularity of one charged operation matters.

An output lower bound is equally conditional. If an algorithm must explicitly write <span class="math-inline">k</span> separate output words, and each primitive output step writes at most one word, it needs at least <span class="math-inline">k</span> output steps. Returning a pointer to an already materialized <span class="math-inline">k</span>-word object can be constant time **only if** the specification accepts that pointer and construction of the object is charged elsewhere. A compressed output changes the task. These conditions prevent applying an output-size bound to an interface that asks only for an implicit description.

## 8. Fully worked problems

Every problem below is original or independently worded from a reasoning type in the selected courses. The point is to make the choice of size measure and cost model explicit before any calculation.

### Problem 1 — Several correct outputs versus one algorithmic output

**Question.** An input array is <span class="math-inline">[7,4,7,4]</span>. The specification says “return two distinct zero-based indices i and j with i&lt;j and equal array values.” How many outputs are allowed, and can a deterministic algorithm still be a function?

**Solution.** With zero-based positions, the two valid index pairs are <span class="math-inline">(0,2)</span> and <span class="math-inline">(1,3)</span>. The problem relation contains both pairs for this input. A deterministic algorithm can choose a rule, such as the lexicographically first pair, and return only <span class="math-inline">(0,2)</span>. Its mapping from this input to one output is a function and still solves the relation. An answer “there are two answers, so no deterministic algorithm exists” confuses the problem's permitted outputs with one procedure's choice. If the task instead demands *all* pairs, the output specification changes.

### Problem 2 — Exact binary length at boundaries

**Question.** Find the binary lengths of <span class="math-inline">0,1,15,16,17,2<sup>m</sup>−1,2<sup>m</sup></span> for <span class="math-inline">m≥1</span>.

**Solution.** By convention zero is encoded as `0`, so its length is one. One is `1`, also length one. Fifteen is `1111`, length four; sixteen is `10000`, length five; seventeen is `10001`, length five. The largest <span class="math-inline">m</span>-bit positive integer is <span class="math-inline">2<sup>m</sup>−1</span>, written as <span class="math-inline">m</span> ones. The next integer <span class="math-inline">2<sup>m</sup></span> is a one followed by <span class="math-inline">m</span> zeros, length <span class="math-inline">m+1</span>. The jump at an exact power of two is why the correct formula uses <span class="math-inline">⌊log₂ U⌋+1</span>, not <span class="math-inline">⌈log₂ U⌉</span> for every positive <span class="math-inline">U</span>.

### Problem 3 — An array has two size measures

**Question.** An array contains <span class="math-inline">n</span> unsigned values, each in <span class="math-inline">[0,n³−1]</span>, and each stored in the smallest common fixed width. Estimate its data bits, assuming <span class="math-inline">n≥2</span>.

**Solution.** The width is <span class="math-inline">b=⌈log₂(n³)⌉=⌈3log₂ n⌉</span> bits, since <span class="math-inline">2<sup>b</sup></span> distinct patterns must cover the range. Hence the array payload uses exactly <span class="math-inline">nb</span> bits under the stated fixed-width layout, which is <span class="math-inline">Θ(n log n)</span> bits. It has <span class="math-inline">n</span> *elements* but more than a constant number of bits per element. A word-RAM with <span class="math-inline">w≥b</span> could hold each value in one word; a narrower machine would need multiple words per element. A length header and allocation metadata are separate.

### Problem 4 — Addressing is not the same as storing the length

**Question.** A memory has <span class="math-inline">n=256</span> cells indexed <span class="math-inline">0,…,255</span>. What minimum unsigned word width addresses every cell? What minimum width stores the integer <span class="math-inline">256</span> itself?

**Solution.** There are <span class="math-inline">256=2⁸</span> addresses, so eight bits suffice for indices <span class="math-inline">0,…,255</span>. The integer 256 is binary `100000000` and requires nine bits. Therefore a loop counter that must hold <span class="math-inline">n</span> at termination is not represented by the same eight-bit unsigned variable that addresses the final element. An implementation can use a wider counter, a different termination test, or a sentinel. The mathematical distinction is <span class="math-inline">⌈log₂ n⌉</span> for addresses versus <span class="math-inline">⌈log₂(n+1)⌉</span> for the value <span class="math-inline">n</span>.

### Problem 5 — Matrix width is not entry count

**Question.** A dense <span class="math-inline">30 × 40</span> matrix has 16-bit entries. A procedure reads every entry once. Give its number of entries, payload bits, and minimum word reads on a 64-bit machine under (a) one entry per word and (b) perfectly packed entries with one-word reads.

**Solution.** There are <span class="math-inline">30·40=1200</span> entries and <span class="math-inline">1200·16=19200</span> payload bits. Under (a), each entry is separately word-aligned, so 1200 word reads are required. Under (b), one 64-bit word holds four entries and 300 word reads suffice. The two layouts represent the same abstract matrix and same payload information but give different read counts. Ignoring addressing overhead, both require work proportional to their own stored-word count. Calling the scan “40 steps because the width is 40” is wrong.

### Problem 6 — Sparse and dense graph representations

**Question.** Compare a graph with <span class="math-inline">V=1000</span> vertices and <span class="math-inline">E=1500</span> directed edges under adjacency lists and an adjacency matrix. Count the leading representation units without claiming exact machine bytes.

**Solution.** A standard adjacency-list layout stores a record per vertex and an edge record per directed edge, hence a quantity proportional to <span class="math-inline">V+E=2500</span> records/words, subject to pointer and allocator constants. An adjacency matrix has <span class="math-inline">V²=1,000,000</span> Boolean positions: one million bits if packed or one million word cells in a naive word-per-entry layout. The list is attractive for this sparse graph. However, a matrix can answer an edge-existence query by direct indexed access; a basic list may have to inspect a neighbor list. Space alone does not decide every interface cost. An undirected edge stored in two adjacency lists changes the constant factor, not the <span class="math-inline">V+E</span> parameter form.

### Problem 7 — An alleged constant-time static array

**Question.** A claimed algorithm creates a new zero-initialized array of length <span class="math-inline">n</span>, then returns its first element. Its author counts only the final read and reports constant time. Identify the omitted obligation.

**Solution.** Under an eager initialized-array contract, all <span class="math-inline">n</span> cells must be established as zero. If a primitive write handles one word, initialization entails <span class="math-inline">n</span> writes; the final read adds a constant amount. A lazy allocation scheme may defer physical writes, but then the model and operating-system behavior must be stated: a later read must still return zero, and deferred work or page handling is charged at some point. If the problem merely asks to return the number zero, allocating the array is unnecessary. The lesson is to analyze the **specified computation**, not just the last source line.

### Problem 8 — Word-size overflow changes the answer

**Question.** On an unsigned eight-bit word machine, a procedure computes <span class="math-inline">200+100</span> in one primitive addition. Is its result the exact integer sum 300?

**Solution.** One eight-bit word stores only <span class="math-inline">0,…,255</span>. With wraparound arithmetic, <span class="math-inline">300 mod 256 = 44</span>; an implementation that traps overflow behaves differently. The exact integer 300 is binary `100101100` and requires nine bits. Exact addition needs a representation using more than eight bits and appropriate carry handling. A constant-time *word* addition is a statement about an instruction, not a guarantee of exact arithmetic on arbitrary integers. Any solution that reports 300 while invoking only one eight-bit modular addition has changed models without saying so.

### Problem 9 — Product growth invalidates source-line counting

**Question.** A loop multiplies <span class="math-inline">n</span> copies of <span class="math-inline">2<sup>w−1</sup></span> and returns the exact product. Why is “<span class="math-inline">n−1</span> multiplications, therefore <span class="math-inline">n−1</span> word-RAM steps” invalid? Give a definite output-size lower bound. This is an independently written version of the large-integer model-checking type emphasized in CMU 15-451 Lecture 3.

**Solution.** The exact result is <span class="math-inline">2<sup>n(w−1)</sup></span>, which needs <span class="math-inline">n(w−1)+1</span> bits. Once the partial product exceeds <span class="math-inline">w</span> bits, it is no longer an operand of a primitive one-word multiplication. The result occupies at least <span class="math-inline">⌈(n(w−1)+1)/w⌉</span> words; explicitly writing those words takes at least that many word outputs in a one-word-output model. A stronger exact running-time bound would require a specified multiword multiplication algorithm. Reducing modulo <span class="math-inline">2<sup>w</sup></span> restores word-size operands but changes the requested answer.

### Problem 10 — Binary capacity and table size

**Question.** A capacity <span class="math-inline">U=2²⁰</span> is supplied in binary. A method allocates <span class="math-inline">U+1</span> table cells. Compare capacity-input bits with cells and classify the dependence. This is independently worded from the encoding-versus-capacity reasoning type in Berkeley CS170's knapsack lecture.

**Solution.** The binary representation of <span class="math-inline">2²⁰</span> has one leading one and twenty zeros: 21 bits. The table has <span class="math-inline">1,048,577</span> cells. Its size is exponential in the exponent parameter 20, and proportional to the numeric capacity. This demonstrates why a method polynomial in <span class="math-inline">U</span> need not be polynomial in the length of a binary input containing <span class="math-inline">U</span>. With other input fields, total length may exceed 21 bits, so the exact relationship to *total* length must be stated rather than guessed. The classification applies to this table-based method, not every possible algorithm for the task.

### Problem 11 — A comparison lower bound and a direct-address query

**Question.** A course proves a comparison lower bound for searching among arbitrary comparable keys. Someone proposes a Boolean table indexed by integer keys from <span class="math-inline">0,…,U−1</span> and claims the lower bound is false. Resolve the apparent contradiction. This is an independently worded model-switching type prompted by CMU 15-451 Lecture 3.

**Solution.** The lower bound quantifies over algorithms whose information about opaque keys comes from comparisons. The proposed table uses an integer key as a memory address, an operation outside that model. Under a word-RAM with sufficient address width, direct-address queries take a constant number of word operations after table construction. But initialization uses <span class="math-inline">U</span> table cells and inserting keys costs additional work. If <span class="math-inline">U</span> is huge, the total method may be unattractive. Both claims can hold simultaneously because their operation sets and charged resources differ. The question “which is faster?” needs the permitted operations, preprocessing, number of queries, and space budget.

### Problem 12 — When must every position be read?

**Question.** Prove a worst-case read lower bound for deciding whether all <span class="math-inline">n</span> one-word entries are zero when the array is unsummarized. Explain why the same bound does not apply to returning its length.

**Solution.** Consider the all-zero input. If a deterministic correct algorithm omits entry <span class="math-inline">j</span>, replace just that entry by one. Every entry it read remains zero, so its observations and control path are unchanged. It returns “all zero” on the modified input, a contradiction. Therefore it reads all <span class="math-inline">n</span> entries on this input and has at least <span class="math-inline">n</span> reads in the worst case. By contrast, if the array length is explicitly stored in a trusted header, returning it does not depend on the values of the <span class="math-inline">n</span> entries; changing an unread entry cannot change the answer. The adversary's indistinguishability pair no longer exists.

### Problem 13 — Explicit output versus a pointer

**Question.** A method is asked to return a copy of an <span class="math-inline">n</span>-word array. Can it be constant time by returning the original array's address?

**Solution.** A copy is a distinct <span class="math-inline">n</span>-word object with the same values, so changing the original later must not change the copy. Returning the original address aliases the original and violates the contract. If the output interface requires writing each new word and a primitive step writes one word, at least <span class="math-inline">n</span> writes are necessary. A copy-on-write representation might defer those writes, but it changes the representation and must charge later modifications and metadata. If the contract explicitly permits a read-only shared view, returning a pointer can be constant time. These are different tasks.

### Problem 14 — What does a measured runtime establish?

**Question.** An implementation completes 100 random arrays of length <span class="math-inline">10⁶</span> quickly. Which conclusions are justified: (a) it terminates on every input, (b) its worst-case time is below the measured maximum, (c) it was fast on those 100 instances under the tested setup, (d) it is correct on all arrays?

**Solution.** Only (c) follows directly. A finite sample cannot rule out another array that triggers a slower path or nontermination. The maximum observed time is a **lower bound on the maximum across all admissible instances under the same measurement convention**, not an upper bound. Passing 100 outputs also cannot prove universal correctness. The measurements are useful evidence about implementation performance, but a proof of (a) or (d), and a mathematical worst-case upper bound for (b), need reasoning covering every admissible input. The distinction between an empirical implementation result and an algorithmic guarantee is part of the computational model contract.

### Problem 15 — The same loop under binary and unary encodings

**Question.** A program receives a positive integer <span class="math-inline">U</span>, then executes exactly <span class="math-inline">U</span> constant-cost iterations. Give its iteration count as a function of input length when <span class="math-inline">U=2<sup>m</sup></span> is encoded (a) in binary and (b) in unary. Does the algorithm itself change?

**Solution.** In binary, the input is a one followed by <span class="math-inline">m</span> zeros and has <span class="math-inline">m+1</span> bits. The loop performs <span class="math-inline">2<sup>m</sup></span> iterations, exponential in <span class="math-inline">m</span>. In unary, the same value is a string of <span class="math-inline">2<sup>m</sup></span> ones, so the loop performs one iteration per input symbol and is linear in that much larger encoded input. The loop's actions did not change; only the size convention and the work needed to supply the input changed. Claiming polynomial time without naming the encoding conceals this difference.

### Problem 16 — Decision-tree capacity

**Question.** A comparison-only task has 65 distinguishable correct answers. Each charged test is yes/no. What is the minimum possible worst-case number of tests from information capacity alone? If a test may instead have three outcomes, what lower bound follows?

**Solution.** After <span class="math-inline">d</span> yes/no tests, at most <span class="math-inline">2<sup>d</sup></span> distinct leaves are reachable. Six tests allow only 64 leaves, fewer than 65; seven allow 128. Therefore every correct binary decision tree has worst-case depth at least seven. With at most three outcomes per test, <span class="math-inline">3³=27&lt;65</span> while <span class="math-inline">3⁴=81≥65</span>, so at least four tests are needed. These are **lower bounds**, not constructions attaining them: restrictions on which questions are legal may force more tests. An integer-indexed table can evade this comparison-only argument by using an address computation not modeled as one of those tests.

## 9. High-yield review: complete decision rules and traps

1. **Write the contract first.** Name the admissible inputs, allowed outputs, encoding, primitive operations, and charged resources before judging an algorithm. A claim missing one of these may be unanswerable rather than false.
2. **Keep four objects separate.** A problem can permit many outputs; one deterministic algorithm chooses one. A program implements that algorithm; a benchmark measures that program on selected instances.
3. **Use bits for encoding size.** The binary length of positive <span class="math-inline">U</span> is <span class="math-inline">⌊log₂ U⌋+1</span>, with zero encoded as one bit under the convention used here. The length jumps at exact powers of two.
4. **Do not silently equate element count and bit length.** An <span class="math-inline">n</span>-element array of <span class="math-inline">b</span>-bit values carries <span class="math-inline">nb</span> data bits before metadata.
5. **For a dense matrix, multiply dimensions.** An <span class="math-inline">r×c</span> matrix contains <span class="math-inline">rc</span> entries. Its bit storage also depends on entry width and packing.
6. **For a graph, name the representation.** Adjacency lists use storage proportional to <span class="math-inline">V+E</span> records; an adjacency matrix has <span class="math-inline">V²</span> positions. The same abstract graph can induce different primitive costs.
7. **Distinguish addressing from holding the endpoint.** To address cells <span class="math-inline">0,…,n−1</span>, require at least <span class="math-inline">⌈log₂ n⌉</span> bits. To store the integer <span class="math-inline">n</span>, require <span class="math-inline">⌈log₂(n+1)⌉</span> bits.
8. **A primitive word operation takes word-sized operands.** A source-language operator on a multiword integer is an algorithm, not automatically one word-RAM instruction.
9. **State overflow semantics.** Modular, trapping, saturating, and exact integer arithmetic solve different specifications. A word-width assumption without overflow behavior is incomplete.
10. **Indexed access does not imply free initialization.** Reading one already-stored array element may be constant time; constructing and zeroing <span class="math-inline">n</span> distinct cells entails work that must be accounted for.
11. **An interface does not fix implementation cost.** `get_at(i)` has different costs in a static array and a basic linked list. Check representation and operation preconditions.
12. **Comparison lower bounds stay inside the comparison model.** Integer indexing or bit inspection may escape that model but may introduce memory, preprocessing, or key-range costs.
13. **Charge preprocessing when comparing query methods.** A constant-time direct-address query follows table construction; it is not a constant-time end-to-end method from a raw input.
14. **Numeric value is not numeric description length.** A capacity <span class="math-inline">U=2<sup>m</sup></span> needs <span class="math-inline">m+1</span> bits but a <span class="math-inline">U</span>-cell table has exponentially many cells in <span class="math-inline">m</span>.
15. **Use “pseudo-polynomial” for the right reason.** It describes an algorithm whose bound is polynomial in numeric values and item count but may be superpolynomial in binary input length; it does not classify the underlying problem by itself.
16. **A read-all lower bound needs sensitivity.** If changing any unread input unit can change the required answer, an adversarial pair proves the bound. If a stored summary suffices, the premise fails.
17. **Match the granularity of a read.** Packed <span class="math-inline">w</span>-bit input read by words may require <span class="math-inline">⌈n/w⌉</span> word reads rather than <span class="math-inline">n</span> bit reads.
18. **An explicit output has a writing cost.** Writing <span class="math-inline">k</span> separate words costs at least <span class="math-inline">k</span> one-word writes; returning a pointer is a different output contract.
19. **Worst case is a quantifier over all instances of the selected size.** A handful of quick experiments supports only those measurements, not a universal upper bound or universal correctness.
20. **Average case requires a distribution.** No probability distribution means no mathematically defined average-case input time.
21. **Count space in the stated unit.** <span class="math-inline">s</span> words contain <span class="math-inline">sw</span> payload bits; “space” may include or exclude the input and output, so label the convention.
22. **Check the first and last legal inputs.** Empty arrays, absent keys, maximum addresses, exact powers of two, and overflowing intermediate values reveal model errors quickly.
23. **A comparison tree has finite information per test.** For integers <span class="math-inline">b≥2</span> and <span class="math-inline">q≥1</span>, if each test has at most <span class="math-inline">b</span> outcomes, distinguishing <span class="math-inline">q</span> required answers needs at least <span class="math-inline">⌈log<sub>b</sub> q⌉</span> tests in the worst case; verify that the answers really are distinguishable and that no extra operation is allowed.
24. **Encoding conventions are part of the theorem.** A method linear in a unary numeric input can be exponential in the length of the same integer encoded in binary.

## 10. References and remaining limits

1. MIT, Erik Demaine, Jason Ku, Justin Solomon, *6.006 Introduction to Algorithms*, Spring 2020, [Lecture 1: Introduction](https://live.ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/477c78e0af2df61fa205bcc6cb613ceb_MIT6_006S20_lec1.pdf), pp. 2–4; [Recitation 1: Algorithms and Model of Computation](https://live.ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/c6d8f06c6f11e3342633dec85498f551_MIT6_006S20_r01.pdf), pp. 1–4.
2. Carnegie Mellon University, Daniel Anderson and David Woodruff, *15-451 Algorithm Design and Analysis*, Spring 2025, [Lecture 3: Integer Sorting](https://www.cs.cmu.edu/~15451-s25/notes/lecture03.pdf), pp. 1–4.
3. Princeton University, Kevin Wayne, *Algorithm Analysis*, updated 2021, [lecture slides](https://www.cs.princeton.edu/~wayne/kleinberg-tardos/pdf/02AlgorithmAnalysis-2x2.pdf), slides 3–7.
4. Stanford University, Mary Wootters and CS161 course scribes, *Design and Analysis of Algorithms*, Fall 2017, [Lecture 1: Introduction](https://web.stanford.edu/class/archive/cs/cs161/cs161.1182/Lectures/Lecture1/CS161Lecture01.pdf), pp. 2–3.
5. University of California, Berkeley, CS170 course staff, *Efficient Algorithms and Intractable Problems*, [knapsack and pseudo-polynomial-time lecture slides](https://cs170.org/assets/lec/lec-13_blank.pdf), PDF pp. 9–11.

The selected courses are a documented, accessible subset, not every course worldwide. The word-RAM instruction set varies by author; multiplication, division, allocation, cache effects, and I/O require separate conventions in applications where they matter. The chapter addresses the identified in-scope cases, but no finite chapter can guarantee performance on every unseen exam question. Its purpose is to make resource claims testable and precise before the later analysis chapters build on them.
