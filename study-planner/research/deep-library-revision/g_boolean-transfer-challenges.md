## Ten solved synthesis and counting challenges

These are newly authored, medium-to-hard transfer problems. Each combines mechanisms instead of changing only one number in an earlier question. Solutions can be read immediately; no assessment is requested from the student.

### Challenge 1. Solve for every possible unknown Boolean function

**Task.** Find and count all $H(a,b)$ satisfying $a+H=a+b$, and then impose $aH=ab$ as a second requirement.

**Solution.** At $a=0$, the first equality becomes $H(0,b)=b$, fixing $H(0,0)=0$ and $H(0,1)=1$. At $a=1$, both sides of the OR equality are one, so either output is allowed at each of $10,11$. There are $2^2=4$ possible functions. In cofactor form every solution is
$$H=(\neg a)b+aK(b),$$
where $K$ is an arbitrary unary function. Its four possibilities are $0,1,b,\neg b$. This is why OR cancellation cannot prove $H=b$ from the first equality alone.

The second requirement gives $H(1,b)=b$ and is automatic at $a=0$. Thus the two requirements together fix both cofactors to $b$, leaving exactly the function $H=b$. The proof also explains the mechanism: the two equations expose complementary input slices rather than permit cancellation on a hidden slice.

### Challenge 2. Symmetry combined with self-duality

**Task.** Count symmetric self-dual scalar functions on $n$ inputs and evaluate the count at $n=5$ and $n=4$.

**Solution.** A symmetric function is determined by layer outputs $s_0,\ldots,s_n$. Complementing a word changes weight $k$ to $n-k$, so self-duality requires $s_{n-k}=1-s_k$. For odd $n$, the $n+1$ layers form $(n+1)/2$ distinct pairs, one free bit per pair:
$$N=2^{(n+1)/2}\quad\text{for odd }n.$$
At $n=5$ the layer pairs are $(0,5),(1,4),(2,3)$, giving eight functions. At even $n$, the central layer $k=n/2$ maps to itself and symmetry forces equal outputs on complementary words within that layer, while self-duality forces opposite outputs. Therefore no such function exists, giving zero at $n=4$.

The contradiction is not that an input word equals its own complement; for positive $n$ it does not. The contradiction comes from assigning one shared *layer* output to both complementary words. Separating those two levels is essential.

### Challenge 3. Count the monotone self-dual three-input functions

**Task.** Classify all functions that are both monotone in every input and self-dual on three inputs.

**Solution.** Monotonicity and self-duality force bottom output zero and top output one. Let $u_1,u_2,u_3$ be the outputs at the three singleton-one words. Self-duality fixes each opposite pair-layer output to the complement of its opposing singleton output. If two singleton outputs are one, say at100 and010, monotonicity requires output one at101 because100 is a subset of101. But101 complements010, whose output is one, so self-duality requires output zero there. This is impossible.

Thus at most one singleton can be true. With none true, all three pair outputs are one: this is majority. With exactly singleton $i$ true, the two pair sets containing $i$ are true and the opposing pair false: this is the projection $x_i$. Each listed function is visibly monotone and self-dual. There are exactly four: the three projections and majority. This is fewer than the sixteen self-dual functions and fewer than the twenty monotone functions; multiplying those two class counts would have no meaning.

### Challenge 4. A four-input voter in three representations

**Task.** Construct a function that is one when at least three of $a,b,c,d$ are one. Give its canonical one-row count, an SOP and its ANF.

**Solution.** The accepted words have weight three or four, so there are $\binom43+\binom44=5$ canonical minterms. An SOP is
$$F=abc+abd+acd+bcd.$$
Weight three activates exactly one triple; weight four activates all four and OR still gives one. For the ANF, constants, singleton and pair coefficients vanish because all corresponding low-weight outputs are zero. Each triple coefficient is one. The degree-four coefficient is the XOR of all sixteen outputs, namely the XOR of five ones, which is one. Therefore
$$F=abc\oplus abd\oplus acd\oplus bcd\oplus abcd.$$
At1111, the four triple terms XOR to zero and the final term restores one. Omitting that final monomial would produce exactly-three, not at-least-three. This independently authored variant follows the voter-specification mechanism in the Cambridge examples, with full coefficient derivation rather than a copied problem solution.

### Challenge 5. Find all essential variables without trusting the written cover

**Task.** For $F=xy+(\neg x)y+yz+(\neg y)z$, find a simplified expression, essential support, and the directions of dependence.

**Solution.** The first two products combine to $y$. The last two combine to $z$. Thus $F=y+z$. Its $x$ cofactors are both $y+z$, so $x$ is irrelevant despite appearing in opposite polarities. With respect to $y$, the cofactors are $F_{y=0}=z$ and $F_{y=1}=1$, giving $D_yF=\neg z$. Changing $y$ affects the output exactly when $z=0$, always in the increasing direction. Similarly $D_zF=\neg y$, and $z$ is positive unate and essential. The essential support is $\{y,z\}$.

The function still has eight rows when tabulated over the three named inputs. It has six true rows: the accepted $(y,z)$ contexts are01,10,11 and each has two $x$ values. A support size of two is not a request to silently discard the stated third table column.

### Challenge 6. Diagnose two-output equivalence under a care condition

**Task.** Compare $F=(a+b,ab)$ and $G=(a\oplus b,0)$. Find the full mismatch set and characterize care sets that make them equivalent.

**Solution.** The first coordinate mismatch is $(a+b)\oplus(a\oplus b)=ab$. The second is $ab\oplus0=ab$. The correct vector miter is their OR, hence $M=ab+ab=ab$. It is one exactly on11. XORing the discrepancies would instead give $ab\oplus ab=0$ and falsely declare full equivalence.

Under a care function $C$, equality requires $CM=Cab=0$. Therefore the care set may include any of00,01,10 but must exclude11. There are $2^3=8$ possible binary care functions satisfying that requirement, including the empty care set. If a nonempty care set is required, there are seven. These are counts of allowed care functions; the original two vector circuits remain nonequivalent on the full domain regardless of which alternative care set one later proposes.

### Challenge 7. Boolean product difference with a shared controlling variable

**Task.** Let $f=x\oplus y$ and $g=x\oplus z$. Find $D_x(fg)$ and all primary-input patterns detecting $x$ stuck at zero.

**Solution.** The zero cofactors are $f_0=y$, $g_0=z$ and the one cofactors are $f_1=\neg y$, $g_1=\neg z$. Hence
$$D_x(fg)=yz\oplus(\neg y)(\neg z)=\neg(y\oplus z).$$
The two products are disjoint, so this XOR is also their OR. A second route uses the zero-cofactor rule: $d=D_xf=1$ and $e=D_xg=1$, giving $f_0e\oplus g_0d\oplus de=y\oplus z\oplus1$. This matches XNOR. Omitting the last term would produce XOR and invert the sensitivity contexts.

To detect stuck-at-zero, healthy $x$ must be one and $y=z$ must make the derivative one. The patterns are100 and111. At100 the healthy product is one and the faulty product zero; at111 the healthy product is zero and the faulty product one. Excitation without propagation is insufficient: at101 or110 the product is zero in both circuits.

### Challenge 8. Care-restricted consensus and unsafe removal

**Task.** Compare $F=ab+(\neg a)c$ with $G=ab+c$. Derive an exact care condition for equivalence and decide whether $G$ is always a valid replacement.

**Solution.** At $a=0$, both functions are $c$. At $a=1$, $F=b$ and $G=b+c$, which differ exactly when $b=0,c=1$. Thus the mismatch is
$$M=a(\neg b)c.$$
The functions agree under care set $C$ exactly when $Ca(\neg b)c=0$. Full replacement is invalid because101 is a witness. For example $C=\neg a+b+\neg c$ excludes precisely that witness and allows replacement on all other rows.

This is not the consensus theorem: adding $bc$ to $F$ is always redundant, while replacing $(\neg a)c$ by $c$ adds the uncovered101 row. Removing a selector literal needs a coverage proof on the remaining region. A care specification can authorize that change, but an implementation's transient input assumptions must not be invented to manufacture a care set.

### Challenge 9. Quantifier order as a game of choices

**Task.** Let $R(x,y,z)=(x\oplus y)\Leftrightarrow z$. Compare $\forall x\exists y\,R$ and $\exists y\forall x\,R$ as functions of $z$.

**Solution.** For every fixed $x,z$, choose $y=x\oplus z$. Then $x\oplus y=z$ and $R=1$. Therefore existential elimination of $y$ produces one for either $x$, and $\forall x\exists y\,R=1$ for both $z$ values.

For a single fixed $y,z$, toggling $x$ toggles $x\oplus y$. It cannot equal the same fixed $z$ for both $x$ values. Hence the universal cofactor conjunction over $x$ is zero and $\exists y\forall x\,R=0$ for both $z$ values. The first order lets $y$ depend on $x$; the second commits to one $y$ before facing both $x$ choices. Neither operation can be changed to a favored witness substitution without preserving this dependency rule.

### Challenge 10. Count affine functions that are both symmetric and self-dual

**Task.** Count affine symmetric self-dual functions on five inputs, then on four inputs.

**Solution.** An affine function is $c\oplus\bigoplus_i a_ix_i$. Permuting two input positions must leave a symmetric function unchanged. Evaluating the two singleton words shows $c\oplus a_i=c\oplus a_j$, so all input coefficients are equal to one common bit $a$. Thus the symmetric affine possibilities are the two constants ($a=0$) and parity or complemented parity ($a=1$).

For $a=0$ the functions are constant and fail self-duality. For $a=1$, complementing all inputs changes parity by $n\bmod2$. It produces the required opposite output exactly when $n$ is odd, independently of $c$. Consequently there are two functions for five inputs and zero for four inputs. This is consistent with the broader symmetric/self-dual count of eight for five inputs: the affine requirement retains only two of those eight. A shared closed form such as $2^{n+1}$ for two different classes never proves those classes have identical membership.
