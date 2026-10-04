### The chapter in one coherent map

Start with the hidden-state partition and the actual observation protocol. Multiply each prior by that state's likelihood of the complete evidence. Add the resulting joint masses to obtain the evidence probability, then divide all masses by the same positive denominator. Posterior odds are prior odds multiplied by a likelihood ratio; a sequential ratio must condition on the preceding history unless conditional independence has been established. Predictions average the next observation's likelihood under posterior state weights. Decisions additionally require an explicit loss function. Continuous parameter inference replaces discrete normalization by an integral and returns a density, whose probabilities must be integrated.

The core formulas are $w_i=\pi_iL_i$, $Z=\sum_iw_i$, $r_i=w_i/Z$ for $Z>0$, and $O_{\mathrm{post}}=O_{\mathrm{prior}}L_H/L_{H^c}$ when the odds factors are defined. For a detector, positive credibility is $ps/[ps+(1-p)f]$, negative target probability is $p(1-s)/[p(1-s)+(1-p)(1-f)]$, and overall accuracy is $ps+(1-p)(1-f)$. Under zero correct-decision loss, the target action is preferable when its posterior reaches $c_{FP}/(c_{FP}+c_{FN})$.

### Modeling, partitions, and normalization

1. Name the target hypothesis and observed event before manipulating numbers. The probability of an observation inside a hypothesis and the probability of that hypothesis after the observation have opposite conditioning directions.

2. Hypotheses used in the total-probability denominator must be mutually exclusive and exhaustive. If proposed causes overlap, split them into disjoint membership cells before assigning their likelihoods.

3. Prior probabilities are weights over hypotheses and sum to one. Likelihoods at one fixed observation are not weights over hypotheses and generally do not sum to one.

4. The event probability is a prior-weighted sum of likelihoods. Taking their simple average is valid only when the model supplies equal priors for the entire hypothesis partition.

5. Bayes' numerator is the joint mass of the hypothesis and evidence. Keeping a separate row for prior, likelihood, joint mass, and posterior prevents substitutions between these quantities.

6. Every posterior component uses the same evidence denominator. A different denominator for each hypothesis cannot produce a coherent posterior over one common observation.

7. The posterior components must be nonnegative and sum to one. This is an arithmetic check, but satisfying it does not prove that the likelihood model or report protocol was correctly chosen.

8. A zero-prior stratum contributes zero joint mass. Its elementary conditional likelihood is undefined; either skip that stratum or explicitly specify a generative kernel without claiming a ratio on a null event.

9. A positive-prior hypothesis with zero evidence likelihood receives zero posterior whenever total evidence is positive. This is a valid exclusion inside the model, unlike division by zero total evidence.

10. If every weighted likelihood is zero, conditioning on the observation is undefined in the elementary model. Returning equal posteriors would add an unsupported rule rather than apply Bayes.

11. Existing information must condition the priors and likelihoods consistently. Use the probability measure within that information event instead of combining population weights with subgroup rates.

12. Countably many hypotheses require a convergent nonnegative evidence sum. The random-family problem includes size zero, where the no-boys likelihood equals one rather than zero.

13. Weighted likelihoods may share a common positive factor that cancels in the posterior. The rescaled sum is not the absolute probability of the evidence unless that factor is restored.

14. A factor depending on the hypothesis cannot be canceled between competing weights. This includes different sample sizes, different report-selection probabilities, and different numbers of compatible histories.

15. The evidence probability lies between the smallest and largest likelihood on positive-prior strata. A value outside this range exposes an inconsistent input model before posterior calculation begins.

16. Recovering an intersection from a posterior requires multiplying by the evidence probability. Check the resulting joint table for nonnegative cells before claiming the inferred likelihoods are feasible.

### Base rates and detector quantities

17. Sensitivity is the positive-report probability within the target class. Positive predictive value is the target probability within positive reports; they coincide only under special model parameters.

18. Specificity is the negative-report probability within the background class. Negative predictive value is the background probability within negative reports and additionally depends on prevalence.

19. Complement a likelihood inside its conditioning class. The negative target likelihood is $1-s$, while the negative background likelihood is $1-f$; swapping them changes the model.

20. A rare class can have many fewer true positives than background false positives despite high sensitivity. Compare weighted joint masses rather than the two conditional rates alone.

21. Natural frequencies are exact scaled representations for rational model probabilities. They do not assert that an actual random sample must equal the displayed expected or synthetic counts.

22. In a frequency table, the positive posterior divides true positives by all positives. Dividing by all target cases instead calculates sensitivity, which answers a different question.

23. Negative target probability divides false negatives by all negatives. Do not confuse this with the false-negative rate, whose denominator is the entire target class.

24. Overall accuracy weights sensitivity and specificity by their class prevalences. An arithmetic mean of those rates is balanced accuracy, a separate criterion unless the classes are equally prevalent.

25. Always predicting background can have high accuracy when the target is rare. Its inability to detect targets matters under objectives that penalize false negatives differently from false positives.

26. A positive report is favorable evidence only if its likelihood is larger in the target class. Calling a report positive does not establish this inequality after additional conditioning.

27. With fixed positive sensitivity and false-positive rate, positive posterior is increasing in prevalence. A sharp prior interval therefore maps to a sharp posterior interval through its endpoints.

28. At a fixed interior prior, positive posterior increases with sensitivity and decreases with false-positive rate. Joint constraints on uncertain rates can prevent independently chosen corner values from being feasible.

29. Solving for a target credibility requires a positive denominator and an admissible prior. Report an out-of-range algebraic solution as infeasible or vacuous instead of a probability estimate.

30. When sensitivity equals false-positive rate, the positive event preserves the prior. The overall positive frequency then contains no information about prevalence within that model.

31. Known unequal class likelihoods and the overall evidence frequency identify the prior through an affine equation. Unknown likelihoods generally leave the inverse problem underdetermined.

32. A posterior near one is not a guarantee about every future case. It remains a conditional probability under the supplied model and evidence, which may be imperfectly specified.

### Odds and repeated observations

33. Convert probability r into odds $r/(1-r)$ and odds O into probability $O/(1+O)$. Treating odds as probability can yield impossible numbers or a wrong threshold.

34. A likelihood ratio above one increases posterior odds relative to prior odds. It need not make the target more likely than its complement when prior odds are very small.

35. The positive detector ratio is $s/f$ and the negative ratio is $(1-s)/(1-f)$ when denominators are positive. Negative reports can supply a larger absolute log-evidence change than positives.

36. Posterior odds between two members of a larger partition ignore other hypotheses in their ratio. Converting that ratio into a binary probability conditions on the pair, not on the full partition alone.

37. Evidence strength is relative to a competing model. Changing that competitor changes the likelihood ratio even if the likelihood under the target remains unchanged.

38. The general sequential update uses the likelihood of the new evidence given both hypothesis and prior history. A history-free likelihood needs a conditional-independence or other justified simplification.

39. Independence of observations given a fixed hypothesis does not imply their marginal independence after mixing over hypotheses. Learning the hidden state can couple predictions across trials.

40. Marginal independence does not establish independence inside every hypothesis. It cannot alone justify multiplying within-hypothesis likelihoods for a Bayesian update.

41. A copied report has conditional likelihood one under all hypotheses still compatible with the original. It contributes likelihood ratio one and must not repeat the original evidence factor.

42. Repeated independent observations of one fixed latent state update that state's posterior. Independently redrawing the state before every trial produces a different likelihood and prediction model.

43. Posterior predictive probabilities average the next observation's rates under posterior state weights. Plugging in only the most probable state discards remaining model uncertainty.

44. A specified sequence and an unordered count can share a posterior when their likelihoods differ by a common combinatorial factor. Their evidence probabilities still differ by that factor.

45. Without-replacement sampling changes conditional likelihoods after each draw. Squaring an initial proportion models replacement and is generally wrong for a remaining-content urn.

46. A coarse report such as at least one success requires summing all compatible histories. It cannot be replaced by exactly one success or by all successes without adding information.

47. Reversing the order of updates leaves the final posterior unchanged when both routes represent the same joint event under one coherent model. Intermediate conditionals may nevertheless differ.

48. Opposing full-history likelihood ratios can cancel, restoring the prior. Such cancellation says nothing about whether the joint history is common or rare in absolute probability.

49. A minimum number of reports is an integer threshold. After taking logarithms, verify the neighboring powers explicitly so rounding does not produce a number below the requirement.

50. A stopping report has a likelihood defined by its protocol. First success on trial three is the sequence failure-failure-success, not a report of one success in three unspecified positions.

51. Equal single-report likelihoods can conceal different joint likelihoods across hypotheses. Dependence structure itself may make a combined observation informative when each marginal report is uninformative.

52. Extremely small floating-point products can underflow to zero even when evidence is mathematically positive. A log-weight computation separates numerical failure from genuinely impossible evidence.

### Reporting and selection protocols

53. A truthful sentence alone need not specify how an observation was selected. The probability that each hypothesis generates the particular report must be modeled before applying Bayes.

54. At least one boy in a two-child family and a randomly observed child being a boy are different events. Their report likelihoods explain the one-third and one-half answers without contradiction.

55. Selecting a child uniformly across a population weights family sizes by the number of children. Selecting a family uniformly first does not create this size bias.

56. A size-biased distribution requires finite positive mean for normalization. Zero-size groups contribute no individual-selection opportunities, although they may have positive group-selection prior mass.

57. A knowledgeable host who always reveals an empty door has a different likelihood model from an ignorant host whose random opening happens to reveal an empty door.

58. For a particular door-opening report, an informed host's tie-breaking probability can change the switching posterior. The unconditional always-switch win rate need not change with it.

59. Conditional results must specify the exact observed opening, selection, or report event. A general strategy's unconditional success probability is not automatically the posterior for a particular report.

60. Randomly revealing a card face weights card types by their red-face multiplicities. Conditioning only on the presence of some red face ignores those unequal reporting opportunities.

61. Equal-weight evidence in a pair of coins retains heavy-heavy and light-light pairs. Their combinatorial counts, rather than equal category labels, determine the posterior weights.

62. Merging disjoint reports averages their posteriors with conditional report frequencies. The binary merged posterior must lie between the refined values and need not equal their simple average.

63. Refining information can raise or lower a specific hypothesis's posterior depending on the refined observation. More detail does not guarantee a higher probability for whichever target is being considered.

64. Rejection sampling from independent joint draws until matching evidence produces the posterior. Its expected number of attempts is the inverse evidence probability, so rare reports make it inefficient.

### Decisions, continuous models, and final checks

65. Maximum likelihood maximizes observation likelihood, while maximum posterior maximizes prior-weighted likelihood. They agree under equal priors but can disagree sharply under unequal ones.

66. Under zero-one classification loss, predicting hypothesis i has posterior risk one minus its posterior probability. This derivation establishes maximum posterior optimality for that specific loss.

67. Under unequal binary error costs and zero correct-decision costs, the target threshold is $c_{FP}/(c_{FP}+c_{FN})$. Costs determine an action threshold while leaving inference unchanged.

68. A threshold tie means both actions minimize expected loss. State any tie-breaking policy explicitly instead of claiming that one action has strictly lower risk at equality.

69. Adding an abstention action can outperform either class label. Maximum posterior is optimal among labels under zero-one loss, not necessarily among every action allowed by an expanded decision problem.

70. Observational conditioning does not by itself identify an intervention effect. A causal interpretation needs assumptions about what changes when a variable is externally set.

71. A continuous posterior is a density normalized by an integral. When the observation is continuous, the marginal denominator is a density and must not be called a singleton probability.

72. Posterior interval probabilities require integrating the density. A density value can exceed one and is not the probability that the parameter equals that exact value.

73. A uniform coin-rate prior and a history of h heads and t tails give density proportional to $\theta^h(1-\theta)^t$. The sampling-independence assumption is conditional on the common fixed rate.

74. The integer beta integral needs its explicit t-zero base case. Applying an integration-by-parts recurrence with a vanishing boundary term outside its assumptions can produce a false zero integral.

75. Under the uniform rate prior, the next-head prediction is $(h+1)/(h+t+2)$. This is a predictive probability under that prior, not a statement that every underlying rate equals this value.

76. Changing the prior density generally changes the posterior even with identical observations. A uniform density is a specified prior assumption, not an automatic representation of having no information.

77. Uniformity in one parameterization is not invariant under a nonlinear transformation. The transformed density must include the change-of-variable effect or be derived from its distribution function.

78. Distinct positive-likelihood paths toward an impossible event can have different posterior limits. The null-event elementary posterior therefore has no unique repair from algebra alone.

79. Before accepting an answer, check conditioning direction, partition coverage, likelihood history, positive evidence, normalization, parameter range, and the requested quantity. Then identify which tempting shortcut would answer a different question.

80. A finite simulation illustrates a stated mathematical model and its checkpoints. The general definitions and proofs remain necessary for new inputs; neither a simulation nor this chapter guarantees perfect performance on every unseen examination question.
