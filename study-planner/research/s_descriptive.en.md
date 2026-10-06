# Descriptive Statistics and Exploratory Data Analysis

## 1. Sources, scope, and a precise reading route

This chapter develops the mathematics of describing a finite data set before using it to infer properties of a population. Read the lesson before attempting the problems. The solved bank is available for study; it is not a diagnostic test that you must answer before learning. Keep a formula sheet containing the definitions, the denominator convention, and the assumptions behind every shortcut.

The reviewed core combines **MIT 15.075J** (Cynthia Rudin, Fall 2011, Chapter 4), **Stanford STATS60** (Michael Howes and Tselil Schramm, Spring 2026, Lectures 5, 7, and 8), **UC Berkeley SticiGui** (Philip B. Stark, Chapters 3, 4, and 8), and **CMU 36-309** (Howard Seltman, Experimental Design and Analysis, Chapter 4, selected sections). **Harvard's Introduction to Data Science** (Rafael Irizarry, Chapter 12) adds the empirical distribution, quantile plots, and robust summaries. The [source comparison](../reviews/s_descriptive-sources.html) gives exact reading scopes and explains why screened alternatives were not selected. These are five reviewed university teaching sources, not five catalogue links.

Oxford's historical IAUL notes were also examined as a comparison. Their incorrect numerical CV example, unclear moment normalization, and erroneous description of Kendall scoring are not propagated. University provenance does not replace checking an equation. We derive the formulas ourselves and distinguish exact identities from approximations and conventions.

The sequence is: identify observations and measurement scales; build frequency and distribution displays; derive location and spread; handle transformations, grouping, and updates; interpret shape and association; then solve mathematical and conceptual examination problems. The later probability, estimation, hypothesis-testing, and regression chapters develop sampling laws and inferential methods. Here we establish the descriptive foundations and a few clearly labelled bridges.

## 2. Observational units, variables, and measurement scales

An observational unit is the object about which a record is collected. If a file contains one row for each student and columns for ID, major, ordered satisfaction category, height, and number of absences, students are units and columns are variables. The row count is not necessarily the number of independent observations: ten repeated measurements from one student are ten measurements but only one sampled student. Independence matters later for inference, while the descriptive calculations remain defined for the actual recorded list.

An ID written as an integer is still a label. Averaging IDs does not describe the students. A nominal variable permits equality comparisons and category counts. An ordinal variable also permits ordering, but an arbitrary numerical coding does not make differences equal. An interval scale supports meaningful differences but has an arbitrary zero, such as Celsius temperature. A ratio scale has a meaningful zero and supports ratios, such as elapsed time or nonnegative counts. Discrete versus continuous is a different classification: a count is discrete and usually ratio-scaled; a rounded height remains a measurement of a continuous characteristic.

Changing an ordinal coding from 1, 2, 3 to 1, 10, 100 preserves ranks but can change the mean drastically. Changing Celsius to Fahrenheit preserves differences up to a positive scale factor but changes ratios and the coefficient of variation. Therefore choose a statistic from the measurement contract, not from the computer's numeric storage type.

A finite population can be a complete list of all relevant units. A sample is the observed subset or collection selected by a sampling mechanism. A descriptive statistic is any stated function of the observed list. A population parameter describes the target population. The same arithmetic average can be either a complete-population parameter or a sample statistic; the role depends on the target and collection design. A large convenience sample can describe itself accurately and still be biased for another population.

Before calculating, check units, impossible values, missing-value codes, repeated rows, and the meaning of weights. A missing entry is not zero. Replacing missing values by the observed mean preserves that observed mean but compresses the apparent spread. Reporting a correct formula on incorrectly coded data gives an incorrect scientific conclusion.

## 3. Frequency tables, histograms, and loss of information

Let the recorded numerical list be $x_1,\ldots,x_n$, with $n\ge1$. A frequency table for distinct values $v_j$ uses counts $f_j\ge0$ satisfying $\sum_j f_j=n$. Relative frequencies are $p_j=f_j/n$ and sum to one. This representation loses record order but retains the multiset. A table of interval counts loses the locations inside each interval as well.

For bin edges $b_0<b_1<\cdots<b_m$, this chapter uses $[b_{j-1},b_j)$, except that the final bin includes its right endpoint. Every covered observation must enter exactly one bin. Let bin width be $w_j=b_j-b_{j-1}$ and count be $f_j$. A count histogram is convenient when widths are equal. For a **density histogram**, the height is

$$h_j=\frac{f_j}{n w_j},\qquad h_jw_j=\frac{f_j}{n},\qquad \sum_j h_jw_j=1.$$

The area encodes mass. If two bins have equal counts and one is twice as wide, its density height is half as large. A height can exceed one because it has reciprocal measurement units; its area must respect the probability scale. A categorical bar chart has arbitrary category widths, so bar height encodes count or proportion directly. Never estimate a bin probability from density height alone.

For bins $[0,1)$ and $[1,3]$ with counts 2 and 6, the relative masses are $1/4$ and $3/4$ while density heights are $1/4$ and $3/8$. The right bin is only 1.5 times as tall but has three times the mass. Under a piecewise-uniform within-bin approximation, the estimated fraction in $[1,2]$ is $3/8$. The actual data could place all six right-bin observations above 2 or below 2, so the exact fraction is not determined.

Changing bin edges can change apparent modes without changing the observations. Try several meaningful widths and inspect the raw values or an ECDF as well. Sturges' heuristic uses approximately $1+\log_2 n$ bins. The Freedman–Diaconis heuristic uses width $2\,IQR\,n^{-1/3}$ when IQR is positive. Neither is a theorem guaranteeing discovery of every cluster; zero IQR, small samples, and extreme values require judgement. A stem-and-leaf display preserves values if the key is explicit: under key `2|7 = 27`, stem 2 with leaves 1, 4, 7 means 21, 24, 27.

<!-- SIM:histogram -->

## 4. The empirical distribution and its endpoint rules

The empirical cumulative distribution function is the fraction of observations at or below a threshold:

$$F_n(t)=\frac{1}{n}\sum_{i=1}^n\mathbf{1}\{x_i\le t\}.$$

It is nondecreasing, right-continuous, zero below the minimum and one at or above the maximum. At a repeated value $v$ with frequency $f$, its jump is $f/n$, not $1/n$. Treat the left limit $F_n(t^-)$ as the fraction strictly below $t$. Then endpoint-sensitive counts are exact:

$$\frac{\#\{i:a<x_i\le b\}}n=F_n(b)-F_n(a),\qquad \frac{\#\{i:a\le x_i\le b\}}n=F_n(b)-F_n(a^-).$$

For data $1,2,2,5$, $F_n(2)=3/4$ and $F_n(2^-)=1/4$. The fraction in $(2,5]$ is $1/4$; in $[2,5]$ it is $3/4$. A continuous distribution assigns zero probability to a singleton, but an empirical distribution does not. Importing continuous endpoint intuition into a finite list is a common examination error.

An exact ECDF determines the relative multiset frequencies. If the original sample size is known, jumps reveal multiplicities. If it is not known, duplicating every observation leaves the ECDF unchanged, so the exact number of records cannot be recovered. It also does not recover chronological order or the pairing between two columns.

<!-- SIM:ecdf -->

## 5. Arithmetic and weighted means: balance, totals, and quadratic loss

Write $S=\sum_i x_i$ and $\bar x=S/n$. The centered deviations sum to zero because $\sum_i(x_i-\bar x)=S-n\bar x=0$. A signed balance equation therefore identifies the mean. A mean need not occur among the data: the mean of 0 and 10 is 5. It is not automatically a likely or typical outcome in a multimodal data set.

For any proposed center $c$, expand $x_i-c=(x_i-\bar x)+(\bar x-c)$. The cross term vanishes on summing. Hence

$$\sum_{i=1}^n(x_i-c)^2=\sum_{i=1}^n(x_i-\bar x)^2+n(c-\bar x)^2.$$

This is both a proof and an examination shortcut. The unique minimizer of squared loss is $c=\bar x$. Moving the center by $d$ adds exactly $nd^2$. The proof requires no normality or independence because it is an identity for a fixed list. Dividing by $n$ gives the corresponding average-loss identity.

For nonnegative weights $w_i$ with positive total $W$, define $\bar x_w=\sum_i w_ix_i/W$. The same expansion gives weighted loss $\sum_i w_i(x_i-c)^2=M_{2,w}+W(c-\bar x_w)^2$. Frequency weights mean repeated observations; importance or reliability weights have a different statistical interpretation. The weighted descriptive variance $M_{2,w}/W$ is always defined when $W>0$, but no universal replacement of $n-1$ by $W-1$ is valid for every weight type.

When merging groups, use counts as weights. Groups of sizes 2 and 8 with means 10 and 20 have combined mean 18, not 15. Mean-of-means is correct only for equal group sizes or when the desired unit is the group itself rather than the individual. Always identify the denominator's observational unit.

<!-- SIM:mean -->

## 6. Medians, modes, quantiles, and the absolute-loss proof

Sort the observations as $x_{(1)}\le\cdots\le x_{(n)}$. The conventional midpoint median is $x_{((n+1)/2)}$ for odd $n$ and $(x_{(n/2)}+x_{(n/2+1)})/2$ for even $n$. At least half the observations are at or below a median and at least half are at or above it. Ties can make these fractions larger than one half.

The median minimizes $L(c)=\sum_i|x_i-c|$. Pair smallest with largest, second smallest with second largest, and so on. For a pair $a\le b$, $|a-c|+|b-c|\ge b-a$, with equality for every $c\in[a,b]$. For even $n$, the common intersection of all pair intervals is $[x_{(n/2)},x_{(n/2+1)}]$; every point of this interval minimizes total absolute loss. For odd $n$, the unpaired middle observation forces the minimizer to that middle value. The midpoint convention chooses one minimizer; it does not prove uniqueness for an even list with a middle gap.

The mode is any value with largest frequency. Under zero-one mismatch loss $\sum_i\mathbf{1}\{x_i\ne c\}$, a mode minimizes the number of disagreements. Distinct values can tie as modes. A histogram's modal bin is not necessarily the raw-data mode and depends on binning.

For $0<p\le1$, the inverse-ECDF or nearest-rank quantile is

$$q_p^{NR}=\inf\{t:F_n(t)\ge p\}=x_{(\lceil np\rceil)}.$$

At $p=0$ we explicitly set the empirical quantile to the minimum. This convention chooses the lower middle observation at $p=1/2$ for even $n$. It differs from the midpoint median. For linear interpolation commonly called type 7, use $h=1+(n-1)p$, $j=\lfloor h\rfloor$, and $g=h-j$:

$$q_p^{7}=(1-g)x_{(j)}+g x_{(j+1)},\qquad 0\le p\le1,$$

with endpoint cases $q_0^7=x_{(1)}$ and $q_1^7=x_{(n)}$. For $1,5,8,15$, type-7 quartiles are 4, 6.5, 9.75, while nearest-rank quartiles are 1, 5, 8. Neither disagreement is an arithmetic error. Median-of-halves is another convention and must state whether an odd middle observation is included or excluded.

Interpolated quartiles need not leave exactly 25% of a tied finite sample below each boundary. Increasing affine transformations commute with either convention. Under a decreasing transformation, type 7 reverses the order and maps $q_p$ to the transformed $q_{1-p}$; nearest-rank can select the other endpoint of a jump. For nearest-rank, derive the transformed rank rather than applying an unqualified symmetry rule.

<!-- SIM:quantiles -->
<!-- SIM:loss -->

## 7. Variance, standard deviation, and two different denominators

Define centered sum of squares $M_2=\sum_i(x_i-\bar x)^2$. This chapter distinguishes the **descriptive list variance** $v=M_2/n$ from the **Bessel-corrected sample variance** $s^2=M_2/(n-1)$ for $n\ge2$. Their relation is $s^2=nv/(n-1)$. Both describe spread; the second also has an unbiased-estimation property under a specified sampling model. The phrase “sample variance” without a formula can be ambiguous across course conventions.

Expansion gives a useful identity:

$$M_2=\sum_i x_i^2-\frac{(\sum_i x_i)^2}{n},\qquad v=\frac1n\sum_i x_i^2-\bar x^2.$$

For $2,4,4,6$, the mean is 4, deviations are $-2,0,0,2$, and $M_2=8$. Thus $v=2$, $s^2=8/3$, descriptive SD is $\sqrt2$, and corrected SD is $\sqrt{8/3}$. Averaging deviations gives zero, not SD. Averaging absolute deviations gives 1 here, which is another legitimate spread measure but is not either SD.

Variance is nonnegative and is zero exactly when every recorded value equals the mean. SD is its nonnegative square root. If measurements have units $u$, variance has units $u^2$ and SD has units $u$. The root mean square of the raw observations satisfies $RMS^2=v+\bar x^2$. RMS measures size relative to zero; SD measures spread relative to the mean.

At $n=1$, descriptive variance is zero and corrected sample variance is undefined. For an empty list, even the mean is undefined. Dividing by zero and silently returning zero is not a valid convention. If the mean is known in advance and squared residuals are taken around that population mean, the usual unbiased denominator is $n$; estimating the center from the same observations changes the expectation of the residual sum.

<!-- SIM:variance -->

## 8. Why Bessel's correction works, and when it does not

Let $X_1,\ldots,X_n$ be independent identically distributed observations with finite mean $\mu$ and variance $\sigma^2$. This paragraph concerns repeated sampling, not a single fixed list. Use the earlier identity around $\mu$:

$$\sum_i(X_i-\bar X)^2=\sum_i(X_i-\mu)^2-n(\bar X-\mu)^2.$$

The expected first term is $n\sigma^2$. Independence gives $Var(\bar X)=\sigma^2/n$, so the expected second term is $\sigma^2$. Therefore $E[M_2]=(n-1)\sigma^2$, $E[v]=(n-1)\sigma^2/n$, and $E[s^2]=\sigma^2$. Normality is not needed for this unbiasedness proof. Independence, identical first two moments, and finite variance are the actual assumptions used. The separate chi-square sampling law requires normality and belongs to a later chapter.

The residuals obey one linear constraint, $\sum_i(X_i-\bar X)=0$, which motivates $n-1$ degrees of freedom. This is not a claim that the residuals are independent. With a common variance and nonzero pairwise covariances,

$$Var(\bar X)=\frac{n\sigma^2+2\sum_{i<j}Cov(X_i,X_j)}{n^2},\qquad E[M_2]=n\sigma^2-nVar(\bar X).$$

If all observations are the same random variable, the measured residual spread is identically zero even when that random variable has positive variance. Bessel's correction cannot recover variability absent from the sampling design. Also, unbiased variance does not imply unbiased SD: square root is concave, so $E[s]\le\sigma$ when expectations exist. Equality generally fails for a nondegenerate sampling law. Nor does it imply unbiased reciprocal variance.

For deterministic reliability weights and iid observations, let $W=\sum_iw_i$ and $W_2=\sum_iw_i^2$. The expected weighted centered sum is $\sigma^2(W-W_2/W)$. An unbiased weighted variance therefore divides by $W-W_2/W$, when this denominator is positive. This result describes one independently sampled observation per weight, not a table whose integer weight means that many separate observations. In a true frequency table of $W$ independent records, Bessel's denominator is $W-1$.

To derive the weighted correction, let $\bar X_w=\sum_iw_iX_i/W$. Expansion around the population mean gives $M_{2,w}=\sum_iw_i(X_i-\mu)^2-W(\bar X_w-\mu)^2$. The first expectation is $W\sigma^2$; independence and fixed weights give $Var(\bar X_w)=\sigma^2W_2/W^2$. Subtracting the second expectation yields the claimed denominator. The weighted mean therefore has the same variance as an unweighted mean of effective size $n_{eff}=W^2/W_2$. This is a variance-equivalence calculation, not an actual count of sampled people. If all positive mass is on one record, $W_2=W^2$ and the correction denominator is zero, consistently with having no independent information about spread.

## 9. Affine transformations, standard scores, and relative dispersion

For $y_i=ax_i+b$, the mean is $\bar y=a\bar x+b$, centered deviations are $a(x_i-\bar x)$, and

$$M_{2,y}=a^2M_{2,x},\qquad v_y=a^2v_x,\qquad s_y=|a|s_x.$$

Translation changes location but not spread. Negative scaling reverses order without making SD negative. For $a=0$, the transformed data are constant; correlation and standard scores that require positive spread become undefined. The midpoint median transforms as $a\,med(x)+b$ for either sign of $a$, because its two middle endpoints reverse together. Range scales by $|a|$. Type-7 IQR also scales by $|a|$; nearest-rank requires its explicit rank convention under reversal.

If $v>0$, descriptive standard scores are $z_i=(x_i-\bar x)/\sqrt v$. They sum to zero and satisfy $\sum_i z_i^2=n$. Their descriptive variance is one. If instead $z_i=(x_i-\bar x)/s$, the squared scores sum to $n-1$ and their corrected sample variance is one, while their descriptive variance is $(n-1)/n$. Always match the normalization to the requested denominator. A standard score is a relative distance; it is not a probability or percentile unless a reference distribution is specified.

For positive ratio-scale data with positive mean, $CV=s/\bar x$ is a dimensionless relative-spread measure; some conventions multiply it by 100%. Positive unit changes preserve it, but adding a constant changes it. A Celsius CV depends on an arbitrary zero and is not a meaningful unit-invariant relative comparison. Near a zero mean the ratio is unstable; a negative mean makes the ordinary positive-dispersion interpretation inappropriate. Using $|\bar x|$ is an explicit alternative, not a universal cure.

<!-- SIM:affine -->

## 10. Range, IQR, MAD, trimming, and boxplot construction

The range is maximum minus minimum. The interquartile range is $Q_3-Q_1$ under a stated quantile convention. The median absolute deviation about the median is

$$MAD=med_i\bigl(|x_i-med(x)|\bigr).$$

This MAD is different from the **mean** absolute deviation about the mean. State the words when a source uses the same abbreviation differently. A normal-consistency scaling of about 1.4826 is sometimes applied to MAD; raw MAD and scaled MAD are distinct. Zero IQR or zero MAD does not force constant data: a large tied central block can coexist with extreme observations.

A $k$-trimmed mean removes the lowest and highest $k$ order statistics and averages the remaining $n-2k>0$ records. A $k$-Winsorized mean replaces those extremes by the nearest retained boundary values while keeping $n$ records. Trimming and Winsorizing change the target summary; never delete an unusual measurement without a substantive reason and a record of the decision.

For a type-7 Tukey-style boxplot in this chapter, calculate $Q_1,Q_2,Q_3$, $IQR$, lower fence $L=Q_1-1.5IQR$, and upper fence $U=Q_3+1.5IQR$. Whiskers end at the smallest and largest **observed** values inside $[L,U]$. Observations strictly outside the fences are plotted individually. The fences themselves are not generally observed values and are not the whisker endpoints. A value exactly on a fence is retained. The boxplot label must disclose the quartile convention because software hinges can differ from type 7.

For $1,2,3,4,5,6,7,20$, type 7 gives $Q_1=2.75$, median 4.5, and $Q_3=6.25$. IQR is 3.5 and fences are $-2.5$ and 11.5. Whiskers end at 1 and 7, and 20 is plotted separately. A boxplot does not reveal the raw mean, modes, exact number of repeated outliers hidden behind one point, or every detail of the tails. Overlaying raw dots can reveal those missing facts.

<!-- SIM:box -->

## 11. Shape: symmetry, skewness, kurtosis, and limits of shortcuts

A finite multiset is symmetric about $c$ if reflection $x\mapsto2c-x$ preserves frequencies. Then its mean and midpoint median equal $c$. The converse fails: $0,2,3,3,7$ has mean and median 3 but is not symmetric. Symmetry does not imply unimodality; two equal clusters on opposite sides of zero can be symmetric.

Define empirical central moments $m_r=n^{-1}\sum_i(x_i-\bar x)^r$. For $m_2>0$, moment skewness is $g_1=m_3/m_2^{3/2}$, moment kurtosis is $b_2=m_4/m_2^2$, and excess kurtosis is $g_2=b_2-3$. Software bias corrections use different formulas; the definition must accompany a numerical answer. By Cauchy–Schwarz applied to squared deviations, $b_2\ge1$. High kurtosis means large standardized fourth-power contribution; a verbal description of “peakedness” alone is insufficient.

Positive skewness and a long right tail often accompany a mean above the median, but this is not a universal theorem about all multimodal finite lists. Pearson's heuristic $mode\approx3\,median-2\,mean$ is an approximation for some moderately skewed distributions, not an identity. The zero third moment is also insufficient to prove symmetry. For values $-2,-1,1,3$ with weights 4, 1, 6, 1, the total weight is 12, the weighted sum is zero, and the weighted cubic sum is zero. The second central moment is 8/3, yet reflected masses differ because neither 2 nor -3 occurs.

Under nonzero affine scaling, moment skewness changes by $sign(a)$ and kurtosis is unchanged. Fourth-power outlier contributions grow rapidly. Normal-population kurtosis is 3 and excess is zero, but a finite sample from that population need not have those exact values. A constant list has no defined standardized skewness or kurtosis because the denominator vanishes.

## 12. Exact finite-list bounds and cautious normal approximations

For any nonnegative list and threshold $t>0$, let $k$ observations satisfy $x_i\ge t$. Their contribution to the total is at least $kt$, so $k/n\le\bar x/t$. This is the finite-list Markov bound. It is invalid for a list containing negative values unless another nonnegative quantity is used.

For any list with $v>0$, apply the same argument to squared centered deviations. If $k$ observations have $|x_i-\bar x|\ge t\sqrt v$, then $kt^2v\le nv$ and

$$\frac{k}{n}\le\frac1{t^2}.$$

This is a deterministic counting bound, with integer consequence $k\le\lfloor n/t^2\rfloor$. For strict outside endpoints use the corresponding strict inequality before integer rounding; this can strengthen an integer bound when $n/t^2$ is an integer. Using corrected $s$ instead changes the non-strict bound to $k\le\lfloor(n-1)/t^2\rfloor$. These are upper bounds, not predictions that the fraction equals the bound.

A useful range bound follows if all values lie in $[a,b]$. Each product $(x_i-a)(b-x_i)$ is nonnegative. Averaging and rearranging gives $v\le(b-\bar x)(\bar x-a)\le(b-a)^2/4$. Equality in the last bound needs the mean at the midpoint and all observations at the endpoints with equal masses. For odd $n$, equal endpoint masses are impossible, so the sharp finite-list maximum is $(b-a)^2\lfloor n^2/4\rfloor/n^2$.

For a **normal population**, a value within one, two, and three population SDs has probability about 0.6827, 0.9545, and 0.9973. Arbitrary data have no such guarantee. Standardizing does not make a distribution normal. Under a stated model $X\sim N(\mu,\sigma^2)$, $P(X\le c)=\Phi((c-\mu)/\sigma)$; two-sided intervals require subtracting two CDF values. The original examination bridge in the bank tests exactly this distinction.

## 13. Grouped data and what midpoint approximations cannot recover

For grouped interval counts, midpoint $c_j=(b_{j-1}+b_j)/2$ gives approximate mean $\widetilde x=\sum_j f_jc_j/n$ and approximate descriptive variance $\widetilde v=\sum_j f_j(c_j-\widetilde x)^2/n$. These are exact summaries of the **midpoint-replaced** list. They are not necessarily exact summaries of the original observations.

If every bin has width at most $h$, replacing an observation by its midpoint changes it by at most $h/2$. Therefore $|\bar x-\widetilde x|\le h/2$. More specifically, an exact mean lies between $\sum_j f_jb_{j-1}/n$ and $\sum_j f_jb_j/n$, with endpoint attainability affected by half-open bins. No corresponding equality for variance follows from these mean bounds. Inside-bin locations can either increase or decrease the midpoint variance.

For a piecewise-uniform interpolation of grouped quantiles, let the desired cumulative mass $pn$ lie in a bin with lower edge $L$, width $h$, bin count $f>0$, and prior cumulative count $C$. The estimate is $L+h(pn-C)/f$. It locates area in the **histogram model**, not an exact order statistic in the unavailable raw data. Empty bins, quantiles on a cumulative boundary, and open-ended classes need explicit conventions. The familiar grouped-mode interpolation also assumes a local histogram shape and must not be presented as an exact raw-data mode.

If the true mean within each group and its within-group centered sum are known, exact pooling becomes possible. Counts alone are insufficient. This distinction turns apparent formula substitution problems into information-sufficiency problems.

## 14. Pooling groups: within variation and between variation

Let group $g$ have size $n_g>0$, mean $\bar x_g$, and centered sum $M_{2,g}$. With $N=\sum_gn_g$ and combined mean $\bar x=\sum_gn_g\bar x_g/N$, expand each observation around its group mean. The cross term vanishes separately in each group:

$$M_{2,total}=\sum_g M_{2,g}+\sum_g n_g(\bar x_g-\bar x)^2.$$

The first part is within-group variation; the second is between-group variation. The second can be positive even when every group is internally constant. For two groups with sizes $n_A,n_B$ and mean gap $\Delta=\bar x_B-\bar x_A$,

$$M_{2,total}=M_{2,A}+M_{2,B}+\frac{n_An_B}{n_A+n_B}\Delta^2.$$

For two constant groups $0,0$ and $6,6$, both internal variances are zero, but combined mean is 3 and combined $M_2=36$, giving $v=9$ and $s^2=12$. Averaging the two group variances produces zero and discards the mean gap.

If group variances are corrected sample variances, replace $M_{2,g}$ by $(n_g-1)s_g^2$ before pooling. A statistical “pooled within-group variance” divides only the within sum by $N-G$ and targets a common within-group variance under a model. It is different from the total descriptive variance, which includes between variation and divides by $N$. The later inference chapter explains the model; here the arithmetic distinction is exact.

Simpson's reversal occurs when group-specific rates and aggregate rates compare different mixtures. For easy tasks, A succeeds in 9/10 and B in 80/100; for hard tasks, A succeeds in 30/100 and B in 2/10. A is better within each group, yet aggregate A is 39/110 and B is 82/110. The unequal weights reverse the aggregate comparison. This observation by itself does not identify the causal treatment effect.

<!-- SIM:pooling -->

## 15. Adding, deleting, correcting, and streaming observations

Keep the triplet $(n,\bar x,M_2)$ rather than raw totals alone. When appending value $x$, let $\delta=x-\bar x$. The new mean and centered sum are

$$\bar x'=\bar x+\frac{\delta}{n+1},\qquad M_2'=M_2+\frac{n}{n+1}\delta^2=M_2+\delta(x-\bar x').$$

The derivation is a two-group merge with the singleton's internal sum zero. Adding a value at the existing mean leaves $M_2$ unchanged but decreases descriptive variance because the count rises. Adding a distant value increases $M_2$, yet the variance change also depends on the new denominator. Specifically $v'>v$ exactly when $\delta^2>(n+1)v/n$.

To delete one observed value from a list with $n>1$, the remaining mean is $\bar x'=(n\bar x-x)/(n-1)$ and $M_2'=M_2-n(x-\bar x)^2/(n-1)$. Correcting a recorded value $u$ to $u+d$ keeps $n$ fixed and gives $\bar x'=\bar x+d/n$ and $M_2'=M_2+2d(u-\bar x)+d^2(1-1/n)$. A legal deletion cannot produce negative $M_2$ in exact arithmetic; a negative computed value indicates arithmetic error, inconsistent input summaries, or numerical roundoff.

The append recurrence is Welford's algorithm. Unlike subtracting nearly equal large totals $\sum x_i^2-S^2/n$, it usually avoids severe cancellation when measurements are large but deviations are small. It still uses finite precision and is not a universal error-free guarantee. For integer examples, exact rational arithmetic can audit the recurrence. Merging two Welford summaries uses the two-group formula above and supports parallel accumulation.

```python
def descriptive_summary(values):
    # The input must be nonempty, finite, and already validated.
    n, mean, m2 = 0, 0.0, 0.0
    for x in values:
        n += 1
        delta = x - mean
        mean += delta / n
        m2 += delta * (x - mean)
    if n == 0:
        raise ValueError("The empty list has no mean or variance.")
    return n, mean, m2 / n, (m2 / (n - 1) if n > 1 else None)
```

This code performs $O(n)$ arithmetic operations and uses constant extra storage. `None` explicitly distinguishes undefined corrected variance from zero. It does not automatically reject infinities or missing-value strings; validation is part of the caller's contract.

<!-- SIM:stream -->

## 16. Paired data, covariance, and correlation

Keep record pairing fixed. For paired observations $(x_i,y_i)$, define $C=\sum_i(x_i-\bar x)(y_i-\bar y)$, descriptive covariance $C/n$, and corrected covariance $C/(n-1)$. When both centered sums $M_{2,x},M_{2,y}$ are positive,

$$r=\frac{C}{\sqrt{M_{2,x}M_{2,y}}}.$$

The denominator convention cancels if used consistently. Cauchy–Schwarz gives $|C|\le\sqrt{M_{2,x}M_{2,y}}$, so $-1\le r\le1$. Equality requires the centered vectors to be nonzero scalar multiples: all observed pairs lie on a nonhorizontal, nonvertical straight line. A constant variable makes correlation undefined, not zero. Under $u=ax+b$ and $v=cy+d$ with $a,c\ne0$, covariance scales by $ac$ and correlation by $sign(ac)$.

Sorting the columns independently destroys pairing and can manufacture a strong correlation. For $x=(-1,0,1)$ and $y=(1,0,1)$, covariance and correlation are zero even though $y=x^2$ is deterministic. Zero correlation concerns linear association and does not establish independence or absence of dependence.

Conversely, nonzero empirical correlation does not logically disprove independence of the population variables: independent random samples can display accidental correlation. Population independence with finite second moments forces population covariance zero, but a descriptive statistic from one finite list is not an exact statement about that population parameter. The two levels of reasoning must be kept separate when an examination question supplies sample versus population moments.

For paired sums, descriptive variance obeys $v_{x+y}=v_x+v_y+2C/n$; for differences the sign reverses. Thus “variances add” needs zero covariance, and independence is a sufficient probabilistic condition rather than a descriptive assumption about arbitrary lists. The regression slope with an intercept is $C/M_{2,x}=r\sqrt{v_y/v_x}$ when $v_x>0$. Equal correlation does not imply equal slope or equal scatter geometry. Full regression inference is deferred.

Spearman correlation is Pearson correlation of within-column average ranks. For no ties, it also equals $1-6\sum_i d_i^2/[n(n^2-1)]$. With ties, use average ranks and Pearson's formula rather than this unadjusted shortcut. For tie-free Kendall correlation, each pair contributes $+1$ if the two differences have the same sign and $-1$ if they have opposite signs; $\tau=(N_c-N_d)/\binom n2$. Tie-corrected variants require additional denominator rules. A perfect rank association can be nonlinear in the original scale.

<!-- SIM:correlation -->

## 17. Quantile plots, smooth displays, and time order

A Q–Q plot compares ordered sample values to reference quantiles at explicitly stated plotting probabilities. For a normal-reference plot, use $p_i=(i-1/2)/n$ and $z_i=\Phi^{-1}(p_i)$, then plot $(z_i,x_{(i)})$. Normal-shaped data produce an approximately straight trend whose intercept and slope reflect location and scale. Repeated values form horizontal bands under this axis orientation. Tail bending is evidence against the chosen shape, not a proof that a particular alternative distribution generated the sample. Reversing axes reverses the visual interpretation of curvature.

For two samples, compare the same probability quantiles, not simply record number when sample sizes differ. An affine increasing relation between the quantile functions appears as a straight line. A smooth density estimate introduces a bandwidth; too much smoothing can merge modes and too little can create unstable bumps. It does not turn every bump into a scientifically distinct population. The ECDF is an exact finite-list representation; a smoothed curve is a model-dependent display.

Chronological order is additional information. A histogram or mean cannot distinguish $1,2,3,4$ from $4,3,2,1$, while their time trends are opposite. A trailing moving average of width $w$ at time $t\ge w$ is $MA_t=w^{-1}\sum_{j=t-w+1}^t x_j$. At the start, either delay output until a full window exists or state a shorter-window denominator. A centered moving average uses future observations and therefore is not available for real-time forecasting without delay.

An exponentially weighted moving average uses $E_t=\lambda x_t+(1-\lambda)E_{t-1}$ with $0<\lambda\le1$ and a stated initial value. Expanding gives $E_t=\lambda\sum_{j=1}^t(1-\lambda)^{t-j}x_j+(1-\lambda)^tE_0$. The geometric weights including the initialization sum to one. Larger $\lambda$ responds more quickly and smooths less. A one-step forecast uses the previous summary $E_{t-1}$; using $E_t$ leaks the observation being predicted into its own forecast.

<!-- SIM:qq -->
<!-- SIM:smoothing -->

## 18. Complete summary and problem-solving workflow

First identify the observational unit, numerical scale, raw versus grouped input, and any weights or pairings. Second record the exact median/quantile and variance definitions. Third convert the given summaries to counts, totals, and centered sums; then derive the requested answer before comparing alternatives. Fourth check units, nonnegativity, endpoints, and information sufficiency. Finally state whether the result is exact, a bound, a within-bin approximation, or a conclusion requiring a population model.

The mean preserves totals and minimizes squared loss. Every absolute-loss median lies in the middle interval and is resistant to a few extreme replacements. The mode minimizes mismatch loss. Variance measures centered quadratic spread; SD is its square root; RMS includes the squared location as well. IQR and MAD emphasize central structure and can be zero despite nonconstant data.

For transformations, location changes linearly while variance changes quadratically and SD uses the absolute scale factor. Pooling requires within and between variation. Updating count, mean, and centered sum avoids repeatedly reconstructing the list. Correlation describes paired linear association, is undefined for a constant column, and does not identify causation. Graphs and numerical summaries answer different questions, so inspect both.

The most important exact identities are $M_2=\sum x_i^2-S^2/n$, $\sum(x_i-c)^2=M_2+n(c-\bar x)^2$, $s^2=nv/(n-1)$, and $M_{2,total}=\sum_gM_{2,g}+\sum_gn_g(\bar x_g-\bar x)^2$. Derive their conditions rather than memorizing disconnected formulas. The final rule bank applies them to boundary cases, adversarial examples, and examination distractors.

## 19. Worked mathematical and conceptual problems

Each solution gives assumptions, calculation or proof, and the mistake that would lead to a plausible incorrect answer. Course-inspired problems use independently specified data and wording. Exact original-examination adaptations are labelled separately with archive commit, booklet, page, and printed option order. Their answers are independently derived; they are not represented as official answer keys.

<!-- INCLUDE:problems -->

## 20. Examination rules and advanced pitfalls

Read these complete rules after the lesson. Each states an actionable condition, consequence, or counterexample; none replaces the derivation above.

<!-- INCLUDE:review -->

## 21. Editable visual laboratories

The laboratories compute the actual states for your supplied data. They start paused and support step, back, seek, restart, speed, and reduced-motion display. A histogram model uses its declared endpoint rule; a quantile or box model states type 7 versus nearest rank. Finite displayed cases illustrate proofs and do not replace them. Print includes checkpoints and their explanations.

<!-- LAB:statistics -->

## 22. References and verification boundaries

1. MIT, **15.075J / ESD.07J, Statistical Thinking and Data Analysis**, Fall 2011. Cynthia Rudin; course co-instructors Allison Chang and Dimitrios Bisias. [Chapter 4: Summarizing Numerical Data](https://ocw.mit.edu/courses/15-075j-statistical-thinking-and-data-analysis-fall-2011/e8d615e72bb6d384e34fc2a10a8f03cb_MIT15_075JF11_chpt04.pdf), PDF pages 1–7 reviewed.
2. Stanford, **STATS60 / STATS160 / PSYCH10**, Spring 2026. Michael Howes and Tselil Schramm. [Lecture 5](https://web.stanford.edu/class/stats60/lectures/05-lecture-mean.html), [Lecture 7](https://web.stanford.edu/class/stats60/lectures/07-lecture-variability.html), and [Lecture 8](https://web.stanford.edu/class/stats60/lectures/08-lecture-robustness.html), relevant full textual lecture bodies reviewed.
3. UC Berkeley, **SticiGui**, Philip B. Stark. [Chapter 3: Histograms](https://www.stat.berkeley.edu/~stark/SticiGui/Text/histograms.htm), frequency tables through percentiles; [Chapter 4: Location and Spread](https://www.stat.berkeley.edu/~stark/SticiGui/Text/location.htm), location/loss, spread, affine maps, Markov and Chebyshev sections; [Chapter 8: Computing Correlation](https://www.stat.berkeley.edu/~stark/SticiGui/Text/computeR.htm), full textual chapter reviewed.
4. Carnegie Mellon, **36-309, Experimental Design and Analysis**, Howard Seltman. [Chapter 4: Exploratory Data Analysis](https://www.stat.cmu.edu/~hseltman/309/Book/chapter4.pdf), PDF pages 1–24 reviewed, especially sections 4.1–4.3.4. Graphical conventions and small-sample caveats were compared with the other sources.
5. Harvard, **Introduction to Data Science**, Rafael Irizarry. [Chapter 12: Summary Statistics](https://rafalab.dfci.harvard.edu/dsbook/summary-statistics.html), sections 12.1–12.8 and 12.9.1–12.9.2 reviewed. Empirical distributions, density displays, quantile plots, stratification, and outlier effects are the complementary scope.
6. Oxford, **Descriptive Statistics for Research**, IAUL and Department of Statistics, Hilary Term 2002. [Lecture 1](https://www.stats.ox.ac.uk/pub/bdr/IAUL/Course1Notes1.pdf), PDF pages 11–22 examined as a historical comparison. Individual author attribution is unconfirmed. Identified mathematical/numerical defects are documented in the source audit; this is not one of the five selected core sources.
7. Iranian examination archive, [Phd-Exam-CSE, Exams](https://github.com/bheydari721rn24/Phd-Exam-CSE/tree/bdadf6e2c9cadc4772ae137a96a3da753c7cfd08/Exams). Only the named original pages in the authentic bank were checked for this chapter. No archive-wide question-coverage claim is made.

The [quality audit](../reviews/s_descriptive-quality.html) distinguishes proof, finite mathematical tests, original-PDF checking, and browser verification. Candidate comparison is bounded to located accessible material and cannot certify a globally exhaustive ranking of every university course. No finite chapter or audit guarantees performance on every unseen question. The goal is deep, explicitly checked preparation whose remaining limitations are visible.
