## From algebra to examination certificates

The complete foundational lesson and its forty worked tutorials remain below. The following constructions connect that teaching to the revised examination bank. They add explicit counting, circuit interpretation and verification methods; they do not replace the lesson with a recall sheet. Throughout, signals are binary, $+$ denotes OR inside Boolean expressions, and numerical counts use ordinary integer arithmetic. An input word has a declared significance order before it is assigned an index.

### 1. Canonical form is a construction with a proof

For a row $r=(r_1,\ldots,r_n)$, define $m_r$ by choosing $x_i$ when $r_i=1$ and $\neg x_i$ when $r_i=0$, and ANDing the chosen literals. Each literal is one precisely when that input agrees with its row bit, so their AND is one exactly at $r$. Define $M_r$ with the opposite polarities, joined by OR. Every literal is zero at $r$; any other word differs in at least one position and makes the corresponding literal one. Thus $M_r$ is zero exactly at $r$.

$$F=\bigvee_{r:F(r)=1}m_r,\qquad F=\bigwedge_{r:F(r)=0}M_r.$$

The first construction accepts precisely the true rows. The second rejects precisely the false rows. This proves their equality to the specification, including the all-zero function, whose DNF is the empty OR, and the all-one function, whose CNF is the empty AND. Their values are zero and one, respectively.

With input order $a,b,c$, a row has index $4a+2b+c$. For $F=\neg a\neg b+abc$, the true indices are $0,1,7$, giving three canonical minterms; the false indices are $2,3,4,5,6$, giving five canonical maxterms. The simplified expression has two product terms, but it still has three true rows. A request for canonical term count, minimum product count and gate count therefore poses three different tasks.

The last bank's authentic majority CNF question illustrates another distinction: an equivalent DNF is the wrong requested format. A correct answer must satisfy both the truth function and the prescribed syntax. Build a row-specific witness for each disputed clause instead of relying on its resemblance to a memorized formula.

### 2. Count independent decisions after identifying the constrained objects

A single $n$-input scalar function has $2^n$ input rows. The class of all such functions has $2^{2^n}$ members, because each of those rows receives an independently chosen output bit. A predicate's number of true rows is instead a count within one specified truth table. These two levels cannot be interchanged.

If $d$ rows of a partial scalar table are free and uncoupled, there are $2^d$ completions. Relations between rows change the number of independent choices. For self-duality, complementation pairs row $i$ with $2^n-1-i$ and forces opposite outputs. When $n\ge1$, there are $2^{n-1}$ distinct pairs, giving $2^{2^{n-1}}$ unrestricted self-dual tables. A pair with no fixed entries contributes two choices, a consistent constrained pair contributes one, and an inconsistent pair forces zero global completions. At $n=0$, the sole empty word is its own complement, so self-duality is impossible for a binary scalar output.

For a symmetric function, all words of the same Hamming weight share one output. The $n+1$ weight layers are nonempty and otherwise independent, giving $2^{n+1}$ functions. Layer $k$ contains $\binom nk$ words. After choosing layer outputs $s_k$, the true-row count is
$$N_{\mathrm{true}}=\sum_{k=0}^{n}s_k\binom nk.$$
For three-input majority, the layer outputs are $0,0,1,1$, yielding $3+1=4$ true rows. There are sixteen possible symmetric layer-output vectors, and majority is only one of them.

### 3. Independence, overlap and complement counting

Consider $F=(a_1b_1)+\cdots+(a_nb_n)$ with $2n$ distinct primary inputs. Independence here refers to the disjoint sets of *input variables*, not disjoint true-product events. A row can make several products one. Counting one chosen true term overcounts such rows.

The false event is simpler: every pair must avoid $11$. A pair has exactly three allowed states, and those choices can be made independently across distinct input pairs. Therefore
$$N_{\mathrm{false}}=3^n,\qquad N_{\mathrm{true}}=4^n-3^n.$$
For two pairs, inclusion–exclusion independently checks the result: each product is one on four rows, their overlap contains one, and $4+4-1=7=16-9$.

If terms share a variable, this product argument no longer applies. For $F=ab+ac=a(b+c)$, condition on $a$: when $a=0$ no row is accepted; when $a=1$, three of the four $(b,c)$ contexts are accepted. There are exactly three true three-input rows. The formula $4^2-3^2=7$ describes a different four-input function and cannot be transferred by merely counting the two written products.

An implication chain gives a different counting certificate. Its accepted words are exactly $0^k1^{n-k}$ for $k=0,\ldots,n$, producing $n+1$ true rows. Every forbidden $10$ adjacency violates one clause, and every word without such an adjacency has a unique transition position. A chain of neighboring equivalences instead accepts only the two constant words for $n\ge1$. At $n=1$ both conjunctions are empty and coincide; strict comparison needs $n\ge2$.

### 4. Recover ANF coefficients instead of counting expressions that might collide

The unique algebraic normal form uses XOR of square-free monomials. Write
$$F(x)=\bigoplus_{S\subseteq\{1,\ldots,n\}}c_S\prod_{i\in S}x_i.$$
Let $1_T$ be the word that is one precisely in positions of $T$. Evaluation gives $F(1_T)=\bigoplus_{S\subseteq T}c_S$. Therefore
$$c_S=\bigoplus_{T\subseteq S}F(1_T).$$
To prove the inversion, substitute the evaluation sum. A fixed coefficient $c_U$ appears once for each intermediate set $T$ with $U\subseteq T\subseteq S$, a total of $2^{|S|-|U|}$ times. In XOR arithmetic this multiplicity vanishes unless $U=S$, where it is one. The inversion both constructs the coefficients and proves their uniqueness.

For an affine function, recover $c=F(0)$ and $a_i=F(e_i)\oplus F(0)$; there are $n+1$ independent binary coefficients and $2^{n+1}$ distinct functions. For degree at most two, additionally recover
$$a_{ij}=F(e_i+e_j)\oplus F(e_i)\oplus F(e_j)\oplus F(0),$$
where $e_i+e_j$ denotes the word containing the two distinct one positions. There are $1+n+\binom n2$ square-free monomials, giving $2^{1+n+\binom n2}$ functions. A squared input is not another choice, because $x_i^2=x_i$ for both possible input values.

Degree “at most two” includes the affine subclass. For $n\ge2$, the count of functions with degree *exactly* two is $2^{1+n+\binom n2}-2^{n+1}$. At $n=1$, there are no pair monomials and that difference is zero. The class also includes zero; no convention for the algebraic degree of the zero function changes this counting argument.

### 5. A monotone-function count requires the cube's partial order

Identify each word with its set of one positions. Monotonicity means $S\subseteq T\Rightarrow F(S)\le F(T)$. It does not constrain incomparable sets. The minimal true sets of a monotone function form an antichain; conversely, an antichain defines a unique monotone function by declaring all its supersets true. The empty antichain gives constant zero and the antichain containing the empty set gives constant one.

For three inputs, the antichain counts by size are $1,8,9,2$, totaling twenty. The nine two-member antichains split into three singleton/singleton pairs, three pair/pair pairs and three singleton/opposing-pair combinations. The two triples are the full singleton layer and full pair layer. No fourth incomparable member exists in the three-input cube. This classification establishes completeness rather than treating twenty as a table to memorize.

For a *specified* function, use cofactors instead of enumerating all functions. Positive unateness in input $x$ means $F_0\le F_1$, equivalently $F_0\neg F_1=0$. Negative unateness means $F_1\le F_0$. Both conditions hold for an irrelevant input. Merely seeing both $x$ and $\neg x$ in a redundant expression proves neither binateness nor dependence: $xy+(\neg x)y=y$ is independent of $x$.

### 6. Translate a source schematic into named equations

Every output must be traced through the actual connected pins. For the authentic five-NAND network, name $t=\neg(xy)$, $u=\neg(xt)$ and $v=\neg(yt)$. The outputs are $F_1=\neg(uv)$ and $F_2=\neg(vv)$. Tied NAND inputs implement NOT, so the second output is $yt=(\neg x)y$, while the first is XOR. The ordinary integer certificate $x-y=F_1-2F_2$ verifies the half-subtractor on all four input rows.

A select pin has a different role from a data pin. In a two-to-one mux, $s=0$ selects $I_0$ and $s=1$ selects $I_1$, giving $F=(\neg s)I_0+sI_1$. Two cascaded source muxes with first data $(1,0)$ and second data $(t,0)$ produce $t=\neg b$ followed by $F=(\neg a)(\neg b)$. Keep constant-data labels and select-value labels visibly distinct in the schematic.

Both networks describe settled binary behavior. Animated checkpoints trace logical evaluation and input cases; they do not assert measured transistor timing. A temporal hazard demonstration must instead declare a delay contract. For $F=ab+(\neg a)c$, stable $b=c=1$ makes both endpoints one when $a$ changes. If the old product falls before the inverter-dependent new product rises, the uncovered interval can produce a static-one glitch. The consensus term $bc$ bridges that interval without changing the truth table. This explanation applies to the specified single-input transition and SOP implementation, not every possible waveform or hardware mapping.

### 7. Turn “same function” into a certificate with a clear domain

For scalar functions $F,G$, the miter $M=F\oplus G$ marks disagreement. Full equivalence is $M=0$ on every input; a satisfying input is a counterexample. Under a care function $C$, equivalence means $CM=0$, so disagreement outside the care set is permissible. For vector outputs, OR the individual mismatch indicators. XOR is wrong because two simultaneous errors can cancel.

For example, compare $F=a+b$ with $G=a\oplus b$. Their miter is $ab$, since $a+b=a\oplus b\oplus ab$. They are not fully equivalent: $11$ is a witness. If $C=\neg(ab)$, then $CM=0$ and they are equivalent on the declared care set. A don't-care output is freedom in a partial specification; it is not a third value added to binary algebra.

When solving a relation for an unknown Boolean function $H$, restrict each remaining-input context and list which values of $H$ are permitted there. Zero allowed values makes the relation inconsistent; one forces that table cell; two make it free. If the cells are independent, count completions by multiplying their local choice counts. This method is worked through in the transfer challenges and extends beyond guessing a short formula.

**Sources for these constructions.** Cambridge's complete Boolean-law slides, Stanford's memoryless/acyclic model and majority derivation, Berkeley's two complete written bodies on algebra and canonical design, and CMU's scoped cofactor/quantification/recursive-verification material were reread for this revision. MIT's Chapter 4 annotations and Cornell's written gates/selector body provide additional checks. The exact reading scopes and access limitations are recorded in the source audit. ANF inversion, constrained function counts and antichain classifications here are independently proved extensions rather than attributed wholesale to those courses.
