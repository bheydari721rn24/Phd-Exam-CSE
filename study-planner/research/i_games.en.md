# Adversarial Search and Pruning

Author-review draft. Study the teaching sections before the worked-problem bank. Exact values, one-sided bounds and policy-dependent estimates are distinguished throughout. The edition remains subject to student review.

## 1. Written university foundations and learning boundary

The primary written foundations are Stanford CS221 Spring2026 Games modules, Berkeley CS188 textbook Games sections3.2–3.5, MIT6.034 Fall2010 Lecture6 transcript by Patrick H. Winston, and Cornell CS4700 Fall2018 adversarial-search slides by Bart Selman. CMU15-281 Fall2025 material by Pat Virtue contributes additional mathematical examples and opponent-model questions. The [written-source comparison](../reviews/i_games-sources.html) gives exact links, actually read sections, acquisition fingerprints, comparisons with Harvard/Yale and independently checked source corrections.

This chapter studies decisions in finite game trees, accurate pruning, resource-limited evaluation, known stochastic opponents and introductory extensions. It assumes basic recursion, inequalities, induction and finite expectation. It teaches each new game-search concept before using it. A mixed-strategy equilibrium in a simultaneous game, a partially observable stochastic game and an arbitrary infinite cyclic game are different mathematical problems; ordinary minimax on a finite fully observed tree does not by itself solve them.

The central skill is to justify a decision using exactly the information available. A completed search may establish an exact value. A pruned search may establish only a one-sided bound. A heuristic evaluates a model approximately. A sample estimates a policy's outcome statistically. These are different kinds of evidence, and the distinction controls both a correct exam solution and a correct program.

## 2. States, turns, actions and strategies

A **state** contains enough information to determine legal actions, successor states and all future payoffs under the game's rules. Write $A(s)$ for its finite legal-action set and $T(s,a)$ for the successor after action $a$. A terminal predicate tells us when play has ended, and $u(s)$ assigns a terminal utility from one permanently designated player's perspective. We call this player MAX. In a two-player zero-sum game the other player's utility is $-u(s)$, so that player's decisions minimize MAX's utility.

The state must record whose turn it is. Two identical board arrangements with different players to move usually have different legal choices and values. Rule-dependent information also belongs in the state. For chess, piece placement and side to move alone can omit castling rights, an en-passant possibility or history relevant to a draw rule. A program may use a compressed representation, but compression must preserve every distinction needed by the model.

A node in a search tree represents a particular history reaching a state. Different histories may lead to the same state; these nodes are called transpositions. A state graph merges them, whereas an unfolded game tree repeats them. A finite state space does not imply a finite unfolded tree: a legal cycle can produce indefinitely many histories. Termination therefore requires a finite horizon, terminal/repetition rules, a suitable solved cyclic-game method, or another explicitly stated condition.

A **deterministic strategy**, or policy, selects a legal action at every state controlled by that player. A stochastic policy assigns probabilities $\pi(a\mid s)\ge0$ summing to one over legal actions. A policy is a contingent plan: it must say what to do after each possible opponent response, including responses that do not lie on the principal line currently expected.

A **root action** is one immediate decision. A **principal variation** is one sequence obtained by following selected optimizing actions. A **value function** assigns values to states. None is automatically a complete stored strategy. If a question asks for a strategy, specifying a single attractive root-to-leaf path is generally insufficient.

## 3. Backward induction and the minimax recurrence

First suppose the game tree is finite, all states are fully observed, transitions are deterministic, there are two opposing utility objectives and every nonterminal node has at least one legal action. Scores always remain in MAX's coordinates, including during MIN's turn. Define

$$V(s)=\begin{cases}u(s),&s\text{ is terminal},\\ \max_{a\in A(s)}V(T(s,a)),&s\text{ is a MAX node},\\ \min_{a\in A(s)}V(T(s,a)),&s\text{ is a MIN node}.\end{cases}$$

To evaluate a tree, begin at terminal leaves and repeatedly replace a MAX node by its largest child value and a MIN node by its smallest. The action is an optimizing argument, not the numerical value itself:

$$a^*(s)\in\operatorname{argmax}_{a\in A(s)}V(T(s,a))$$

at MAX, with argmin at MIN. Argmax can contain several actions. An implementation that returns one must specify how ties are handled.

**Why the recurrence is correct.** Prove the claim by induction on the maximum number of edges remaining to a terminal node. At height zero, the only payoff is the stated terminal utility. Assume the recursive value and corresponding guarantee are correct for every child. At a MAX node, MAX can choose a child with largest value and thereafter use that child's guaranteeing strategy. This secures at least the displayed maximum. No first action can secure a larger amount because the opponent can use its minimizing continuation in the selected child. The MIN case reverses the inequalities. Hence the recurrence gives an achievable guarantee and a matching adversarial upper bound at every node.

The induction also constructs a policy at every controlled node by recording a corresponding optimizing action. Randomization cannot improve MAX's worst-case guarantee in this finite, sequential, fully observed, two-player model: a distribution over first actions has expected value no greater than its largest supported child value. This conclusion does not extend to simultaneous hidden choices such as rock-paper-scissors.

Let $J(\pi,\sigma)$ denote MAX's payoff under MAX policy $\pi$ and MIN policy $\sigma$. For the exact policies constructed above,

$$J(\pi,\sigma^*)\le J(\pi^*,\sigma^*)=V(s_0)\le J(\pi^*,\sigma).$$

The left inequality says another MAX policy cannot beat the minimizing policy's restriction. The right inequality says MAX's policy retains its guaranteed payoff against any legal opponent policy. It does not say this policy maximizes average payoff against every weak or random opponent.

## 4. A complete deterministic calculation

Consider three actions leading to MIN nodes with terminal children $(4,11,-2)$, $(6,3,9)$ and $(5,8,7)$. Their exact values are $-2$, $3$ and $5$. MAX therefore chooses the third action and the root value is5. It is incorrect to choose the branch containing11: that leaf is controlled by an opponent who can instead choose-2.

The principal variation for an optimizing pair of strategies takes the third action and then the leaf5. MAX still needs appropriate continuation choices in larger trees if MIN deviates elsewhere. In this two-ply example the only MAX decision is at the root, so the root action happens to determine MAX's entire nontrivial policy; that coincidence is not a general rule.

To verify a numerical answer, compute every internal backup explicitly, label its controlling player, and identify the child attaining the value. A path alone cannot certify that all relevant alternatives are no better. A proof of a lower bound must show how MAX can enforce it; a proof of an upper bound must show how MIN can restrict play to it.

## 5. What exhaustive minimax costs

Use $D$ for the number of individual plies, meaning edges on a root-to-leaf path. One move by MAX followed by one move by MIN is two plies. Some sources call that pair one unit of depth; their exponent $2d$ becomes our $D$. Count what the question asks before substituting a formula.

For a complete $b$-ary tree with every leaf at ply $D$, the leaf count is $b^D$ and the total node count is

$$1+b+\cdots+b^D=\frac{b^{D+1}-1}{b-1}\quad(b>1).$$

For $b=1$, the tree is a chain with one leaf and $D+1$ nodes. If a node evaluation costs $c$ and successor generation has a nonconstant cost, those costs must be included separately; counting leaves as unit operations silently assumes an appropriate cost model.

Depth-first minimax takes $O(b^D)$ time in the complete fixed-branching model. Storing all siblings at each of $D$ active levels uses $O(bD)$ state storage. Generating one successor at a time can reduce auxiliary recursion storage to $O(D)$, provided state mutation/restoration or persistent-state storage has the stated cost. Materializing the entire tree uses exponentially more memory. Thus different space bounds can describe different implementations without disagreement about minimax itself.

With varying branching factors $b_0,\ldots,b_{D-1}$ that are uniform within each level, the leaf count is their product. If branching varies separately at individual nodes, multiply-along-one-path is not the whole leaf count; sum the descendant counts recursively.

## 6. Pruning begins with a decision certificate

Suppose MAX has already fully evaluated an action with value5. It now examines an alternative MIN node. The first evaluated child has value3. Whatever the remaining child values are, the MIN node's value is at most3. MAX can retain its known5, so the unexplored remainder cannot improve the root decision.

Notice the logical output: the alternative has value **at most3**. Its exact value might be3,0 or-100. The algorithm need not know which to reject that action. Writing an exact3 on a partially searched node is not justified merely because the routine returns the number3.

The dual situation occurs when a MIN ancestor can already obtain7 and a descendant MAX node has found a child worth9. That MAX node can reach at least9, so the minimizing ancestor can reject the route through it. Other children of the MAX node need not be evaluated. Here the result is a **lower bound**.

A useful certificate compares the current branch with alternatives at any relevant ancestor, not just its parent. A distant MAX ancestor's existing option can justify pruning below intervening MIN and MAX levels. This is why a correct implementation carries thresholds down the recursion.

## 7. Alpha, beta and an exact return contract

An alpha-beta call receives an initial window $(\alpha_0,\beta_0)$ with $\alpha_0<\beta_0$. These numbers encode alternatives that make the current subtree irrelevant outside that interval. They are decision thresholds. They are **not necessarily bounds enclosing the current subtree's true minimax value**: calling a subtree with alpha5 can legitimately discover that its exact value is-20.

The fail-soft convention returns a numerical score $r$ that can exceed the window. A conservative interpretation is:

$$r\le\alpha_0\Longrightarrow V(s)\le r,\qquad \alpha_0<r<\beta_0\Longrightarrow V(s)=r,\qquad r\ge\beta_0\Longrightarrow V(s)\ge r.$$

An exact terminal score outside the window still satisfies the corresponding weaker bound. Thus a flag derived only from the window can conservatively classify it as upper/lower even though the leaf itself is exact. More detailed implementations may retain stronger evidence, but they must prove it.

At MAX, update the working score from examined children, tighten alpha, and stop when alpha reaches beta. At MIN, tighten beta and stop on the same inequality. A root call with $(-\infty,+\infty)$ returns the exact minimax value for finite leaf utilities. A narrower call may correctly return only a bound. Fail-hard implementations clamp a cutoff result to a threshold; their return numbers differ, so trace questions must specify the convention.

**Why cutoffs preserve the root value.** A MAX cutoff is justified once an explored continuation proves that this branch can reach at least a value the relevant MIN ancestor can already avoid. A MIN cutoff is the symmetric restriction against a MAX ancestor's existing option. Removing further work in that branch therefore cannot change the ancestor's optimizing decision value. Apply the same reasoning inductively through the depth-first recursion. No claim is made that every discarded subtree's exact value has been recovered.

For a precise recursive proof, retain the three-part return contract above as the induction hypothesis. On a MAX node, a child return below the incoming alpha is only an upper certificate and cannot establish an improvement above alpha. A return inside the window is exact and can raise alpha. A child return reaching beta supplies the lower certificate needed for cutoff. The MIN case interchanges upper/lower and the threshold roles. Once all children have been processed without a cutoff, an interior result is exact; a result outside the original window supplies the appropriate one-sided certificate. This proof avoids the erroneous assumption that every partial working score is always an exact child backup.

## 8. A complete implementable search

The following routine assumes a finite deterministic tree, finite utilities, nonempty children at nonterminals, and a depth budget counted in individual edges. `state.kind` determines control, so an extra turn does not require changing score signs. `evaluate` returns an estimate in MAX's coordinates. Setting the budget beyond every terminal leaf yields exhaustive minimax with pruning.

```python
from math import inf

def alphabeta(state, plies, alpha=-inf, beta=inf):
    if isinstance(plies, bool) or not isinstance(plies, int) or plies < 0:
        raise ValueError("The ply budget must be a nonnegative integer")
    if not alpha < beta:
        raise ValueError("The incoming window must be strictly ordered")
    if state.terminal:
        return state.utility
    if plies == 0:
        return evaluate(state)
    if state.kind == "MAX":
        value = -inf
        for child in ordered_children(state):
            value = max(value, alphabeta(child, plies - 1, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    if state.kind == "MIN":
        value = inf
        for child in ordered_children(state):
            value = min(value, alphabeta(child, plies - 1, alpha, beta))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value
    raise ValueError("This routine handles deterministic MAX/MIN nodes only")

def choose_max_action(state, plies):
    if (isinstance(plies, bool) or not isinstance(plies, int)
            or plies < 1 or state.terminal or state.kind != "MAX"):
        raise ValueError("A legal root decision requires a nonterminal and one ply")
    best_action = None
    best_score = -inf
    for action, child in ordered_actions(state):
        score = alphabeta(child, plies - 1, best_score, inf)
        if best_action is None or score > best_score:
            best_action, best_score = action, score
    return best_action, best_score
```

Terminal testing precedes the depth cutoff. Otherwise a known win at the boundary might incorrectly receive a heuristic score. The two child iterators are abstract interfaces, not hidden algorithmic steps: each yields legal successors in a declared order. A mutable implementation must undo a move before visiting a sibling, including after a cutoff or exception. Validate a nonnegative integral depth at the public input boundary.

The root wrapper deliberately retains the first action on equality. After the first exact incumbent is known, another child called with that alpha can return an upper bound equal to the incumbent even when the child's true value is smaller. Replacing the incumbent on `>=` can then select an inferior action. To enumerate every truly optimal action, re-search equality candidates with a sufficiently wide window or retain a proof of exact equality; a returned number alone is insufficient.

## 9. Tie handling and an instructive counterexample

Let a MAX root's first action be an exact terminal value5 and its second action be a MIN node whose ordered terminal children are5 and0. With equality pruning, the second call receives alpha5. After seeing its first child5, MIN can stop and return5 as an upper bound. Its actual value is0. The correct root action remains the first, and the exact root value is5.

This example explains three superficially conflicting statements. Alpha-beta preserves the minimax root value. Equality pruning can hide additional tied optimal actions. A numerically tied return need not represent a tied optimal action at all. Each is true under the appropriate statement of what has been computed.

If an examination explicitly forbids pruning on equality, use strict cutoff inequalities and count more leaf visits where required. That convention changes work and trace details; it does not change the exhaustive root minimax value. State the convention before identifying pruned edges.

## 10. Ordering and exact best-case counts

Good ordering means trying high-value successors early at MAX and low-value successors early at MIN. This tends to establish useful rejection thresholds sooner. An ordering heuristic can be imperfect without changing the exact root result, provided it only reorders legal children and the underlying finite search remains complete. Dropping moves because they look weak is a different, potentially approximate algorithm.

Worst-case alpha-beta still examines all $b^D$ leaves. Under perfect ordering in a complete uniform $b$-ary tree with leaves exactly $D$ plies below the root, the minimum number of examined leaves is

$$L_D=b^{\lceil D/2\rceil}+b^{\lfloor D/2\rfloor}-1.$$

For even $D=2k$, this is $2b^k-1$; for odd $D=2k+1$, it is $b^{k+1}+b^k-1$. Therefore $O(b^{D/2})$ expresses the even-depth exponent improvement; it is not an exact count for every parity, incomplete tree or child order.

One way to derive the formula classifies ideal-order searches as principal, cutoff and all-children cases. At depth zero each costs one leaf. Let their costs be $P_D,C_D,A_D$. The principal case searches its first child as principal and the other $b-1$ children as cutoff cases. A cutoff case needs one refuting child; an all-children case must refute all $b$ children. Thus

$$P_D=P_{D-1}+(b-1)C_{D-1},\qquad C_D=A_{D-1},\qquad A_D=bC_{D-1}.$$

The last two relations give $C_D=b^{\lfloor D/2\rfloor}$. Substitute into the first relation and sum its increments. Pairing successive equal powers yields the displayed expression for $P_D=L_D$. These recurrences describe an ideal complete-tree certificate with an appropriate ordering, not the cost of every tree with the same branching factor.

With MAX branching $n$, MIN branching $m$, and $k$ complete alternating rounds, the corresponding perfectly ordered leaf count is $n^k+m^k-1$, while exhaustive search has $(nm)^k$ leaves. Unequal branching by role must not be replaced by an arithmetic average branching factor inside an exact count.

## 11. Evaluation, cutoff and error propagation

For a nonterminal position at the depth horizon, an evaluation function $h(s)$ estimates its true continuation value. A common design is $h(s)=\sum_i w_i f_i(s)$, where features may measure material, mobility or threats. The function must use the same utility perspective at every level. A large feature score is not automatically a calibrated probability or a proven game-theoretic value.

Depth-limited minimax is exact for the finite surrogate tree whose frontier utilities are the stated evaluations. It need not be exact for the original game. Alpha-beta remains an exact acceleration of that surrogate calculation; it does not repair a mistaken frontier model.

There is a useful conditional error theorem. Suppose every frontier estimate differs from that position's correct continuation value by at most $\varepsilon$. For any two same-length vectors $x,y$,

$$|\max_i x_i-\max_i y_i|\le\max_i|x_i-y_i|,\qquad |\min_i x_i-\min_i y_i|\le\max_i|x_i-y_i|.$$

To prove the first inequality, let $x_j$ attain the maximum. Then $\max x-\max y\le x_j-y_j\le\max_i|x_i-y_i|$; exchange $x,y$ for the other direction. Negating values proves the MIN case. A weighted expectation with nonnegative weights summing to one is also nonexpansive by the triangle inequality. Induction through the backed-up tree therefore bounds root value error by $\varepsilon$, not $D\varepsilon$.

If each root action's backed-up estimate has error at most $\varepsilon$, choosing the greatest estimate loses at most $2\varepsilon$ in true action value. If $a^*$ is truly best and $\hat a$ is selected, then

$$Q(a^*)\le\widehat Q(a^*)+\varepsilon\le\widehat Q(\hat a)+\varepsilon\le Q(\hat a)+2\varepsilon.$$

Consequently a true best-action gap greater than $2\varepsilon$ cannot be reversed. The premise is strong: ordinary uncalibrated chess features do not come with a certified uniform error. The theorem is not an unconditional guarantee of good play, nor a guarantee about a sequence of later approximate decisions without further analysis.

Searching deeper often helps but need not improve every decision with arbitrary evaluations. A tactical loss just beyond the horizon can make an unstable position look attractive. Quiescence search selectively extends specified tactical continuations until a stable evaluation condition or a hard safety limit is reached. An extension without a termination rule can itself fail to finish.

## 12. Iterative deepening and transpositions

Iterative deepening completes searches at budgets1,2,3 and so on, keeping the action from the last completed iteration. At least one legal fallback action must exist before a deadline can interrupt the first iteration. A partially searched deeper iteration is not automatically better evidence than the last complete result. Move ordering can use the preceding principal variation, but the old depth-limited value is not assumed exact at the new depth.

If one counts leaf evaluations in complete unpruned trees, repeated depths0 through $D$ cost $\sum_{d=0}^D b^d$. Relative to the final $b^D$ leaves, this tends to $b/(b-1)$ for $b>1$. This simple ratio is not a universal overhead bound for variable branching, alpha-beta with changing order, node-generation costs or costly evaluation. With $b=1$, repeated traversal incurs quadratic total nodes over the depth sequence rather than a constant-factor geometric bound.

A transposition table can reuse results from identical sufficiently described states. A practical entry includes a position key, a searched horizon and a flag: exact, lower bound or upper bound. A lower-bound entry tightens alpha; an upper-bound entry tightens beta; an exact usable entry can be returned. Classify a fail-soft score against the **original** call window, not the mutated final alpha/beta. Otherwise a routine can label a bound exact merely because it changed its own threshold.

Depth qualification is semantic. A result from a different depth is not generally identical to the current depth-limited surrogate value. Practical engines may deliberately accept a deeper result under a declared search policy, while an exam asking for a precise fixed-horizon recurrence requires that recurrence's value. Hash collisions, omitted rule history and incompatible evaluation versions also invalidate reuse unless handled.

## 13. Known random opponents and expectiminimax

When an opponent follows a known distribution $\pi(a\mid s)$, the correct backup for optimizing expected utility against that model is an expectation rather than a minimum:

$$V(s)=\sum_{a\in A(s)}\pi(a\mid s)V(T(s,a)).$$

MAX nodes still take maxima. A natural random event, such as a die roll, is handled by the same weighted-sum operation. A game containing both an adversary and randomness uses MAX, MIN and CHANCE nodes in the actual order of events; it is called expectiminimax. Several opponents aligned against MAX may create consecutive MIN levels, and an extra turn may create consecutive MAX levels. Do not force alternation when the rules do not alternate.

A model saying the opponent takes a specified action with probability0.8 and otherwise samples uniformly from $m$ legal actions means that action has total probability $0.8+0.2/m$ and each other action has $0.2/m$. If random sampling explicitly excludes the preferred action, the probabilities differ. A solution must state which process the words describe.

The order of information and choice matters. If MAX chooses an action before observing a random outcome, the value is $\max_a\sum_z p(z)Q(a,z)$. If MAX first observes the outcome and can condition its action on it, the value is $\sum_zp(z)\max_aQ(a,z)$. The second is at least the first because a contingent action can always imitate a fixed action. Equality is possible, for example when one action is optimal in every outcome. Interchanging max and expectation without a justification gives MAX information it may not possess.

## 14. When chance-node pruning is legitimate

A single low child does not upper-bound an expectation when unexamined children can have arbitrarily high utilities. Conversely, a single high child does not lower-bound the final expectation if the remainder can be arbitrarily negative. Ordinary MIN/MAX cutoff reasoning therefore cannot simply be copied into a chance node.

Finite known utility bounds make a useful interval possible. Suppose processed outcomes contribute an exact weighted partial sum $S$, their total probability is $q$, and every unprocessed continuation value lies in $[L,U]$. Then

$$S+(1-q)L\le V(s)\le S+(1-q)U.$$

The proof adds each unknown contribution between $p_iL$ and $p_iU$. Nonnegativity of the probabilities is essential. If the upper endpoint is no greater than a MAX ancestor's established incumbent, the remaining outcomes cannot improve that decision. A corresponding lower endpoint can justify rejection by MIN. The certificate is an interval, not an exact expected value.

More generally, if evaluated outcomes themselves return intervals $[\ell_i,u_i]$, sum their probability-weighted endpoints rather than pretending the returned numbers are exact. Probability mass from repeated successor states must also be combined correctly. Rounding at intermediate steps can create a false cutoff; use exact rational arithmetic where feasible or conservatively outward-rounded intervals.

## 15. Utility transformations and risk

For deterministic minimax, a strictly increasing function $g$ commutes with finite min and max. Hence transforming all terminal utilities to $g(u)$ transforms the exact root value to $g(V)$ and preserves every action comparison and tie. The proof selects the same ordered extremum at each backup and proceeds by induction. A merely nondecreasing function can collapse unequal utilities into ties; a decreasing function reverses order.

Expectation depends on cardinal differences. A deterministic payoff2 beats a fair lottery between0 and3 because $2>1.5$. Cubing all outcomes reverses that preference: the deterministic utility becomes8, whereas the lottery's expected transformed utility is13.5. This is not a failure of expectation; the utility function, and therefore the decision objective, has changed.

A positive affine change $g(u)=au+c$, with $a>0$, preserves expected-utility decisions because normalized probabilities give $E[g(u)]=aE[u]+c$, and the same transformation commutes with min and max. It is important to transform actual terminal utilities before expectation, rather than apply a nonlinear function only to an already computed mean.

Expected monetary value and expected utility need not agree for a risk-sensitive decision maker. Concave utility represents diminishing marginal utility in a stated model. An evaluation score used for deterministic move ordering is not automatically suitable as a cardinal reward in a chance tree. A probabilistic search requires a coherent numerical objective and a justified probability model.

## 16. Multiplayer and hidden-information boundaries

In a general sequential game, a terminal payoff can be a vector $(u_1,\ldots,u_k)$. At a node controlled by player$i$, a max-n backup selects a child maximizing component$i$ and propagates the **entire selected vector**. Componentwise maxima assembled from different children may describe no realizable outcome. A deterministic tie rule or a stated equilibrium-selection convention is required when a player is indifferent between vectors that other players value differently.

Several MIN layers model a coalition sharing one objective against MAX. They do not generally model independent agents with distinct payoffs. Likewise, a simultaneous move cannot be modelled by revealing the first action to the second player unless that observation really exists. In matching pennies, pure sequential best response and simultaneous mixed-strategy analysis are different games.

With hidden information, actions must be consistent across histories a player cannot distinguish. Consider a hidden fair bit. After receiving no observation, a player chooses a guess and wins if it matches. Solving each hidden world separately permits a different correct guess in each and falsely yields a guaranteed win. A legal fixed or randomized guess wins with probability one-half. Averaging separately optimized perfect-information values has introduced an illegal information-dependent strategy; this is strategy fusion. The correct model uses information sets, beliefs or an appropriate imperfect-information game method.

## 17. Monte Carlo tree search without perspective errors

Basic Monte Carlo tree search repeatedly selects a path in the stored tree, expands a permitted new child, simulates a continuation using a declared rollout policy, and updates statistics along the visited path. A rollout payoff is a sample under the simulated policies, not an exact minimax certificate. Repeating an inaccurate rollout policy more times reduces sampling noise about that policy; it does not by itself remove model bias.

For an edge to child$i$, let $N_i$ be its visit count and $W_i$ its accumulated bounded reward from the perspective of the player selecting that edge. With parent visits $N>1$, one common selection score is

$$\operatorname{UCB}_i=\frac{W_i}{N_i}+C\sqrt{\frac{\ln N}{N_i}},\qquad C>0.$$

The mean term rewards promising outcomes and the bonus encourages uncertain alternatives. An unvisited legal child must be handled explicitly, commonly by exploring it before applying the displayed formula; division by zero is not a number to silently ignore. A natural logarithm is assumed. Different reward scales require a compatible exploration coefficient.

If every stored $W_i$ instead uses MAX's fixed utility coordinates, MIN cannot simply maximize the same UCB expression. Either transform the exploitation term to the selecting player's objective or consistently store player-relative edge rewards. In a win/loss0–1 encoding, complementing the reward is appropriate for the opposing player; negating0–1 rewards is a different scale. Extra turns mean that blindly flipping perspective at every edge is also wrong.

Backpropagation increments visits exactly once per visited node or edge under the declared convention and adds the corresponding payoff. Draw treatment, such as one-half reward, must be specified. A commonly used final root rule selects the most-visited action; this differs from maximizing the exploratory UCB score at decision time. Finite samples provide no guarantee that this action is truly best.

For $n$ independent Bernoulli rollouts under a fixed policy with true win probability$p$, the sample mean is unbiased and has variance $p(1-p)/n$. That statement is about the fixed-policy experiment; adaptive tree selection and changing policies require more careful assumptions. Introductory UCT asymptotic statements are not finite-budget certificates of perfect game play.

## 18. How to solve a game-search examination question

First determine the model: controlling player at each node, utility perspective, action order, deterministic or probabilistic transitions, available observations and the terminal or cutoff boundary. Write down whether depth means individual plies or complete rounds. Identify the requested result: value, action, policy, exact leaf count, pruned branches or a proof.

For minimax, back up the relevant tree and identify attaining children. For alpha-beta, declare equality and fail-soft/fail-hard conventions, track the incoming window at each call, and label cutoff returns by their justified direction. Count only leaves actually evaluated when that is the requested metric. Do not infer the exact value of a pruned subtree from a returned endpoint.

For chance nodes, verify probabilities sum to one and use a weighted sum. If pruning is requested, identify the actual finite bounds on the unobserved contribution. For utility transformations, distinguish order preservation from expectation preservation. For depth-limited play, distinguish exactness on the surrogate from quality relative to the full game.

Finally, verify the answer using an independent route: a full small-tree backup, an enforcement/restriction certificate, an exact probability calculation, a boundary parameter value or an explicit counterexample. A numerical answer without its modelling assumptions can be correct for a different game and still fail the question being asked.
