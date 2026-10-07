1. **A named random variable is a fixed map.** When a question gives elementary outcomes, compute the value on each outcome before assigning a law. In a two-die experiment, the pair and its sum are different objects. Losing the pair can lose dependence information needed for a later question.

2. **Convert values back into events.** To evaluate $P(X=x)$, identify every outcome in the fiber $\{\omega:X(\omega)=x\}$. If four outcomes with weights $(1,2,3,4)/10$ map to $(-1,2,-1,5)$, the mass at $-1$ is $4/10$, not two of four.

3. **Uniform elementary outcomes do not make all measurements uniform.** A maximum of two fair four-sided dice has masses $(1,3,5,7)/16$. Its fiber sizes differ. Use the fiber count divided by the elementary sample-space size only after verifying equal elementary probabilities.

4. **Discrete does not mean integer-valued.** A point mass at $\pi$ is discrete. Integer formulas using $F(k)-F(k-1)$ require integer support; the general jump formula $F(x)-F(x^-)$ works at arbitrary real atoms.

5. **A countable law can have accumulating atoms.** The values $1/k$ with masses $2^{-k}$ approach zero, but no mass remains at zero. Do not infer a continuous component from an accumulation point; check where probability is concentrated.

6. **Distinguish an atom set from its closure.** In that $1/k$ example, zero is in the closure but $P(X=0)=0$. If an examination uses the word support, identify its convention before declaring that every listed support point has positive mass.

7. **Check every sign separately from normalization.** A table $(\theta,1-3\theta,2\theta)$ sums to one identically but is valid only for $0\le\theta\le1/3$. A solved sum equation does not certify nonnegative probabilities.

8. **Strictly positive support changes endpoint parameter cases.** Three positive masses in the preceding table require $0<\theta<1/3$. At either endpoint the law remains valid, but the effective atom set shrinks. Match strict versus nonstrict parameter wording.

9. **A normalizer cannot repair negative weights.** Dividing weights $(1,2,-1,2)$ by their total four leaves a negative mass. Nonnegativity is necessary before interpreting normalization as a probability construction.

10. **Finite sums require the full declared support.** For weights $k+1$ on $k=0,\ldots,4$, the total is 15. Dropping zero's weight because zero has value zero confuses the mass sum with a value-weighted moment sum.

11. **Infinite normalization needs a limit.** For $1/[k(k+1)]$, partial mass through $m$ is $1-1/(m+1)$. Its remaining tail is positive, but tends to zero. A finite plot need not contain all probability when it is explicitly labelled a prefix.

12. **Nonnegative sums may be regrouped by fibers.** The identity $p_{g(X)}(y)=\sum_{g(x)=y}p_X(x)$ relies on disjoint atom events and nonnegative probability terms. It does not need continuity or derivatives.

13. **PMF heights are already probabilities.** A discrete stem at $x$ has height $P(X=x)$. Do not multiply it by a bin width as if it were a density histogram. Unequal spacing between atoms does not change their masses.

14. **A CDF is defined off support too.** With atoms at $-2,1,4$, $F(2.5)=F(1)$. Interpolating between CDF levels invents probability where the discrete law has none.

15. **A jump's value includes its atom.** Since $F(t)=P(X\le t)$, the right-continuous value at a jump is the upper level. A function zero for $t\le0$ and one for $t>0$ is not the CDF of a mass at zero.

16. **Use the left limit for strict lower events.** $F(t^-)=P(X<t)$. For a law with positive mass at $t$, this differs from $F(t)$. Replacing a strict event by a nonstrict one changes the answer by exactly that atom's mass.

17. **Recover an atom by a jump difference.** $P(X=t)=F(t)-F(t^-)$. If $P(X<2)=1/3$ and $P(X>2)=1/4$, the mass at two is $5/12$. The two tails and the atom partition the whole experiment.

18. **The integer difference has a precise condition.** For integer-valued $X$, $p(k)=F(k)-F(k-1)$. On support $\{0,1/2,1\}$, using a unit backward step at one would also include the mass at one-half.

19. **An open-lower, closed-upper interval uses ordinary CDF subtraction.** For $a<X\le b$, subtract $F(a)$ from $F(b)$. This removes all outcomes at or below $a$, including its atom.

20. **A closed lower endpoint needs a left limit.** For $a\le X\le b$, use $F(b)-F(a^-)$. With masses $(.2,.5,.3)$ at $(-2,1,4)$, the event $1\le X\le4$ has mass $.8$, not $.3$.

21. **A strict upper endpoint also needs a left limit.** The event $a<X<b$ has probability $F(b^-)-F(a)$. A diagram's closed dot at $b$ belongs to the CDF value but must be excluded from this event.

22. **Both half-open directions have different formulas.** The event $a\le X<b$ has mass $F(b^-)-F(a^-)$. Check the lower and upper atoms separately rather than relying on a memorized single interval formula.

23. **For integer support, ceiling and floor encode real bounds.** The event $.2\le X\le3.9$ includes integers one, two, three. Use $F(3)-F(0)$; nearest-integer rounding can wrongly admit zero or four.

24. **Empty feasible intervals have zero mass.** If no integer satisfies the supplied bounds, do not accept a negative CDF subtraction from reversed limits. Establish the ordered feasible atom set first.

25. **At least is not strictly greater.** For integer $r$, $P(X\ge r)=1-F(r-1)$ while $P(X>r)=1-F(r)$. Their difference is $p(r)$, so a positive atom makes an off-by-one tail error visible.

26. **Every real-variable CDF must reach one in the limit.** A curve that remains $.8$ forever is incomplete or invalid. A disclosed $.2$ tail at later finite atoms can repair a prefix; putting that mass at infinity changes the type of variable.

27. **Monotonicity cannot replace right continuity.** A proposed function can be bounded, nondecreasing, and have limits zero and one yet fail at a jump value. Test the value against the limit from the right at every piecewise boundary.

28. **A continuous increasing segment excludes a purely finite-atom law.** A truly linear CDF rise across an interval is not a finite sequence of atom jumps. A smoothed drawing of a discrete CDF must not be interpreted as its exact mathematical graph.

29. **CDF differences determine interval mass, not allocation within it.** If $F(1)=.2,F(4)=.8$, then $.6$ is allocated among integers two, three, four. Any one of those masses can range from zero through $.6$ unless extra constraints are given.

30. **Lower quantiles select the first cumulative level reaching the target.** For cumulative levels $.2,.7,1$, a target $.7$ selects the second atom. A jump can overshoot the target, so $F(Q(u))=u$ need not hold.

31. **An inverse sampler must choose an endpoint contract.** Half-open intervals on $[0,1)$ use the first cumulative value strictly exceeding $U$. At $U=.2$, the second interval begins. The lower-quantile convention differs on exact boundaries but agrees in law for an ideal continuous uniform input.

32. **Reject uniform input outside the sampler's domain.** With a $[0,1)$ contract, input one is invalid. Silently selecting the final atom hides an implementation error; finite digital boundary tests deserve explicit handling.

33. **Simulation frequencies are estimates under their sampling model.** A short run need not match a theoretical PMF exactly. Proving a sampler's distribution requires its interval-length or event construction, not a histogram that happens to resemble the expected bars.

34. **A nonlinear measurement adds colliding preimages.** For $Y=X^2$, the mass at positive $y$ is the sum over both supported square roots. At zero, there is only one preimage; do not double-count it.

35. **Solve a transform equation within the given support.** Algebraic roots outside the source atom set contribute zero. The quadratic $X(X-1)$ can map pairs of integer inputs to the same value; evaluate all valid roots before claiming uniformity.

36. **A negative affine scale reverses both order and inequalities.** For $Y=aX+b$ with $a<0$, $F_Y(t)=1-F_X(((t-b)/a)^-)$. The left limit retains boundary mass that belongs to $Y\le t$.

37. **A zero affine scale is a separate deterministic law.** When $a=0$, all mass lies at $b$. Inverting by dividing by $a$ would be undefined. A degenerate transformation cannot be treated using the nonzero-scale formulas.

38. **Equal PMFs do not determine an equality event.** Fair bits $B$ and $1-B$ have the same law but never agree. Two independent fair bits agree with probability $1/2$. The joint construction distinguishes them.

39. **A single coincident event probability does not establish equal laws.** For a uniform three-value $X$, independent $X+Y$ and the copy sum $2X$ both have mass $1/3$ at four, but only the independent sum can be three. Compare the whole law or a separating event.

40. **Pairwise independence is weaker than mutual independence.** The triple $(A,B,A\mathbin{\oplus}B)$ of fair bits has independent pairs but count support only zero and two. A three-trial binomial requires the full joint factorization.

41. **A Bernoulli indicator can represent a complicated event.** If $A$ is a threshold or a multistage success,$1_A$ is still Bernoulli with parameter $P(A)$. The distribution concerns its binary output, not the complexity of the experiment.

42. **Repeating one indicator does not create two trials.** For $I+I$, only zero and two are possible. A nondegenerate $\operatorname{Bin}(2,p)$ also has mass at one. Identify whether the problem repeats a variable or independently generates a copy.

43. **Discrete uniform denominators count endpoints.** Uniform integers $a$ through $b$ have $b-a+1$ atoms. For $-4$ through 8, the denominator is 13. Congruence or parity conditions select a subset of those actual integers.

44. **Modulo maps need equal fiber counts to preserve uniformity.** Uniform $0,\ldots,10$ modulo 4 gives masses $(3,3,3,2)/11$. Extending to 11 balances the fibers. The output label count alone cannot supply equal probabilities.

45. **Binomial recognition needs four experiment properties.** There must be a fixed $n$, mutually independent binary trials, a common success probability $p$, and a success count. Without these, derive the actual law rather than using the family name.

46. **An exact binomial count includes failures.** Exactly $k$ successes has factor $p^k(1-p)^{n-k}$. Omitting the failure factor counts selected success witnesses, whose events overlap when additional successes occur.

47. **At least tails sum disjoint exact counts.** $P(X\ge r)=\sum_{k=r}^np(k)$. When $r$ is small, the complement through $r-1$ can be shorter. For a two-server threshold, network failure includes both zero and one working server.

48. **Binomial endpoint parameters shrink support.** At $p=0$, the count is zero surely; at $p=1$, it is $n$ surely. Avoid uncontrolled $0^0$ evaluations in code, and exclude zero-mass ratios from adjacent-probability manipulations.

49. **An empty block has zero successes.** The $n=0$ binomial law has one atom at zero. Every normalization and parity identity must agree with that interpretation; an empty experiment is not an undefined count.

50. **Adjacent binomial ratios expose hidden parameters.** For $0<p<1$, $p(k+1)/p(k)=((n-k)/(k+1))(p/(1-p))$. Setting such a ratio to a supplied value can eliminate factorials and powers before solving for $p$.

51. **Binomial mode ties occur at an exact integer boundary.** If $(n+1)p=m$ is integer, the modes are $m-1,m$. For $n=9,p=.4$, these are three and four. Rounding $np$ is not the exact mode rule.

52. **Binomial even-count probabilities need not be one-half.** The formula is $[1+(1-2p)^n]/2$ for $n\ge1$. It follows by adding the normalized and signed expansions. At $p=1/4,n=4$, the answer is $17/32$.

53. **Two-stage eligibility can be collapsed per object.** Independent qualification $a$ followed by conditional success $b$ gives per-object success $ab$. Across independent objects, the final count is $\operatorname{Bin}(n,ab)$. Retain the qualification event when defining success.

54. **Conditioning on the eligible count provides an independent derivation.** Sum $P(K=k)P(Y=r\mid K=k)$ over feasible $k$. Replacing $K$ by its mean changes the experiment and generally loses the correct count law.

55. **Independent unequal probabilities produce a Poisson-binomial count.** Multiply $\prod_j((1-p_j)+p_jz)$ or propagate dynamic probability rows. Averaging the $p_j$ can preserve a mean while changing individual count masses.

56. **A common random probability creates a mixture.** Choosing one coin for an entire block makes later tosses dependent after the regime is hidden. Average conditional laws; do not substitute the average $p$ into one binomial without proving unconditional independence.

57. **The timing of a latent choice is decisive.** Reselecting an independent coin before each toss can make fair independent outcomes; selecting once can give masses $(5,6,5)/16$ on a two-toss count. State which random choice is shared.

58. **A stopped series can use an imagined fixed horizon correctly.** Pre-generate the unplayed outcomes and compare the final majority event. That construction can prove a winning probability, but it does not make the actual stopping-time distribution binomial.

59. **Hypergeometric parameters are finite integers.** Require $0\le K\le N$ and $0\le n\le N$. A numerical root for $K$ outside this integer range cannot describe the population, even if it solves an algebraic probability equation.

60. **Hypergeometric lower support is often positive.** The bound $k\ge\max(0,n-(N-K))$ forces successes when failures cannot fill the sample. Drawing seven of eight objects with three successes forces at least two marked objects.

61. **The hypergeometric numerator chooses both categories.** Use $\binom Kk\binom{N-K}{n-k}$ over $\binom Nn$. Omitting the failure choice or using $n!$ as the denominator counts a different collection of elementary objects.

62. **Without-replacement sequential probabilities change with the state.** After $j$ draws and $k$ successes, the next success chance is $(K-k)/(N-j)$. A constant $K/N$ at every draw silently inserts replacement.

63. **Ordered and unordered derivations can agree without sharing denominators.** For four successes among ten and three draws, the three two-success patterns each have mass $1/10$. Their sum $3/10$ matches the subset formula $36/120$.

64. **Observed urn draws update both composition and remaining target.** Given a first success, the remaining successful-object count decreases by one, and a target total of two requires one more success. Reusing the original parameters ignores the observation.

65. **Geometric trial count starts at one; failure count starts at zero.** $T=G+1$ implies $P(T=t)=pq^{t-1}$ and $P(G=g)=pq^g$. A family name without its convention is incomplete information.

66. **Geometric survival counts prior failures exactly.** For integer $m\ge0$, $P(T>m)=q^m$ and $P(T\ge m+1)=q^m$. At least four total attempts needs three initial failures, not four.

67. **A real geometric threshold uses a floor.** For $x\ge1$, $F_T(x)=1-q^{\lfloor x\rfloor}$. A threshold 3.9 admits times through three. A continuous interpolation changes the law.

68. **Geometric properness requires positive success probability.** At $p=0$, finite stopping masses sum to zero and nontermination is certain. At $p=1$, waiting is immediate; conditioning on later survival is impossible.

69. **Memorylessness is conditional on a nonzero survival event.** Cancel $q^s$ only when $P(T>s)>0$. The remaining iid trials then give $P(T>s+t\mid T>s)=q^t$. Do not retain a factor charging failures already observed.

70. **Varying independent hazards do not give geometric memorylessness.** Survival is $\prod_{j=1}^m(1-p_j)$. Independence supports the product, but a common $p$ is needed for a fixed geometric power and elapsed-time invariance.

71. **Capping accumulates the whole tail into the last atom.** For $W=\min(T,c)$, $P(W=c)=q^{c-1}$. This includes success at $c$ and all later stopping times. Using $pq^{c-1}$ would omit censored nontermination-by-cap histories.

72. **Conditioning on success by a cap instead renormalizes.** Divide $pq^{t-1}$ by $1-q^c$ for $t=1,\ldots,c$. This differs from capping; for fair trials with $c=4$, the final probabilities are $1/15$ and $1/8$ respectively.

73. **A distinct no-success output preserves a separate mass.** With $c$ attempts, the no-success code has mass $q^c$, while success on the final attempt has mass $pq^{c-1}$. State whether the output merges or distinguishes them.

74. **Negative-binomial stopping forces the final success.** For total trials through $r$ successes, use $\binom{t-1}{r-1}p^rq^{t-r}$. Choosing $r$ positions from all $t$ would allow a failed last trial after an earlier completion.

75. **Failures and total trials differ by $r$, not one.** $G_r=T_r-r$. Substitute $t=g+r$ before selecting the coefficient $\binom{g+r-1}{r-1}$. The one-success geometric offset is only the $r=1$ special case.

76. **A fixed-time binomial event answers a negative-binomial CDF.** $T_r\le m$ if and only if at least $r$ of the first $m$ trials succeed. This gives the correct tail while preserving the different support and meaning of $T_r$.

77. **Poisson parameters belong to a specified observation window.** Under a supplied homogeneous rate model, convert units and use $\lambda=rt$. A stated average count alone does not prove a Poisson law. Normalization comes from the exponential series.

78. **Poisson adjacent ratios determine modes and parameters.** $p(k+1)/p(k)=\lambda/(k+1)$. At positive integer $\lambda=m$, two modes $m-1,m$ tie. The zero-parameter law is a separate point mass with one mode.

79. **A Poisson approximation is not a finite identity.** $(1-1/n)^n$ approaches $e^{-1}$ but differs at every finite $n>1$. A displayed finite prefix also has a genuine omitted tail; renormalizing it produces a conditional law rather than the original Poisson.

80. **Validate the whole experiment before transferring a formula.** Joint independence enables convolution products and maximum-CDF products; support permits legal indices; nonzero conditioning mass permits division; finite-moment assumptions govern expectation later. Use an explicit counterexample such as all devices succeeding together to diagnose which missing condition changes the answer.
