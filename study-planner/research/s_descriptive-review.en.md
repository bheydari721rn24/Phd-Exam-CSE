# Complete examination rules and final conceptual checks

Use these rules after reading the derivations. Each rule states its contract; a shortcut without its assumptions is not a valid solution.

1. Identify the observational unit before averaging. A student-weighted mean and an equally weighted mean of class means answer different questions when class sizes differ.

2. A numerical category code is not automatically a numerical measurement. Arbitrary recoding preserves category frequencies but can change its arithmetic mean completely.

3. Ordinal ordering permits rank comparisons but does not justify equal spacing between categories. A difference between adjacent codes need not represent equal scientific change.

4. Missing values are not zeros. Mean imputation leaves the observed mean unchanged while reducing the computed residual spread, so it must not be treated as neutral evidence.

5. Repeated measurements and duplicated rows are still separate recorded entries for descriptive arithmetic. They are not automatically independent observations for inference.

6. A frequency table of exact distinct values preserves the multiset but loses order. An interval frequency table additionally loses positions inside the intervals.

7. A density histogram's bin height is $f_j/(nw_j)$, where $w_j>0$ is the bin width. Its area, not its height, is the bin's empirical mass.

8. Unequal-width bins with equal counts must have different density heights. Comparing raw heights as if they were counts can reverse the visual conclusion.

9. State a nonoverlapping bin endpoint convention. In this chapter bins are left-closed and right-open, except that the last bin includes its final right endpoint.

10. Histogram mass is normalized by $\sum_j h_jw_j=1$. Summing heights alone is generally meaningless unless all widths are one in the chosen units.

11. An exact unweighted histogram also requires integer counts $nh_jw_j$. A normalized density with fractional implied counts is a model, not necessarily the exact display of the stated finite list.

12. Within-bin interpolation assumes a distribution of mass inside a bin. Counts alone cannot determine the exact fraction in a strict subinterval of that bin.

13. Bin boundaries can hide or create apparent modes. Check the observations or ECDF before concluding that a visible bump identifies a distinct population.

14. Sturges and Freedman–Diaconis are binning heuristics, not coverage theorems. A zero IQR can make the latter width degenerate despite a real extreme tail.

15. The ECDF is $F_n(t)=n^{-1}\#\{i:x_i\le t\}$. Its value includes all observations equal to the threshold, while its left limit excludes them.

16. The jump at a value is its empirical frequency. Tied records form one jump of multiplicity divided by sample size, not several separated value locations.

17. The interval $(a,b]$ has mass $F_n(b)-F_n(a)$. The interval $[a,b]$ instead has mass $F_n(b)-F_n(a^-)$; changing a bracket matters when endpoints are observed.

18. The interval $[a,b)$ has mass $F_n(b^-)-F_n(a^-)$. In a discrete empirical distribution, continuous-population habits of ignoring endpoint mass are unsafe.

19. An ECDF determines relative multiplicities, but not the sample size when the entire multiset may have been duplicated. It also cannot recover time order or paired-column identities.

20. The mean preserves the total: $\sum_i x_i=n\bar x$. For group means, multiply each mean by its group size before combining totals.

21. The mean uniquely minimizes squared loss on a nonempty list. The identity $\sum_i(x_i-c)^2=M_2+n(c-\bar x)^2$ proves this without calculus.

22. The weighted mean minimizes weighted squared loss when weights are nonnegative and their total is positive. Negative weights invalidate the ordinary mass and minimization interpretation.

23. The mean of ratios is not generally the ratio of totals. For overall speed, derive total distance divided by total time before selecting arithmetic or harmonic averaging.

24. Equal-distance speeds use a harmonic mean, while equal-time speeds use an arithmetic mean. The exposure contract determines the appropriate weighting.

25. Multiplicative growth uses positive factors and their geometric mean. Averaging signed percentage changes does not preserve the compounded product.

26. The midpoint median uses one middle record for odd size and the mean of two middle records for even size. It is a selected convention, not a universally shared definition of every 50th percentile.

27. Every center between the two middle records minimizes absolute loss for even size. The midpoint is one minimizer; uniqueness fails when those records differ.

28. A weighted absolute-loss minimizer has no more than half the total weight strictly on either side. A lower weighted median is the first value whose cumulative weight reaches half.

29. A mode maximizes frequency and minimizes categorical mismatch loss. The mode can be absent as a unique choice when several values tie for the largest count.

30. For nearest-rank quantiles with $0<p\le1$, use sorted position $\lceil np\rceil$. At $p=0$, the chapter explicitly uses the minimum; blindly using index zero would be invalid.

31. Type-7 quantiles use $h=1+(n-1)p$ and interpolate the surrounding order statistics. They can return a value never observed in the data.

32. Median-of-halves, nearest rank and type 7 can produce different quartiles on the same list. State the chosen convention before computing IQR, fences or a boxplot.

33. Increasing affine transformations preserve the order and commute with the stated quantile calculations. Decreasing transformations reverse ranks and require checking how each quantile convention treats the endpoints.

34. Midpoint medians commute with negative affine scaling. A lower nearest-rank median need not: for an even list it selects a different original middle record after reversal.

35. A quantile level is not a promise that exactly that percentage of finite records lies strictly below the returned value. Ties and finite rank increments prevent such an equality in general.

36. The centered sum $M_2=\sum_i(x_i-\bar x)^2$ is nonnegative. It vanishes exactly when every observation equals the same value.

37. Descriptive variance is $v=M_2/n$ for $n\ge1$. Corrected sample variance is $s^2=M_2/(n-1)$ only for $n>1$; a singleton's corrected variance is undefined rather than zero.

38. For a nonconstant list with $n>1$, $s^2=nv/(n-1)>v$. If both are zero, cancelling them to infer sample size is invalid.

39. Raw totals give $M_2=\sum_i x_i^2-(\sum_i x_i)^2/n$. Before normalizing, check that these totals satisfy Cauchy–Schwarz and produce no negative centered sum.

40. RMS measures distance from zero, not spread about the mean. Its exact relation is $RMS^2=v+\bar x^2$.

41. Under iid finite-variance sampling, $E[M_2]=(n-1)\sigma^2$. Independence makes $Var(\bar X)=\sigma^2/n$; normality is not needed for this expectation calculation.

42. Bessel correction does not repair arbitrary dependence or selection bias. Identical dependent readings can have zero sample spread even when their common random value has positive population variance.

43. Unbiased variance does not imply unbiased SD. Concavity of square root generally lowers $E[s]$ below $\sigma$, and reciprocals require separate positivity and integrability checks.

44. Frequency weights represent repeated records and use correction denominator $W-1$. Deterministic weights on independent equal-variance observations use $W-W_2/W$, where $W_2=\sum_iw_i^2$; the meanings cannot be interchanged.

45. The effective size $W^2/W_2$ describes the variance of a weighted mean under its sampling assumptions. It is neither the total weight nor a literal fractional count of people.

46. Translation changes the mean but leaves centered sums, variances, SD and IQR unchanged. An argument that SD rises by an added constant confuses origin with spread.

47. Under $Y=aX+b$, variance scales by $a^2$ and SD by $|a|$. A negative standard deviation is always an invalid result.

48. With descriptive standardization, score sum is zero and squared-score sum is $n$. With corrected standardization, squared-score sum is $n-1$; identify which score variance is one.

49. Standardization changes location and scale but does not make a distribution normal. Normal probabilities require a separate justified or explicitly supplied model.

50. CV is meaningful only with an appropriate nonzero reference mean and ratio-scale interpretation. It is invariant under positive unit scaling but changes under translation.

51. A boxplot fence is a threshold calculated from quartiles. A whisker ends at the furthest retained observed value, which need not equal that threshold.

52. Under the chapter's strict outlier rule, a value exactly on a fence is retained. If the upper fence itself is observed, it is necessarily the upper whisker.

53. A labelled boxplot outlier is a statistical flag, not proof of recording error. Deleting it requires evidence about data collection and the intended analysis.

54. Zero IQR or raw MAD does not imply zero variance. A heavily tied center with a single extreme observation provides a direct counterexample.

55. Median absolute deviation uses a median of absolute residuals about a median. Mean absolute deviation uses an average and a specified center; neither name should replace its actual definition.

56. Trimming removes records; Winsorization replaces extremes and retains the size. State the count changed at each end and recompute the resulting denominator.

57. Robustness does not mean exact invariance under every replacement. A changed middle record can alter the median even though sending a maximum farther away does not change that same median.

58. Reflection symmetry implies equal reflected frequencies, not merely an equal mean and median. Equal centers or zero third central moment provide too few constraints to prove symmetry.

59. Moment skewness requires $m_2>0$ and is $m_3/m_2^{3/2}$. Under negative scaling it changes sign; under translation it does not change.

60. Moment kurtosis is $m_4/m_2^2$, and excess subtracts 3. State this convention because some software uses bias-corrected variants and some informal sources reverse the excess sign.

61. Cauchy–Schwarz gives moment kurtosis at least one. Equality for an unweighted nonconstant list requires equal-magnitude positive and negative residuals with equal counts.

62. The heuristic $mode\approx3\,median-2\,mean$ is not an identity. Multimodal or irregular finite lists can violate familiar verbal skewness orderings.

63. For nonnegative data, at most $n\bar x/t$ observations can be at least $t>0$. Negative observations invalidate this finite Markov argument by allowing compensation in the total.

64. For centered spread, a tail record at distance at least $t$ costs at least $t^2$ of $M_2$. Therefore its count is at most $M_2/t^2$, with integer rounding and the correct variance denominator applied afterward.

65. A strict tail costs strictly more than $t^2$ per record. When the squared-energy ratio is an integer, the strict bound loses one compared with the closed bound; otherwise its floor may stay the same.

66. An upper bound is not automatically attainable. An extremal construction must satisfy both the prescribed squared-deviation sum and the zero signed-deviation sum.

67. A single centered residual satisfies $|d_i|\le\sqrt{(n-1)v}$. The other residuals must sum to its negative, and that constraint sharpens the simpler bound obtained from its own square alone.

68. For values in $[a,b]$, $v\le(b-\bar x)(\bar x-a)\le(b-a)^2/4$. A known mean can sharpen the unconditional range bound.

69. Equal-weight finite records impose integer endpoint masses. The exact unconstrained maximum range variance is $(b-a)^2\lfloor n^2/4\rfloor/n^2$, so odd size cannot attain the continuous half-and-half bound.

70. The normal 68–95–99.7 percentages concern a normal population. They are neither a theorem for arbitrary lists nor exact required frequencies in each sample from a normal population.

71. Midpoint group summaries describe a replaced list. They need not equal, consistently understate or consistently overstate the true raw variance; interval counts omit within-bin locations.

72. The midpoint mean error is at most the frequency-weighted average half-width. Endpoint inclusion determines whether the corresponding upper and lower limits are attained or only approached.

73. A histogram-interpolated quantile assumes constant density within its containing interval. It does not recover the exact middle records used by a raw midpoint median.

74. Combined $M_2$ equals within-group $M_2$ plus the weighted squared distances of group means from the combined mean. Averaging group variances without the between term discards real variation.

75. A pooled within-group estimator uses within sum and denominator $N-G$ under its model. Total descriptive variance instead includes between sum and divides by $N$; these quantities target different spreads.

76. Simpson reversal follows from comparing different mixture weights. Group-specific superiority can reverse in the aggregate, and neither comparison alone proves a causal effect.

77. Welford appending uses the old residual and new mean: $M_2'=M_2+\delta(x-\bar x')$. Appending at the mean leaves $M_2$ unchanged but decreases descriptive variance by increasing the count.

78. Correlation requires both columns to vary and preserves their original pairing. Zero correlation can coexist with a deterministic curve; a nonzero empirical correlation also does not logically disprove independence of the underlying population.

79. Pearson measures standardized linear association, Spearman uses average ranks with ties, and tie-free Kendall counts concordant minus discordant pairs. Independently sorting columns destroys record-level association, whereas Q–Q sorting intentionally compares distributions.

80. A trailing average uses an explicit startup denominator; a centered average requires future data. In EWMA forecasting, the previous summary predicts the next observation, while using the updated summary leaks the target into its own prediction.
