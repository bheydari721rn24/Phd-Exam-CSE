## 1. Scope, prerequisites, and reviewed courses

This chapter develops Boolean algebra as a precise language for describing, transforming, and checking binary functions. After studying it, you should be able to translate a verbal condition into an unambiguous equation, prove an identity without illegal cancellation, find a counterexample to a false identity, construct and interpret a truth table, and analyze a complicated expression through its cofactors. The final sections extend those foundations to sensitivity, monotonicity, quantified conditions, and recursive verification. These extensions are included because they explain why the basic identities work and how to solve unfamiliar combinations of them.

The prerequisites are binary positional notation, elementary set operations, and direct proof. No knowledge of electronic devices is assumed. Throughout, a logic variable has exactly two values. A voltage in an indeterminate electrical range, an HDL unknown value, and a specification's unspecified output are different concepts; none is a third value in the algebra developed here.

Four complementary core courses were selected after comparing an accessible pool, with two further university courses used for cross-checking. This is a documented selection for this chapter, not a claim that every course worldwide has been inspected.

| Role | University and course | Written material actually reviewed | Contribution |
|---|---|---|---|
| Core foundation | MIT, 6.004 Computation Structures; Chris Terman, Spring 2017 | Chapter 4 annotated teaching text, functional specifications, synthesis, algebraic reduction, don't-care conditions, and the nonminimal-expression discussion | The connection between a specification, an equation, and its implementation; the limits of algebraic cost claims. |
| Core algebra | Cambridge, Digital Electronics; Ian Wassell, 2020–21 | Logic Gates and Boolean Algebra, PDF pages 1–14; examples paper pages 1–2 for in-scope patterns | Precise operator meanings, dual distributivity, absorption, and nested complement manipulation. |
| Core verification | Stanford, EE108A Digital Systems I; William J. Dally and Philip Levis, Winter 2008 | Lecture 1, PDF pages 8–16 | Memoryless functions, acyclic composition, majority specification, and equation verification. |
| Core advanced reasoning | Carnegie Mellon, 18-760 VLSI CAD; Rob A. Rutenbar, Fall 2001 | Advanced Boolean Algebra, PDF pages 4–24 and 30–39; Homework 1, in-scope items 1–5 | Cofactors, Shannon decomposition, Boolean difference, quantification, and recursive reasoning. |
| Cross-check | UC Berkeley, CS61C; John Wawrzynek, with edits by Lisa Yan | Boolean Algebra and Canonical Form, CL Design, written teaching bodies | Distinguishing a unique function from multiple expressions and connecting exhaustive checks to algebraic proofs. |
| Cross-check | Cornell, CS3410; Adrian Sampson and Giulia Guidi, Fall 2024 | Gates & Logic, truth tables, notation, and the universal-construction discussion | Specification-first construction and the distinction between single-bit logical operations and word operations. |

The source audit records the other candidates, inaccessible resources, and corrections. Main explanations, proofs, diagrams, laboratory, and worked questions here are independently written. Course exercise patterns are attributed where used; a linked course does not mean its entire exercise collection has been reproduced.

### Boundary with the next chapters

Basic row-selector terms appear here to prove that every binary function has an expression. Detailed canonical minterm/maxterm indexing, Karnaugh-map geometry, prime-implicant selection, and minimization algorithms belong to **Minterms, Maxterms, and Simplification**. Gate symbols, NAND/NOR-only construction, fan-in restrictions, and implementation costs belong to **Logic Gates and Function Implementation**. Timing and hazard removal require their later chapters. This chapter proves steady-state functional identities, rather than certifying physical transient behavior. The archived Iranian entrance-examination papers remain reserved for the final month.

## 2. Boolean values, notation, and expression structure

### The two-element system

Let B={0,1}. Complement exchanges the two values. AND returns one precisely when both operands are one. Inclusive OR returns one when at least one operand is one. The words "inclusive" and "at least" matter: an OR is still one when both inputs are one.

| x | y | x′ | xy | x+y | x⊕y | (xy)′ | (x+y)′ |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 | 1 | 1 | 1 | 0 |
| 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 |

Juxtaposition and the centered dot mean AND; a plus sign means OR. A prime attached to a parenthesized expression complements that entire expression. An overbar is an equivalent notation, but primes keep the complement's extent explicit in plain text and small displays. XOR is written with its own operator. In the table, NAND is the complement of AND, and NOR is the complement of OR; their physical gate implementations are developed later.

The same familiar characters can represent different operations in different mathematical systems. Here 1+1=1 because the plus sign means OR. In integer arithmetic the sum is two, and in arithmetic modulo two the sum is zero. Never transfer a subtraction, division, cancellation, or binomial rule from ordinary arithmetic merely because the notation looks familiar.

### Precedence and scope

Complement binds most tightly, AND follows, and OR comes last. Therefore x+yz means x+(yz), while (x+y)z has a different expression tree. With XOR, explicit parentheses are preferable to relying on a source's precedence convention. The prime in (x+y)′ does not mean x+y′. A double complement returns the original value: (x′)′=x.

An expression is a syntactic recipe. Its value is obtained by assigning values to all its variables and evaluating its expression tree from the leaves upward. A function is the resulting mapping for every assignment. Two different recipes can define the same function. Counting expressions is consequently different from counting functions.

Consider E=(x+y′)(x′+z). On assignment (x,y,z)=(0,1,1), compute y′=0 and x′=1; the two factors are zero and one; their AND is zero. This explicit tree evaluation prevents the common error of distributing a complement into only part of an expression.

### Literals, terms, and constants

A literal is a variable or its complement. A product term is an AND of literals. A sum term is an OR of literals. A sum of products, abbreviated SOP, ORs product terms; a product of sums, abbreviated POS, ANDs sum terms. A variable alone qualifies as either kind of term. A product containing both x and x′ is zero; a sum containing both is one. Repeated identical literals add nothing because both AND and OR are idempotent.

Count literal **occurrences** when comparing written expressions, unless the problem explicitly asks for distinct variables. For example, xy+x′z has four literal occurrences but three distinct variables. Factoring can change that occurrence count without changing the function. Neither occurrence count nor term count alone determines the number or speed of physical gates.

## 3. Functions, complete truth tables, and precise specifications

### Why a truth table is complete

A scalar Boolean function on n named inputs is a mapping f:B<sup>n</sup>→B. There are 2<sup>n</sup> assignments, since each independent input has two choices. Fix an input order before enumerating rows. For inputs x,y,z in that order, use binary order 000,001,010,011,100,101,110,111, with the first input as the most significant bit. A different order is valid if it is stated, but it changes the meaning of row numbers and column vectors.

Each row requires exactly one output for a fully specified deterministic function. If the same input row is assigned both zero and one, the specification is inconsistent. If a row is omitted, the table is incomplete unless the omission is deliberately identified as an unconstrained case. A truth table is unique after the variable order and row order have been fixed; expressions and circuit structures need not be unique.

For k outputs, the mapping is f:B<sup>n</sup>→B<sup>k</sup>. Each output column can be specified independently unless an additional relationship between outputs is imposed. The number of possible scalar functions is 2<sup>2<sup>n</sup></sup>, because the output at each of the 2<sup>n</sup> rows has two independent choices. The number of unconstrained k-output functions is 2<sup>k·2<sup>n</sup></sup>. For zero inputs there is one input assignment, the empty tuple, and two scalar constant functions. These are nested exponentials, not 2<sup>2n</sup>.

### Turning words into mathematics

Choose variable meanings before writing any formula. Suppose an abstract controller enables an output when a request exists, permission is present, and a veto is absent. Define r as "request exists," p as "permission is present," and v as "veto is active." Then e=rpv′. The veto is high when it forbids the output; failing to state that polarity reverses the meaning of the final literal.

"Exactly one of x and y" means x′y+xy′. "At least one" means x+y. "Neither" means (x+y)′. "Not both" means (xy)′. "Unless inhibited" means AND with the complement of inhibition, not OR with the inhibition signal. "Only if" expresses a necessary condition: e=1 only if p=1 means e≤p; it does not by itself specify e=p. "If and only if" specifies both directions.

Three-input majority is one when at least two inputs are one. One direct expression is xy+xz+yz. To verify the expression, split assignments by the number of ones. With zero or one one, no pair product is one. With two or three ones, at least one pair product is one. This is a structural proof covering all eight rows, not a guess based on three examples.

### A truth-table algorithm and its cost

The following pedagogical Python routine uses actual Boolean inputs and does not reinterpret arbitrary integers as bit vectors. The `fn` callback must be pure and must return a Boolean or the integers zero or one. There are 2**n rows; evaluating a size-s expression tree separately at each row costs O(s·2<sup>n</sup>) time. The code streams rows instead of storing the complete table.

```python
from itertools import product

def rows(fn, n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a nonnegative integer")
    for bits in product((False, True), repeat=n):
        result = fn(*bits)
        if type(result) not in (bool, int) or result not in (0, 1):
            raise ValueError("output must be binary")
        yield tuple(int(b) for b in bits), int(result)

def majority(x, y, z):
    return (x and y) or (x and z) or (y and z)

for assignment, output in rows(majority, 3):
    print(assignment, output)
```

An exhaustive finite table is a proof for the fixed set of variables represented in that table. A few random rows are not a proof. Conversely, a large table is often a poor human explanation: an algebraic or case-based argument can show the reason an identity works and avoid exponential enumeration.

## 4. Fundamental laws and why they hold

### A reference table with both dual forms

| Law | OR-oriented identity | AND-oriented identity |
|---|---|---|
| Identity | x+0=x | x·1=x |
| Domination | x+1=1 | x·0=0 |
| Idempotence | x+x=x | xx=x |
| Complement | x+x′=1 | xx′=0 |
| Commutativity | x+y=y+x | xy=yx |
| Associativity | (x+y)+z=x+(y+z) | (xy)z=x(yz) |
| Distributivity | x+yz=(x+y)(x+z) | x(y+z)=xy+xz |
| Absorption | x+xy=x | x(x+y)=x |
| Combining | xy+xy′=x | (x+y)(x+y′)=x |
| De Morgan | (x+y)′=x′y′ | (xy)′=x′+y′ |

The truth-table definitions are the starting point of this chapter. The identities are theorems of that two-element system. A general Boolean algebra can instead be specified axiomatically; different textbooks choose different independent axiom sets. Merely listing several true identities under the heading "axioms" does not prove that a proposed abbreviated list is sufficient to derive every other law.

### Identities, domination, and complement

For x+0, setting x to zero gives zero and setting x to one gives one, so the result is x. For x·1 the same two cases give x. Replacing the neutral operand by the dominating operand gives x+1=1 and x·0=0. Idempotence follows because applying the same requirement twice neither creates nor removes a satisfying assignment. The complement identities follow because exactly one of x and x′ is one on every row.

Double complement follows directly by exchanging zero and one twice. Complement is also unique. If y satisfies xy=0 and x+y=1, then y=y(x+x′)=yx+yx′=yx′, while x′=x′(x+y)=x′x+x′y=x′y. Thus y=x′. The calculation uses the already established AND distributivity and identity laws; it is useful later when establishing De Morgan by identifying the complement of a compound expression.

### Commutativity and associativity

The definitions of AND and OR do not distinguish the two operands, establishing commutativity. A three-way AND is one exactly when all three inputs are one, regardless of grouping. A three-way OR is one exactly when at least one input is one, regardless of grouping. This proves associativity; induction extends it to any finite number of operands. Associativity concerns grouping and commutativity concerns order. They are different statements.

Neither statement permits moving a prime arbitrarily. NAND and NOR are commutative but not associative. For example, with x=0,y=1,z=1, ((xy)′z)′=0, whereas (x(yz)′)′=1. You cannot construct a many-input NAND by pretending a chain of two-input NANDs is an associative operation.

### The two distributive laws

To prove x(y+z)=xy+xz, split on x. If x=0, both sides are zero. If x=1, both sides equal y+z. This proof is valid for arbitrary Boolean expressions substituted for the operands, because those expressions still evaluate to zero or one on every assignment.

The second law is often less familiar: x+yz=(x+y)(x+z). If x=1, both sides are one. If x=0, both sides are yz. It is therefore a valid Boolean identity even though the corresponding equation would be false over ordinary real addition and multiplication. This law is the correct tool for factoring OR over AND.

Absorption can now be derived: x+xy=x(1+y)=x·1=x. Its AND form is x(x+y)=xx+xy=x+xy=x. Combining follows from xy+xy′=x(y+y′)=x. For the POS form, apply the second distributive law: (x+y)(x+y′)=x+yy′=x.

### Set semantics

Fix a universe of assignments U. Associate a function with its set of satisfying assignments. AND becomes intersection, OR becomes union, complement becomes complement relative to U, and XOR becomes symmetric difference. Then absorption says that adding a subset to an already containing set changes nothing. The translation explains why OR has no cancellation: union loses information about which operand supplied a member.

Boolean algebras need not have only two elements; the power set of any universe is another example. The scalar circuit model here uses the two-element algebra, while reasoning about entire functions uses their on-sets. Keep those levels distinct: a function has many assignments, but its value on each assignment is still binary.

## 5. Duality, complementation, and nested De Morgan transformations

### Duality is a structural operation

The dual of an AND/OR/complement expression swaps AND with OR and swaps zero with one, keeping each variable and each literal complement unchanged. Parentheses follow the expression tree. If an identity is true, its dual identity is true. A convenient general proof uses

<div class="formula-block">E<sup>d</sup>(x₁,…,xₙ) = [E(x₁′,…,xₙ′)]′.</div>

Prove this relation by structural induction. A variable leaf satisfies it because double complement returns the variable. A constant leaf exchanges zero and one. At an AND or OR node, De Morgan supplies exactly the required operator swap. A complement node remains a complement node. Applying the relation to two equal functions proves equality of their duals.

The dual is usually **not** the output complement. For E=x+y, the dual is xy, the complement is x′y′, and the input-inverted function is x′+y′. On input 00, those outputs are zero, one, and one respectively. Memorizing "swap AND and OR" without tracking constants and complements produces wrong answers.

### Deriving De Morgan

An OR is zero exactly when every operand is zero. Its complement is therefore one exactly when every complemented operand is one, giving (x+y)′=x′y′. An AND is zero exactly when at least one operand is zero, giving (xy)′=x′+y′. Both statements extend to arbitrary finite arity. They also remain true when an operand is a compound expression: replace that expression as a whole before deciding how to simplify inside it.

For a nested example, take E=[x+(yz′)′]′. First complement the outer OR to get x′[(yz′)′]′. Remove the double complement, obtaining x′yz′. If you instead flip every visible plus or product in one pass without respecting the two nested primes, you can inadvertently complement z twice or leave an unwanted complement on the inner term.

For E=[(x+y′)(z+w)]′, the outer AND becomes an OR: E=(x+y′)′+(z+w)′. The inner ORs become products, giving E=x′y+z′w′. Each prime's scope has been handled once. These are precisely the steps to use in an unfamiliar long expression.

### Self-dual functions

A function is self-dual when f(x)=f<sup>d</sup>(x), equivalently f(x)=[f(x′)]′ with every input complemented. Each assignment pairs with its bitwise complement. A self-dual function must give opposite outputs on each pair. For n≥1, there are 2<sup>n−1</sup> pairs and therefore 2<sup>2<sup>n−1</sup></sup> self-dual scalar functions. Every self-dual function is balanced, meaning half its outputs are one. Balancedness alone is insufficient: two-input XOR is balanced but gives equal outputs on complementary assignments. No zero-input constant is self-dual.

Three-input majority is self-dual: complementing every vote changes a majority of ones into a majority of zeros. This observation is a check on the specification, not a replacement for its truth table or proof.

## 6. Algebraic simplification, containment, and proof discipline

### Simplify for a stated purpose

An expression may be simplified to reduce literal occurrences, shorten a proof, expose a special operation, or enable a particular implementation. Those objectives can disagree. Every equality in a derivation must be valid for the same domain and assumptions. Fewer written terms do not automatically prove a globally minimal circuit, nor do they guarantee faster propagation through physical hardware.

Start with exact complement scope. Then remove constants, repeated literals, and contradictory products. Look for absorption before expanding. Expansion is useful when it creates complementary pairs; it is harmful when it creates many terms without exposing a reduction. Factor in either direction as needed, and verify the result independently.

### Three reusable reductions with proofs

The covering identity is x+x′y=x+y. Apply OR distributivity: x+x′y=(x+x′)(x+y)=1·(x+y)=x+y. Its dual is x(x′+y)=xy. These identities preserve the cofactor where the first literal is zero or one; simply throwing away the complemented term would not.

The SOP consensus theorem is

<div class="formula-block">xy+x′z+yz = xy+x′z.</div>

Insert x+x′=1 into the last term: yz=xyz+x′yz. The first new product is absorbed by xy, and the second is absorbed by x′z. Thus the original expression has the same on-set without yz. The dual theorem is (x+y)(x′+z)(y+z)=(x+y)(x′+z). The theorem does not say that any third product can be discarded: the literals must match the complementary pair and the remaining factors.

The theorem remains valid for compound expressions substituted for x,y,z. For example, substitute x=p+q, y=r, z=s to remove rs from (p+q)r+(p+q)′s+rs. Complement the entire p+q, not only one input. The eliminated term may still serve a physical hazard-control purpose in a later chapter; functional redundancy and transient redundancy are different claims.

### Deliberate duplication

Idempotence permits duplicating a term when it helps form two combining pairs. For the canonical-style majority expression

<div class="formula-block">x′yz+xy′z+xyz′+xyz,</div>

duplicate xyz twice. Pair it separately with x′yz, xy′z, and xyz′. Those pairs reduce to yz, xz, and xy, yielding xy+xz+yz. A duplicate in an OR changes no output, so the proof is valid even though the intermediate expression is longer. Do not use arithmetic subtraction to "remove" the duplicated terms afterwards.

### Containment and safe local replacement

Define f≤g to mean every assignment satisfying f also satisfies g. Equivalently, fg′=0, fg=f, or f+g=g. Each characterization follows by checking whether any row has f=1 and g=0. The order is about on-set containment; it is not a numerical comparison of truth-table encodings.

An SOP product t is redundant in t+H exactly when t≤H, equivalently tH′=0. H may cover t using several terms collectively, even if no individual term contains t. In a POS, a factor s is redundant in sH exactly when H≤s. These directions are easy to reverse; reason from the rows where the term or remaining product equals one.

For example, yz is covered by xy+x′z because on yz=1 the value of x must be either zero or one, and one of those products then holds. This containment proof of consensus is as strong as the algebraic proof and often easier to visualize.

### Cancellation is generally invalid

From x+y=x+z you cannot infer y=z. Choose x=1,y=0,z=1: both original sides are one but the proposed conclusion is false. From xy=xz you cannot infer y=z; take x=0. Even x+x=0 cannot be treated as an arithmetic equation: Boolean idempotence reduces its left side to x. Cancellation becomes valid only under an additional condition such as fixing the common AND operand to one, or using XOR instead of OR.

An implication is not an identity. A product term may imply an expression without equaling it. Likewise, a transformation valid only under x=0 is not valid on the entire truth table. State assumptions on every conditional identity and check assignments outside the assumption before claiming a general law.

## 7. XOR, parity, equality, and the second algebra

### Deriving XOR rather than confusing it with OR

XOR is one when its inputs differ, so x⊕y=x′y+xy′. Also x⊕y=(x+y)(xy)′=(x+y)(x′+y′). Expanding the POS form leaves exactly the two differing-input products. XNOR, the complement of XOR, is xy+x′y′ and indicates equality of two bits.

XOR is commutative and associative. A chain of XORs is one exactly when an odd number of its inputs are one. Prove this by induction: appending a zero leaves the parity unchanged, and appending a one flips it. Therefore x⊕x=0, x⊕0=x, and x⊕1=x′. Unlike OR, XOR allows cancellation: if x⊕y=x⊕z, XOR both sides with x and use associativity to obtain y=z.

### AND distributes over XOR

The identity x(y⊕z)=xy⊕xz follows by splitting on x. If x=0, both sides are zero; if x=1, both sides are y⊕z. XOR does **not** distribute over AND in the corresponding OR-like manner: the proposed identity x⊕yz=(x⊕y)(x⊕z) fails at x=1,y=0,z=1. Its left side is one and its right side is zero. One distinguishing assignment refutes the identity, even if several other assignments agree.

OR and XOR agree on two expressions precisely when the expressions are never simultaneously one. Thus f+g=f⊕g exactly when fg=0. The two Shannon branch products satisfy that condition because one contains x and the other x′. General SOP products can overlap, so replacing OR by XOR indiscriminately is wrong.

### Boolean-ring representation and algebraic normal form

With XOR as addition and AND as multiplication, the two-element system is a field, often denoted GF(2). OR can be reconstructed as x+y=x⊕y⊕xy; NOT is x′=1⊕x. An **algebraic normal form**, or ANF, is an XOR of square-free products. It uses no literal complements, since each can be replaced by 1⊕x. This is a different normal form from an SOP using OR.

For two variables, write f=c₀⊕c₁x⊕c₂y⊕c₃xy. Evaluate at 00 to obtain c₀=f(0,0). At 10, c₁=f(1,0)⊕f(0,0). At 01, c₂=f(0,1)⊕f(0,0). At 11, c₃=f(1,1)⊕f(1,0)⊕f(0,1)⊕f(0,0). These equations give unique coefficients and prove that every two-input function has an ANF.

For any number of variables, if a<sub>S</sub> is the coefficient of the product indexed by subset S, evaluate the function with exactly the inputs in S set to one. The value is the XOR of coefficients indexed by all subsets of S. Solving subsets in increasing size determines each coefficient uniquely. Equivalently,

<div class="formula-block">a<sub>S</sub> = <math xmlns="http://www.w3.org/1998/Math/MathML"><mstyle displaystyle="true"><mrow><munder><mo movablelimits="false">⨁</mo><mrow><mi>T</mi><mo>⊆</mo><mi>S</mi></mrow></munder><mi>f</mi><mo>(</mo><msub><mn>1</mn><mi>T</mi></msub><mo>)</mo></mrow></mstyle></math>.</div>

Here 1<sub>T</sub> denotes the assignment whose one-valued inputs are exactly T. The big XOR ranges over every subset, including the empty subset. To check the formula, substitute the subset expansion: each lower coefficient appears an even number of times unless its subset is S itself, leaving exactly a<sub>S</sub>. This is the finite subset inversion behind the transform.

The algebraic degree is the largest number of distinct variables in a product with coefficient one. An affine function has degree at most one and has form c⊕a₁x₁⊕⋯⊕aₙxₙ. There are 2<sup>n+1</sup> affine scalar functions. There are 2<sup>n</sup> homogeneous linear ones, for which c=0. Do not call every Boolean function "linear" merely because it has a compact expression; xy has degree two.

## 8. Row selectors and expression completeness

### A row selector is a precise condition

Given a fixed input assignment, AND each input variable if that row contains one and its complement if the row contains zero. The resulting full product is one on that row and zero on every other row. For input order x,y,z, row 101 is selected by xy′z. OR the selectors for the output-one rows to construct an expression for a fully specified function. On any assignment, exactly one full row selector is one, so the construction returns exactly the specified output.

There is a dual construction for zero rows. For row 101, the sum term x′+y+z′ is zero exactly on that row. AND the corresponding sums for all output-zero rows. The resulting product is zero on exactly those rows and one elsewhere. Notice the reversal of complement convention: a selector product uses a true literal for a one-valued input, whereas the zero-selecting sum uses a complemented literal there.

These two constructions prove expression completeness for AND, OR, and NOT. They do not yet prove a minimum number of operations. They also explain constant cases: OR over no one rows is zero, and AND over no zero rows is one. The empty AND is one and the empty OR is zero; these conventions make the zero-input case consistent.

### Cubes and omitted literals

A consistent product fixing r distinct inputs out of n covers 2<sup>n−r</sup> rows because every other input is free. For example, xy′ in three variables covers 100 and 101. Its two full selectors combine as xy′z′+xy′z=xy′(z′+z)=xy′. This is algebraic combining before any map geometry is introduced.

A dash in a cube such as 10- means the third input is free inside that product condition. It does not mean that the output of the original specification is unconstrained on both rows. Keep a compressed input pattern separate from a don't-care output specification.

Contradictory products cover no assignments. Repeated literals do not add a new restriction. To apply the 2<sup>n−r</sup> formula, first remove duplicates and verify that no input appears in both polarities. A collection of products may overlap, so summing their row counts can overcount the on-set; union, not arithmetic addition, determines coverage.

## 9. Cofactors and Shannon decomposition

### Restriction is a new function

The cofactor f<sub>x=0</sub> is the function obtained by setting x to zero and retaining all other inputs as variables. Similarly define f<sub>x=1</sub>. A cofactor is generally a function of fewer variables, not a single number. Avoid the notation f<sub>x′</sub> unless its meaning is declared: it commonly denotes setting x to zero rather than complementing the function.

For f=xy+x′z+yz, setting x=0 gives z+yz=z, while setting x=1 gives y+yz=y. The two cofactors immediately expose the selector structure. This calculation also gives another proof that the yz term is redundant.

Restriction commutes with every truth-functional operation. For example, (fg)<sub>x=0</sub>=f<sub>x=0</sub>g<sub>x=0</sub>, and (f′)<sub>x=0</sub>=(f<sub>x=0</sub>)′. Both sides simply evaluate the same operation after making the same substitution. Restrictions on distinct variables commute, because assigning x and y in either order produces the same final assignment. Inconsistent restrictions on the same variable are not covered by that statement.

### Shannon's theorem in SOP and POS forms

The two identities are

<div class="formula-block formula-steps"><div>f = x′f<sub>x=0</sub> + xf<sub>x=1</sub>.</div><div>f = (x+f<sub>x=0</sub>)(x′+f<sub>x=1</sub>).</div></div>

For the SOP identity, when x=0 the first branch is the zero cofactor and the second vanishes; when x=1 the reverse occurs. For the POS identity, when x=0 the first factor becomes f<sub>x=0</sub> and the second becomes one; when x=1 the first becomes one and the second f<sub>x=1</sub>. These two-case proofs establish the formulas for every function, even when its original expression is large.

The signs in the POS form often cause confusion. Each factor becomes active when its standalone literal is **zero**. Thus the zero cofactor belongs with x, whereas the one cofactor belongs with x′. This is the reverse of the SOP branch literal. Never guess the POS formula from a superficial analogy.

<figure class="boolean-diagram"><svg viewBox="0 0 760 235" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="branch-title branch-desc"><title id="branch-title">Shannon decomposition separates two input slices</title><desc id="branch-desc">The x equals zero cofactor and x equals one cofactor feed a selector controlled by x. Only the selected slice contributes to f.</desc><rect x="24" y="26" width="215" height="75" rx="10" fill="#e5f2f8" stroke="#438297"/><rect x="24" y="133" width="215" height="75" rx="10" fill="#edf5e7" stroke="#708b53"/><text x="45" y="53">Hold the other inputs fixed</text><text class="math-label" x="45" y="84">f<tspan baseline-shift="sub" font-size="15">x=0</tspan></text><text x="45" y="160">Hold the other inputs fixed</text><text class="math-label" x="45" y="191">f<tspan baseline-shift="sub" font-size="15">x=1</tspan></text><path d="M239 65H380M239 170H380M490 118H700" fill="none" stroke="#438297" stroke-width="3"/><rect x="380" y="45" width="110" height="148" rx="12" fill="#fbf5e8" stroke="#ad9054"/><text x="397" y="78">Select zero</text><text x="397" y="164">Select one</text><text class="math-label" x="420" y="122">x</text><text class="math-label" x="565" y="105">f = x′f<tspan baseline-shift="sub" font-size="15">x=0</tspan> + xf<tspan baseline-shift="sub" font-size="15">x=1</tspan></text><text x="522" y="151">Only one branch can be active.</text></svg><figcaption>Figure 1. A cofactor retains the other inputs as variables. The selector recombines the two slices exactly. This is a functional diagram, with no delay or transistor model.</figcaption></figure>

### Repeated decomposition and uniqueness

Expand first on x and then each cofactor on y:

<div class="formula-block">f = x′y′f<sub>00</sub> + x′yf<sub>01</sub> + xy′f<sub>10</sub> + xyf<sub>11</sub>.</div>

The subscripts refer to the fixed order x,y. All four remaining functions depend only on the unassigned inputs. Continuing until every variable is assigned gives the complete row-selector expression. At every step, the coefficients are uniquely determined by restriction, even though simplification can produce multiple alternative expressions.

An input x is in the **essential support** of f exactly when f<sub>x=0</sub> and f<sub>x=1</sub> are different functions. If they are identical, Shannon reduces to (x′+x)f<sub>x=0</sub>=f<sub>x=0</sub>, so x is irrelevant. If they differ on some assignment to the other inputs, changing x on that assignment changes the output. A variable appearing in a written expression can still be absent from the function's essential support.

## 10. Boolean difference, quantification, and monotonicity

### Sensitivity to one input

Define the Boolean difference with respect to x as D<sub>x</sub>f=f<sub>x=0</sub>⊕f<sub>x=1</sub>. It is a Boolean function of the other inputs. A value of one means toggling x while holding all other inputs fixed changes the output. A value of zero means the output is insensitive to that toggle in that context. It is not a real-valued slope and does not predict a propagation delay.

The essential-support criterion is D<sub>x</sub>f≠0 as a function; a single zero sensitivity row does not make an input irrelevant. For f=xy+x′z, the difference is y⊕z. The selector input matters exactly when its two candidate values differ. For three-input majority, f<sub>x=0</sub>=yz and f<sub>x=1</sub>=y+z, so D<sub>x</sub>f=y⊕z as well. The same difference can arise from different functions; it does not uniquely identify the function.

Complementing the output leaves Boolean difference unchanged because complementing both cofactors preserves whether they differ. Difference distributes over XOR. Repeated differences on distinct inputs commute: both orders XOR the same four restricted values. Applying the difference twice to the same input gives zero, since the first result no longer depends on that input.

Do not use the ordinary product rule. With f₀=f<sub>x=0</sub>, g₀=g<sub>x=0</sub>, d=D<sub>x</sub>f, and e=D<sub>x</sub>g, we have f₁=f₀⊕d and g₁=g₀⊕e. Distribute AND over XOR to obtain

<div class="formula-block">D<sub>x</sub>(fg) = f₀e ⊕ g₀d ⊕ de.</div>

The extra de term is necessary. For f=g=x, the product is x, whose difference is one; the naive sum of two identical derivative terms would cancel and falsely give zero. For OR, use f+g=f⊕g⊕fg, giving D<sub>x</sub>(f+g)=f₀′e⊕g₀′d⊕de. These are Boolean identities, with the zero-cofactor convention explicitly fixed.

### Existential and universal elimination

Existential elimination asks whether **some** value of x makes the output one: ∃x f=f<sub>x=0</sub>+f<sub>x=1</sub>. Universal elimination asks whether **both** values do: ∀x f=f<sub>x=0</sub>f<sub>x=1</sub>. Both results are functions of the remaining inputs. They can be called smoothing and consensus with respect to x; the latter is related to, but not the same syntax as, deleting a consensus term in an SOP.

Extend each result back to the full input domain by ignoring x. Then ∀x f≤f≤∃x f. To prove maximality of the lower bound, let h be independent of x with h≤f. It must be contained in both cofactors, so h≤f₀f₁. Likewise, any x-independent upper bound must contain both cofactors and therefore their OR. These are the tightest bounds independent of the eliminated input.

For majority, existentially eliminating x gives y+z, universally eliminating it gives yz, and the difference is y⊕z. The four possibilities for the cofactor pair are especially informative:

| f₀ | f₁ | Universal result | Existential result | Difference | Interpretation |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | The output is always zero here. |
| 0 | 1 | 0 | 1 | 1 | The output follows x here. |
| 1 | 0 | 0 | 1 | 1 | The output follows x′ here. |
| 1 | 1 | 1 | 1 | 0 | The output is always one here. |

Existential quantifiers over distinct variables commute with one another, as do universal quantifiers. Mixed quantifiers generally do not commute: ∀x∃y(x XNOR y)=1, but ∃y∀x(x XNOR y)=0. In the first statement y may depend on x; in the second it must be chosen once for both values of x. Always specify the domain of quantification, which here is {0,1}.

### Unateness is a semantic property

A function is positive unate in x when changing x from zero to one can never make the output fall from one to zero. The exact condition is f₀≤f₁. It is negative unate when f₁≤f₀. An irrelevant input satisfies both conditions. An essential input satisfying neither is binate. A function is unate if an appropriate fixed polarity makes it monotone in each of its inputs.

A product-sum representation using x only in positive polarity is sufficient for positive unateness: changing x to one cannot invalidate a positive product that was already true. The existence of both polarities in a particular expression is **not** proof that the function is binate. For example, xy+x′y=y is independent of x despite the two written polarities. Decide the function's property by its cofactors, not by a redundant representation.

For a syntactically unate SOP cover with no constant-one term, choose each input to falsify its used literal polarity. Every nonempty product then has a false literal, so the expression is zero on that assignment and is not a tautology. Conversely, a constant-one term makes the SOP a tautology. The theorem concerns that unate **cover**; a semantically unate function written redundantly in both polarities does not meet the syntactic assumption until the representation is repaired.

### Carefully limited fault-model interpretation

For a primary input x modeled as stuck at zero, an assignment detects the fault at scalar output f exactly when x=1 and D<sub>x</sub>f=1. The first condition excites the fault; the second makes its effect observable. For stuck-at-one, require x=0 and the same sensitivity condition. This derivation compares the healthy output with the output under the wrong constant input.

The rule is exact for this specified primary-input stuck-at model. It is not automatically a rule for every internal wire fault, bridging fault, analog defect, or timing failure. Internal reconvergent structure can require a separately stated fault model. For multiple outputs, detection means at least one output differs, so OR the output-difference indicators. This model boundary prevents turning a useful algebraic fact into an unsupported physical guarantee.

## 11. Equivalence checking and constrained specifications

### An equivalence miter

To compare two functions f and g on the same input variables, define M=f⊕g. They are identical exactly when M is the constant zero function. A satisfying assignment for M is a concrete counterexample, with unequal outputs. For multiple outputs, use the OR of each corresponding XOR, not the XOR of all discrepancies: two errors could cancel in an aggregate parity.

Containment uses a related witness function: f≤g exactly when fg′ is identically zero. Tautology means f′ has no satisfying assignment, and contradiction means f has none. A solver or laboratory answer should give the counterexample assignment when possible; that assignment explains the failure and permits an independent check.

### Care sets and don't-care outputs

Let C be the care function specifying which input rows are constrained. Two candidate implementations are equivalent on the specification exactly when C(f⊕g)=0. Values outside C are free to differ. They are not unknown values that may be substituted into the algebra as a third truth value.

If d rows are unconstrained and all others are fixed, there are 2<sup>d</sup> scalar completions. Each unconstrained row may independently be assigned zero or one, unless additional constraints relate them. Choosing a completion can enable a simpler expression, but the choice must preserve every constrained row. A contradiction between two required outputs on one care row cannot be repaired by labeling a different row as a don't-care.

Conditional equivalence is transitive when the **same** care set is used. Equivalence under two different assumptions need not establish equivalence on their union. Explicitly state which rows each transformation preserves. The interactive laboratory below compares fully specified functions; it does not silently suppress inconvenient mismatches as don't-cares.

### Recursive proof by restriction

Two functions are equivalent exactly when both corresponding zero cofactors are equivalent and both corresponding one cofactors are equivalent. Apply Shannon to prove the reverse direction; the forward direction follows by substitution. A recursive checker can split on an input and repeat this argument until it reaches constants. Every split removes an unassigned variable, so the procedure terminates after at most n levels. Its naive worst case still visits exponentially many branches.

For a cube-list SOP representation, cofactoring a product is mechanical: remove a term if it conflicts with the selected assignment; remove the selected literal if it agrees; otherwise leave the term unchanged. Remove duplicates and absorbed products to reduce work, but do not assume these local operations always find a globally minimal cover. Heuristics that choose a variable with many opposite-polarity occurrences can make some examples smaller; they do not remove the worst-case exponential cost.

<figure class="boolean-diagram"><svg viewBox="0 0 760 270" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="proof-title proof-desc"><title id="proof-title">A complete restriction proof needs both branches</title><desc id="proof-desc">A miter is split on x into zero and one cofactors. One branch is already zero, and the other is split on y. All leaves must be zero for equivalence. Any nonzero leaf supplies a counterexample.</desc><g fill="none" stroke="#598194" stroke-width="2"><path d="M365 57L170 123M365 57L550 123M550 151L440 218M550 151L662 218"/></g><g fill="#edf5f8" stroke="#8cb2c2"><rect x="285" y="16" width="160" height="45" rx="8"/><rect x="80" y="115" width="180" height="48" rx="8"/><rect x="455" y="115" width="190" height="48" rx="8"/><rect x="385" y="214" width="110" height="40" rx="8"/><rect x="605" y="214" width="110" height="40" rx="8"/></g><text class="math-label" x="319" y="46">M = f ⊕ g</text><text class="math-label" x="103" y="146">M<tspan baseline-shift="sub" font-size="14">x=0</tspan> = 0</text><text class="math-label" x="478" y="146">M<tspan baseline-shift="sub" font-size="14">x=1</tspan></text><text x="170" y="89">Set zero</text><text x="465" y="89">Set one</text><text x="415" y="189">Set zero</text><text x="608" y="189">Set one</text><text class="math-label" x="425" y="242">0</text><text class="math-label" x="646" y="242">0</text><text x="20" y="208">Equivalence requires every leaf to vanish.</text><text x="20" y="236">A single mismatch refutes it.</text></svg><figcaption>Figure 2. This schematic shows the proof obligation, not the tree of every example. Repeated subfunctions can be shared in more advanced decision-diagram methods; no sharing or polynomial bound is assumed here.</figcaption></figure>

## 12. Interactive truth-table and cofactor laboratory

Enter two expressions over the inputs `x`, `y`, and `z`. Use `!` for NOT, `&` for AND, `^` for XOR, `|` for OR, and parentheses. Constants `0` and `1` are allowed. Operators are explicit: write `x & y`, not `xy`. The parser applies NOT first, then AND, then XOR, then OR. A local truth table evaluates all eight assignments and reports either equivalence or the first counterexample in binary row order.

Select an input to display the two cofactors, their Boolean difference, the universal result, and the existential result for the **first** expression. The other two inputs remain variable columns. The results also classify dependence and unateness with respect to the selected input. Change one expression to see precisely which rows fail; then relate those rows to an algebraic proof or counterexample.

<section class="boolean-lab" aria-label="Boolean expression comparison laboratory">
<div class="boolean-controls"><label>First expression<input id="bool-first" maxlength="300" value="(x & y) | (!x & z) | (y & z)" spellcheck="false"></label><label>Second expression<input id="bool-second" maxlength="300" value="(x & y) | (!x & z)" spellcheck="false"></label><label>Restrict this input<select id="bool-variable"><option>x</option><option>y</option><option>z</option></select></label><button type="button" id="bool-example">Load the majority example</button></div>
<p id="bool-status" role="status" aria-live="polite"></p><div class="boolean-table-wrap"><table id="bool-table"><caption>Complete comparison: fixed input order x, y, z</caption><thead><tr><th>x</th><th>y</th><th>z</th><th>First</th><th>Second</th><th>Mismatch</th></tr></thead><tbody></tbody></table></div>
<div class="boolean-table-wrap"><table id="bool-cofactors"><caption>Cofactors and functions of the cofactors</caption><thead></thead><tbody></tbody></table></div><p id="bool-classification"></p>
<p class="lab-note">Exact two-valued, steady-state evaluation only. All three inputs are enumerated even if an expression ignores one. The tool does not optimize circuits, model time, infer unspecified outputs, or evaluate programming side effects. Invalid syntax is rejected and previous result tables are cleared.</p>
</section>

The default example demonstrates consensus redundancy. The majority example demonstrates positive unateness and context-dependent sensitivity. To study a false cancellation, compare `x | y` with `x | z`; their equality on x=1 does not establish equality on x=0. To study XOR versus OR, compare `x ^ y` with `x | y` and identify the overlapping-input row.

When the selected input has identical cofactors, the classification is independent, which means both positive and negative unateness hold. When neither containment relation holds, the input is binate. The four-row cofactor table is the exact evidence for that classification; a label alone is not the explanation.
