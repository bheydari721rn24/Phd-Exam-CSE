# Intelligent Agents, Rationality, Task Environments, and Problem Formulation

## 1. Sources, scope and how to study

This is the first Artificial Intelligence chapter. It builds the mathematical language needed before search algorithms: what an agent knows, what it can do, how its performance is judged, and what information belongs in a state. Read the lesson before attempting the bank. Solutions are teaching explanations, not an instruction to take a diagnostic test now.

Four written courses were reviewed: Berkeley CS188, Fall 2023, taught by Igor Mordatch and Peyrin Kao, Note 1 by Nikhil Sharma; CMU 15-281, Fall 2023, Vincent Conitzer and Aditi Raghunathan, Introduction and activity solutions; Edinburgh INF2D, written Lectures 1 and 2 in its 2025 material; Stanford CS221, Summer 2012–2013, Chris Piech's Markov Decisions handout. Exact documents, the compared pool, disagreements and reading limits appear in the [source audit](../reviews/i_agents-sources.html). The final reference section links each document.

The teaching and problem constructions below are original. They use the reviewed definitions as a starting point, then derive precise conditions and counterexamples. Search-order proofs, Bayesian networks, full MDP algorithms, reinforcement-learning convergence, game equilibria and learning theory have their own later chapters. Here they appear only where necessary to make agent foundations mathematically meaningful. A finite scope and checked derivations support reliable study; they cannot certify performance on every possible unseen question.

## 2. The agent–environment boundary

An agent receives observations and chooses actions. Its environment is the part of the model outside that decision mechanism. A physical robot can have cameras and motors; a software agent can receive a message and send a database request. “Sensor” and “actuator” name these information and influence channels, not necessarily physical devices. A stored image is an observation. A command to move is an action. The resulting displacement is an environmental outcome, which can differ from the command.

Use a discrete decision index $t$. Write $s_t$ for the environment state, $o_t$ for the observation, and $a_t$ for the selected action. In a deterministic model, an observation map $O$ and transition map $T$ give

$$o_t=O(s_t),\qquad a_t=f(o_0,\ldots,o_t),\qquad s_{t+1}=T(s_t,a_t).$$

The order matters: the action selected from the current observation affects the next state, not the already received observation. In a stochastic model, $T(s,a,s')$ denotes a conditional probability rather than a successor state. Never use the same symbol as both a state and a probability without specifying the convention.

The boundary is a modelling choice. A robot team controlled by one central planner can be one decision maker with a joint action. An opponent with separate objectives must still be represented in that team's environment. Counting bodies is not the same as identifying independent decision makers. Include external processes only to the detail needed for prediction and evaluation.

<!-- SIM: loop -->

## 3. Agent function, program and architecture

An **agent function** specifies behaviour for every possible finite observation history. If $P$ is the percept alphabet and $A$ the action set, one conventional signature is $f:P^*\to A$. If no action is selected before the first percept, restrict the domain to nonempty histories. A **program** is a finite implementation of such behaviour on an **architecture**, which supplies memory, computation and sensor/actuator interfaces. Different programs can implement the same function; a particular function need not be implementable within a specified memory or time budget.

A table of actions for histories is a behavioural description, not a scalable design. Suppose there are $p$ percepts and $a$ actions and the agent makes decisions after histories of lengths $1$ through $H$. The number of table entries is

$$N_H=\sum_{t=1}^{H}p^t.$$

For $p\ne1$, multiply the sum by $p$ and subtract the original to obtain $N_H=(p^{H+1}-p)/(p-1)$. For $p=1$, it is $H$. Each entry independently selects one of $a$ actions, so the number of unrestricted tables is $a^{N_H}$. With $p=2,a=3,H=3$, there are $2+4+8=14$ entries and $3^{14}$ functions. A memoryless percept rule needs only $p$ entries and has $a^p$ possibilities.

This counts all syntactic histories, including some unreachable in a fixed environment. Behavioural equivalence on reachable histories can identify different tables. A deterministic agent's own previous actions can be reconstructed from its known function and percept history. For a randomized agent, actions or its random-state information may need to be included explicitly; use the richer history $h_t=(o_0,a_0,o_1,\ldots,a_{t-1},o_t)$ when that distinction matters.

## 4. Performance measures, rewards and PEAS

PEAS describes **Performance measure, Environment, Actuators, Sensors**. It is a specification of the task, not a four-step search algorithm. A performance measure evaluates what happened. A reward is a numerical feedback signal used inside a model or learning procedure. They may agree, but equality must be designed rather than assumed.

For a delivery robot, a complete specification might evaluate completed deliveries, lateness, energy consumption and collisions over a stated horizon; include corridors, doors and other traffic in the environment; provide drive, stop and load commands as actuators; and provide localisation, obstacle range, battery and package sensors. “Be efficient” is not a usable performance measure until its tradeoffs and units are defined.

One possible score is $J=10D-2L-E-100C$, where $D$ is deliveries, $L$ is late minutes, $E$ is energy units and $C$ is collisions. Compare two runs explicitly. Run A has $(D,L,E,C)=(3,2,4,0)$, giving $22$. Run B has $(4,0,3,1)$, giving $-63$. Under this score, more deliveries do not justify a collision. If collisions are forbidden rather than merely expensive, remove unsafe policies from the feasible set; a finite penalty is not automatically a hard constraint.

A badly chosen proxy can reward the wrong behaviour. Paying for each “clean” message lets an agent repeatedly announce cleanliness without cleaning. Paying for dirt removed can encourage re-dirtying if that is allowed and unpenalized. Define the desired outcome independently of the agent's self-report, include all allowed actions, and test what maximizes the proposed score.

## 5. Rationality is conditional, not omniscience

An action is rational when it maximizes expected performance given the agent's information, model, available actions and evaluation criterion. The expectation concerns possible outcomes, not only the outcome later observed. A rational decision can have an unfortunate realization. An omniscient decision maker knows the actual future consequence; ordinary rationality grants no such knowledge.

For a finite one-step model, let $b(s\mid h)$ be the current belief and let $U(s,a)$ include all action-dependent consequences and costs. Then

$$EU(a\mid h)=\sum_s b(s\mid h)U(s,a),\qquad a^*(h)\in\operatorname{argmax}_{a\in A(h)}EU(a\mid h).$$

The maximizing set can contain several actions. A deterministic tie rule chooses one; randomized mixing among tied maximizers remains optimal. An empty legal action set requires an explicit termination or failure convention, not an undefined maximum.

For example, a safe action pays $4$ for certain. A risky action pays $10$ with probability $3/5$ and $-2$ otherwise. Its expected payoff is $6-4/5=26/5>4$. Choosing it maximizes expected payoff, although a realized payoff of $-2$ is possible. If the stated utility is not money, calculate the expected utility of outcomes rather than applying utility to the expected money. Model error and mistaken preferences can make an internally consistent maximizer perform poorly under the true task measure; always state which model is being used.

<!-- SIM: utility -->

## 6. Deriving decision thresholds

Many agent questions reduce to comparing two affine functions of a probability. Suppose hidden state $H$ has probability $p$, and $L$ has probability $1-p$. Actions A and B have utilities $(u_{AH},u_{AL})$ and $(u_{BH},u_{BL})$. Subtract their expected utilities:

$$EU(A)-EU(B)=p(u_{AH}-u_{BH})+(1-p)(u_{AL}-u_{BL}).$$

If the coefficient of $p$ is positive, solve the resulting inequality with its direction unchanged; if negative, reverse it; if zero, the decision is constant or tied. Intersect the answer with $0\le p\le1$. A threshold outside this interval means one action is preferred throughout the feasible range.

Take A with utilities $(12,-4)$ and B with $(5,5)$. Then $EU(A)=16p-4$, and A is optimal exactly when $p\ge9/16$, with a tie at equality. The statement “choose A if H is more likely” is false: $p=0.53$ exceeds one half but is below $9/16$. A prior change, sensor result or loss asymmetry can cross the actual threshold.

An action is statewise dominated if another action has at least as much utility in every state and strictly more in at least one. Weak dominance guarantees no lower expectation; strict expected improvement additionally requires positive probability on a state with strict improvement. Do not delete a tied action by silently assuming every state has positive probability.

## 7. Utility scales, risk and robust decisions

For a common outcome distribution, the transformation $U'=\alpha U+\beta$ with $\alpha>0$ preserves expected-utility rankings because $E[U']=\alpha E[U]+\beta$. A negative scale reverses rankings; a zero scale makes all outcomes equal. An arbitrary increasing transformation preserves rankings of individual certain outcomes, but need not preserve rankings of lotteries.

Let lottery A pay $0$ or $100$, each with probability one half; B pays $40$ certainly. Expected money favours A, $50>40$. With utility $u(x)=\sqrt{x}$ for nonnegative money, expected utility favours B because $5<\sqrt{40}$. Risk preference is encoded by utility; choosing a smaller expected monetary amount is not automatically irrational.

When no probability model is supplied, expected utility cannot be numerically determined from the payoff table alone. A worst-case rule chooses the action maximizing its minimum payoff. A minimax-regret rule first subtracts each action's payoff from the best available payoff separately in each state, then minimizes the largest regret. These are different criteria, not interchangeable definitions of rationality. With A=$(8,-2)$ and B=$(3,3)$, maximin chooses B; under prior $p=4/5$, expected utility chooses A because $6>3$.

## 8. Observability and the information actually available

Full observability means the current percept determines all decision-relevant state information in the declared model. It does not mean the agent knows future random outcomes, transition parameters or other agents' future choices. Partial observability means distinct relevant states can produce the same percept. A noisy camera is one cause; an exact local sensor in a larger world is another.

With deterministic observations, define the observation class $[s]_O=\{s':O(s')=O(s)\}$. An observation is sufficient to identify state if these classes are singletons over the relevant reachable states. It can still be sufficient to choose an optimal action when a class has several states but all share a maximizer. This is why partial observability alone does not prove that memory is beneficial.

Consider two hidden conditions requiring the same safe action. Their sensor readings can be identical without reducing decision quality. Conversely, if the same reading occurs after two histories whose unique optimal actions differ, every deterministic memoryless rule fails on at least one of those histories. The failure is informational: a rule cannot output two different actions for the same input.

<!-- SIM: aliasing -->

## 9. Deterministic, stochastic and strategic environments

A deterministic transition gives one successor for each fully specified state and action. A stochastic transition supplies a distribution. Unknown dynamics concern the agent's knowledge of the transition, not whether the transition is deterministic. A fair die is stochastic even if its distribution is known. A fixed but initially unknown door code can be deterministic and unknown.

Hidden deterministic state can make observations appear random. If the true state includes a hidden bit $z$ and the next observation is $z$, uncertainty about $z$ induces a distribution over observations despite deterministic physical evolution. Augmenting the state can reveal determinism; adding irrelevant variables does not necessarily help the agent observe them.

In a strategic environment, other decision makers choose actions according to their objectives. Their behaviour may be predictable or randomized, but replacing them with a fixed random generator is an additional modelling assumption. A game may have a deterministic next board given the **joint** action while a single player's future remains uncertain. Determinism and number of agents are separate axes.

## 10. Episodic, sequential and time-dependent tasks

An episodic task separates decisions into episodes whose consequences do not affect later opportunities or performance. A one-letter classification task can be episodic when labels are independent and each decision has its own loss. A mail robot with a shared battery or a daily quota is sequential: today's action changes tomorrow's resources. Independent observations alone do not establish episodicity.

A static environment does not evolve during the agent's deliberation in the chosen decision model. It can change when the agent executes an action. A sliding puzzle is a simple example. In a dynamic environment, traffic or other processes move while the agent thinks. In a semidynamic task, the physical state can remain fixed while performance changes with elapsed time, as in a timed puzzle. If time changes action feasibility, augment the state with time and describe the resulting model explicitly.

Discrete and continuous refer separately to states, observations, actions and time. Integer room numbers do not make continuous steering commands discrete. A countably infinite counter is discrete but not finite. A sampled model of a continuous system is an abstraction; it does not make the underlying physics discrete.

## 11. Classify a task by justified assumptions

For an untimed, fully displayed deterministic board puzzle with one player, a known move rule and no external changes, the usual classification is fully observable, deterministic, sequential, static, discrete, known and single-agent. Change one assumption at a time. Hide a tile and observability changes; add a clock penalty and it becomes semidynamic; let a tile slip randomly and the transition becomes stochastic; withhold the slip probability and model knowledge becomes incomplete as well.

Do not classify “chess”, “driving” or “a robot” by a memorized word alone. Standard chess has no hidden pieces, but board arrangement without castling rights, side to move, en-passant rights and relevant draw history is not a complete rule state. Timed chess adds an elapsed-time issue. Driving models depend on sensor limitations, other road users, actuation uncertainty and the time resolution chosen.

For each axis, write a witness: two indistinguishable states for partial observability; two positive-probability successors for stochasticity; a resource changed by an action for sequentiality; an exogenous change during thought for dynamic behaviour. A witness is more reliable than a label unsupported by the task statement.

## 12. Simple reflex and model-based reflex agents

A simple reflex policy maps the current percept to an action. A condition–action implementation can test several fields in that percept; it is not restricted to one Boolean condition. Such a policy may be optimal for a suitable task, including a sequential one if the percept already supplies sufficient state and the optimal action is compiled into a rule.

A model-based reflex agent maintains an internal summary $m_t$ and updates it using the previous action and new percept:

$$m_t=F(m_{t-1},a_{t-1},o_t),\qquad a_t=\pi(m_t).$$

The summary may be a room map, a finite controller state, a set of possible states or a probability distribution. “Model-based” concerns representing how observations and actions relate to the world. “Reflex” concerns applying a current condition–action rule rather than explicitly searching over future consequences at decision time. An agent can have memory without performing online planning.

Using a stale summary is a common implementation error. First predict the effect of the previous action, then incorporate the current observation, then choose a new action. If cleaning may fail, recording “clean” after issuing the command is unjustified unless the new percept verifies it or the model assigns certainty to success.

For the reliable, no-recurrence two-room model, the following controller shows the difference between a current percept and persistent memory. Each cleanliness entry initially means **unknown**, rather than falsely assuming that an unobserved room is clean. An observation of dirty replaces any earlier clean report. The update is justified only by the reliable sensor and no-recurrence model.

```python
# Persistent fields survive between calls.
verified_clean = {"L": False, "R": False}

def choose_action(position, dirty):
    verified_clean[position] = not dirty
    if dirty:
        return "Clean"  # Verify the result on the next call.
    if all(verified_clean.values()):
        return "Stop"
    return "Right" if position == "L" else "Left"
```

This controller does not claim that an issued Clean command has already succeeded. It waits for the next observation. Starting with both rooms dirty, successive percepts lead to Clean, Right, Clean, Stop. With dirt recurrence, the persistent bit for a room not currently observed can become stale, so the code is not a guaranteed maintenance policy for that different model.

## 13. Goal-based and utility-based choice

A goal is a condition on states or histories. Goal-based reasoning seeks a way to satisfy it. Several conditions can form a conjunction: deliver both parcels and return to the charger. Utility grades outcomes and can prefer one goal-reaching run over another because it is faster, safer or less costly. Goals alone do not determine those preferences unless costs or an ordering are separately specified.

These architecture labels are not a strict hierarchy of intelligence. A compiled policy can execute the exact action previously found by a planner. A utility maximizer can use a learned model. A model-based reflex controller can outperform a slow planner under a short deadline. The question is which representation, computation and objective fit the task.

Achievement means reaching a target at some time. Maintenance means avoiding a forbidden condition throughout the relevant run. “Eventually arrive” and “never collide” are not the same goal. A run that collides first and arrives later satisfies the former but violates the latter. A terminal goal test alone cannot detect a past collision unless that information is retained in the state or evaluated over the trajectory.

## 14. Learning, exploration and bounded computation

A learning agent changes its behaviour or model using experience. A performance element chooses actions; a critic supplies task-related feedback; a learning element updates the performance element; an exploration mechanism can select informative experiences. This functional decomposition does not require four physical processors or four independent programs.

Learning can improve the sensor model, transition model, utility estimate, rules, action-value estimates or a direct policy. The useful method depends on the target, prior knowledge, available data and feedback. Data quantity alone cannot determine it. A deterministic environment can require learning an unknown map. A stochastic environment with a fully known model need not require model learning.

Exploration can be rational because it improves later decisions, but it is not obligatory in every unknown environment. Suppose testing an unknown door yields information worth at most $2$ in all remaining decisions and costs $5$ now. The test is not justified by information value. With no remaining decisions and no immediate benefit, learning for its own sake is not required by the specified performance measure.

Bounded optimality compares implementable programs on a specified architecture, accounting for time and resources. If a fast decision has expected utility $8$ and computation raises decision quality to $10$ but costs $3$, the fast choice has larger net utility. “More reasoning” needs a value calculation; it is not a universal improvement.

## 15. Sufficient state and the Markov property

A state is sufficient for prediction if, conditioned on it and the selected action, earlier history adds no relevant information about the next state and reward. In a finite controlled model, write

$$P(s_{t+1},r_t\mid h_t,a_t)=P(s_{t+1},r_t\mid s_t,a_t).$$

This is a property of the representation and model, not a guarantee supplied by calling a variable “state”. Position alone is insufficient if a locked door depends on whether a key was collected. Add a key bit. Position alone is insufficient if future cost depends on remaining fuel. Add fuel. Finite-horizon optimal policies can depend on the remaining time even when physical transitions are stationary; either retain a time-indexed policy or include time in state.

Full history is often a formally sufficient representation, but grows without bound. Seek a compact sufficient summary. A summary sufficient for one objective need not be sufficient for another. For reaching a fixed room, collected food may be irrelevant; for collecting every item, remaining-item bits are essential. State variables are selected relative to transition, legality, goals and costs together.

## 16. The exact criterion for a rational memoryless policy

Fix a finite action set and a set of relevant histories. For each history $h$, let $M(h)$ be the set of actions optimal under the specified continuation criterion. A deterministic policy using only current percept $o$ can be optimal at every relevant history **if and only if**

$$\bigcap_{h:\,\operatorname{last}(h)=o} M(h)\ne\varnothing\quad\text{for every occurring percept }o.$$

**Necessity.** A memoryless rule selects one action $\pi(o)$. If it is optimal at every history with percept $o$, that same action belongs to every corresponding $M(h)$, hence to their intersection.

**Sufficiency.** Choose one action from each nonempty intersection and define $\pi(o)$ to be that action. By construction it is optimal at every history sharing that percept. The argument assumes the relevant optimal-action sets have already been defined consistently; it does not compute them from nothing.

For two histories with $M(h_1)=\{A,B\}$ and $M(h_2)=\{B,C\}$, B works even though state is uncertain. With $M(h_1)=\{A\}$ and $M(h_2)=\{B\}$, no current-percept-only rule works. Distinguishing those histories requires at least two internal conditions. Randomization does not restore optimality at both when each has a different unique maximizer: any mixture assigning positive mass to the wrong action loses utility at one history.

## 17. Beliefs: sets and probability distributions

When the world is partially observed, an agent can maintain a **belief set** of states compatible with the history. Under deterministic dynamics, first propagate every possible current state through the chosen action, then discard successors incompatible with the new observation. If $B_t$ is the current set,

$$B_{t+1}=\{T(s,a_t):s\in B_t,\ O(T(s,a_t))=o_{t+1}\}.$$

For nondeterministic dynamics, replace each singleton successor with its permitted successor set. An empty belief indicates inconsistent observations or a model error, unless the history was assigned probability zero by design. It is not a proof that the physical world has no state.

A probability belief also weights compatible states. For transition probabilities $T$ and observation likelihood $Z(o\mid s',a)$, predict and condition:

$$\widehat b(s')=\sum_s T(s,a,s')b(s),\qquad b'(s')=\frac{Z(o\mid s',a)\widehat b(s')}{\sum_x Z(o\mid x,a)\widehat b(x)}.$$

The denominator must be positive. At zero, do not divide by zero or return a fabricated uniform posterior; report that the observation is impossible under the current model. Set propagation and probability filtering answer different questions. Two beliefs with identical support can select different optimal actions because their weights differ.

## 18. A complete binary-sensor calculation

Let hidden state H have prior $3/10$. A positive sensor result occurs with probability $4/5$ in H and $1/5$ in L. Then

$$P(+)=\frac{3}{10}\frac45+\frac7{10}\frac15=\frac{19}{50},\qquad P(H\mid+)=\frac{12}{19}.$$

A negative result has probability $31/50$ and posterior $P(H\mid-)=3/31$. Both branches must be considered before purchasing the sensor. The posterior is not the sensor's accuracy: $12/19$ differs from $4/5$ because the prior matters.

Use the earlier actions A=$(12,-4)$ and B=$(5,5)$. Before sensing, A has utility $4/5$ and B has $5$, so B wins. After a positive result, A has $116/19>5$. After a negative result, A has $-76/31<5$, so B wins. Expected optimized utility after the free signal is

$$\frac{19}{50}\frac{116}{19}+\frac{31}{50}\,5=\frac{271}{50}.$$

The expected value of sample information is $271/50-5=21/50$. A sensor cost of $1/4$ leaves net gain $17/100$, so acquiring it is rational in this one-step model; cost $1/2$ makes the net gain negative. The editable laboratory recalculates every branch exactly, including ties and zero-probability observations.

<!-- SIM: belief -->

## 19. Why free information cannot hurt under stated conditions

Let $Y$ be a signal available before action, with no effect on the environment, no delay, no cost and no restriction forcing the agent to use it. For each signal value, let $EU(a\mid Y)$ be conditional utility. If $a_0$ is optimal before sensing, then for every possible signal,

$$\max_a EU(a\mid Y)\ge EU(a_0\mid Y).$$

Average over the signal and apply total expectation. The expected optimized value after information is at least $EU(a_0)$, the best prior value. This proves nonnegative information value under the stated conditions. It can be zero: if one action remains best after every signal, the information does not change the decision.

Perfect information reveals the hidden state. Its value is an upper bound on the value of a less informative signal in the same one-step model, because a perfectly informed decision maker can simulate the signal and follow its policy. For A=$(12,-4)$, B=$(5,5)$ and prior $3/10$, perfect information yields $(3/10)12+(7/10)5=71/10$, so its value is $21/10$, exceeding $21/50$ for the noisy sensor. Costs, delay, forced disclosure or an imperfect optimizer invalidate the simple “cannot hurt” conclusion if included in performance.

## 20. A fully specified two-room vacuum world

Represent a physical state by $(x,d_L,d_R)$, where $x\in\{L,R\}$ and each dirt bit is zero or one. There are $2\cdot2^2=8$ states. The local percept $(x,d_x)$ has only four values and does not reveal the other room's dirt. The dynamics below are deterministic and known: Left sets position to L, Right sets it to R, Clean sets the current dirt bit to zero, and Stop leaves the state unchanged. Dirt never reappears. No clock or external process changes the state while the agent deliberates.

The goal is both dirt bits zero. With unit action costs, a known state $(L,1,1)$ has a three-action solution Clean, Right, Clean. Fewer than three actions are impossible: two distinct dirty rooms require two cleans, and reaching the second room requires a move. With no sensors and an arbitrary initial physical state, Right, Clean, Left, Clean guarantees the goal in four actions. Right deliberately merges the two possible initial locations; cleaning then reduces uncertainty about dirt. Sensorless planning can succeed without discovering the exact initial state.

A local rule “clean if dirty; otherwise go to the other room” cleans both rooms but then moves forever. If movement is penalized after the goal, that infinite loop is wasteful. A model-based controller can remember verified cleanliness of both rooms and stop. If dirt can recur, the stop rule requires revision; the proof used the no-reappearance assumption.

<!-- SIM: vacuum -->

## 21. Formulating a deterministic search problem

A search problem specifies a state set $S$, initial state $s_0$, legal action set $A(s)$, result function $T(s,a)$, goal test $G(s)$ and step cost $c(s,a,s')$. A solution is a legal action sequence reaching a goal. An optimal solution minimizes the declared path cost, which for additive costs is

$$g=\sum_{t=0}^{k-1}c(s_t,a_t,s_{t+1}).$$

The goal test need not list all goal states explicitly. “No remaining dirt” is an implicit predicate on two bits. Distinguish a zero-length solution when the initial state is already a goal from failure when no solution exists. Failure is not an empty plan unless the API explicitly distinguishes those cases.

Path cost and depth agree only with equal positive action costs, up to a constant factor. A route with two edges of cost $100$ is more expensive than a route with three edges of cost $1$. Negative-cost cycles can destroy existence of a minimum-cost solution; zero-cost cycles can create infinitely many equal-cost paths. Algorithms and their guarantees must state the relevant cost assumptions. The next chapter treats uninformed search; this chapter establishes the model it operates on.

## 22. Safe abstraction and omitted variables

Let $\phi$ map detailed states to abstract states. A useful exact deterministic abstraction requires equivalent detailed states to agree on goal status and legal abstract actions. For every common action, their successors must remain equivalent and their corresponding costs must agree:

$$\phi(s)=\phi(t)\ \Longrightarrow\ \phi(T(s,a))=\phi(T(t,a)).$$

Together with matching legality, goals and costs, this makes the abstract transition well-defined. Induct on action-sequence length: the base states have the same abstraction; one legal action preserves equivalence by the displayed condition; repeat. The two concrete executions then produce matching abstract states, accumulated costs and goal results. This proves exact preservation for the specified action sequences. A looser relaxation used to obtain a lower bound need not satisfy these exact conditions; it has a different purpose.

If two states share a room position but differ in possession of a required key, “position only” merges a state where Open is legal with one where it is illegal. The abstract plan can become unrealizable. If fuel differs, a common move may be feasible in only one state. If the objective penalizes a previous collision, add a flag or keep a history-based evaluator. The correct abstraction removes irrelevant detail, not inconvenient constraints.

<!-- SIM: abstraction -->

## 23. Count states by independence and constraints

Apply the product rule only when choices are independently allowed. A robot in one of $n$ rooms with $n$ independent dirt bits has $n2^n$ syntactic physical states. If exactly $k$ rooms are dirty, it has $n\binom nk$ states. If the robot must be in a clean room, choose its location first and assign dirt only to the remaining rooms, obtaining $n2^{n-1}$.

For two labelled robots in distinct rooms, positions number $n(n-1)$, not $n^2$. If robots are indistinguishable and all dynamics and objectives are symmetric, unordered positions number $\binom n2$. Removing labels is invalid if the robots have different capacities or actions. A state-space product is an upper bound when some combinations are unreachable; distinguish legal configuration count from reachability from a particular start.

With $N$ physical states, there are $2^N$ belief subsets, including the empty set; there are $2^N-1$ nonempty subsets. The belief states reachable under a particular sensor and transition model can be far fewer. Probability distributions over just two physical states already form a continuum, even though the support-set space is finite.

## 24. State graphs, search nodes and contingent policies

A state graph has one vertex per model state and edges for legal transitions. A search-tree node records a particular path prefix: state, parent, generating action and accumulated cost. Different nodes can contain the same state. A cycle can make a search tree infinite while the state graph is finite. Recognizing equal states requires a sufficient state representation; merging two nodes by position alone is unsafe if one has a key and the other does not.

Under deterministic, known transitions and a known initial state, an action sequence can predict the entire run. Under observation-dependent uncertainty, a contingent policy can select different actions after different observations. A fixed sequence is a special case of a policy. There need not be a fixed sequence as good as the best contingent policy, but uncertainty does not logically require a contingent solution in every task; the sensorless vacuum sequence is a counterexample.

For a known current state with two available actions and three possible observations before a second action, a full two-step contingent policy selects the first action and one second action for each observation. If all combinations are allowed, there are $2\cdot2^3=16$ such policies. There are only $2^2=4$ fixed sequences. If observations are impossible on some branches, count reachable decisions separately.

<!-- SIM: graph -->

## 25. Sequential returns and evaluation

For a finite horizon $H$, a common return is $G=\sum_{t=0}^{H-1}\gamma^t r_t$, optionally followed by a terminal utility with its specified discount. With $\gamma=1$, rewards add without discounting. With $0<\gamma<1$, earlier rewards have greater weight. For bounded rewards $|r_t|\le R$ and an infinite horizon, the geometric series gives $|G|\le R/(1-\gamma)$. Without a bound or discount, existence of an expected return needs separate justification.

A greedy action maximizing immediate reward can be poor for a sequential objective. Action A pays $6$ now and $-10$ next; B pays $1$ now and $8$ next. With $\gamma=1$, their returns are $-4$ and $9$. With general $\gamma$, A is preferred only if $6-10\gamma\ge1+8\gamma$, or $\gamma\le5/18$. The ranking depends on the stated horizon and discount, not a slogan about greed.

Evaluation compares policies on the same model distribution and task criterion. One successful run does not prove rationality; one unlucky run does not disprove it. An independently derived answer is not an official examination key. A simulator that verifies its finite transitions does not prove a claim about every environment. These distinctions keep empirical checks and mathematical guarantees separate.

## 26. Summary and examination workflow

Start by identifying the objective, information, actions and model. Separate a percept from a physical state and separate a physical state from an internal summary. When classifying an environment, give the assumption or witness for each axis. When deciding an action, write its utility in every relevant state, weight by the correct belief, include costs, and compare the resulting values. Solve ties and boundaries explicitly.

When formulating a problem, ensure that states retain everything needed for action legality, transition, goal and cost. Count independent choices and then remove forbidden combinations. Distinguish full configuration space from reachable states, physical states from belief states, and state vertices from search nodes. For information acquisition, optimize separately after each possible signal before averaging; optimizing after averaging answers a different question.

When an assertion says “always”, try a minimal counterexample: a partially observed task with one common best action; a deterministic unknown map; a static puzzle changed by the agent's own moves; a free signal that never changes the best action; a costly computation whose quality gain is too small; or a sequential task whose sufficient percept makes a compiled reflex policy optimal. The detailed rules below attach the necessary conditions to each conclusion.

## 27. Worked mathematical and conceptual problems

The original bank develops counting, information, rationality, architecture and exact modelling from medium calculations to hard synthesis. Course reconstructions have their own provenance labels and independently written data or qualifications. The authentic items are checked English adaptations of the original PDF page, with the original option order retained. Two directly relevant MSc items are included; the inspected recent PhD CE pages did not supply a matching foundations item, and no unrelated question is relabelled as agent foundations. All answers are independently derived.

<!-- INCLUDE: problems -->

## 28. Final rules, traps and boundary conditions

Each rule is a complete retrieval statement, including its assumptions and a calculation or counterexample. These consolidate the lesson; they do not replace the proofs or the worked solutions.

<!-- INCLUDE: review -->

## 29. Editable information-and-action laboratory

Enter a prior, two positive-signal likelihoods, a two-action utility table and an information cost. The laboratory computes both observations, each posterior, each optimal action, expected utility before and after sensing, perfect-information value and net information gain with exact rational arithmetic. Zero-probability observations are explicitly skipped rather than normalized. Probabilities must lie between zero and one; costs must be nonnegative. The animation shows belief mass, decision alternatives and signal branches for your actual input.

<!-- LAB: agents -->

## 30. References and boundaries

- UC Berkeley, CS188, Igor Mordatch and Peyrin Kao; Nikhil Sharma, [Fall 2023 Note 1](https://inst.eecs.berkeley.edu/~cs188/fa23/assets/notes/cs188-fa23-note01.pdf), PDF pages 1–2. Introductory terminology; the source audit qualifies static environments and reflex optimality.
- Carnegie Mellon, 15-281, Vincent Conitzer and Aditi Raghunathan, [Introduction lecture](https://www.cs.cmu.edu/~15281-f23/lectures/15281_Fa23_Lecture_1_Introduction.pdf), especially PDF pages 9–18, 27–30 and 39–51; [Lecture 1 activity solutions](https://www.cs.cmu.edu/~15281-f23/activities/15281_F23_Lecture_1_Activity_Solutions.pdf), pages 1–2. Compiled agents and constrained state counting.
- University of Edinburgh, INF2D, [Intelligent Agents and their Environments](https://opencourse.inf.ed.ac.uk/sites/default/files/https/opencourse.inf.ed.ac.uk/inf2d/2025/inf2dlectureslides-01intelligentagents_0.pdf), pages 5–37; [Problem Solving and Search](https://opencourse.inf.ed.ac.uk/sites/default/files/https/opencourse.inf.ed.ac.uk/inf2d/2025/inf2dlectureslides-02search_0.pdf), pages 3–22 and 28–29. The PDF does not identify a single lecturer; the current course team and provenance qualification appear in the audit.
- Stanford, CS221, Chris Piech, Summer 2012–2013, [Markov Decisions](https://stanford.edu/~cpiech/cs221/handouts/markovDecisions.html), all named sections. Finite stochastic-state modelling and conditional utility; advanced solving methods are deferred.
- Michael Wooldridge, [Intelligent Agents, second-edition Lecture 2](https://www.cs.ox.ac.uk/people/michael.wooldridge/pubs/imas/distrib/pdf-slides/lect02.pdf), especially pages 36–71. Supplementary formal comparison, hosted by Oxford; not attributed to a verified Oxford taught term.
- Iranian MSc Computer Engineering 1405, booklet 135A, original PDF page 15, questions 71 and 75. The worked bank links the exact repository commit and records its SHA-256. Independent solutions are not official keys.

The finite chapter covers agent foundations, constrained state modelling and introductory information-sensitive decisions. Full search algorithms, game solutions, Bayesian-network inference, MDP solution methods and learning theory require their scheduled chapters. Source selection and answer checking are documented; absolute completeness over all courses or all future examinations is not asserted.
