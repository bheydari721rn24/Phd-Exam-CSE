# Variance and covariance: written-source comparison

## Search boundary and selection

This is a chapter-specific evaluation of nine accessible university course inventories, not an assertion that all courses worldwide were found. Written text, proof detail, second-moment breadth, conditional decomposition, and suitability for formula/concept problems determine selection. University prestige alone does not determine rank. Rankings below describe complementary roles rather than a universal league table. Six universities supplied text actually read for this chapter. Video content is excluded.

|Role|University, course and attribution|Actual chapter reading|Contribution and limitation|
|---|---|---|---|
|Core: visual foundations|MIT, 18.05, Spring 2022. Course instructors Jeremy Orloff and Jennifer French Kamrin; combined probability-note authors Jeremy Orloff and Jonathan Bloom.|Combined PDF pages 46–51, 70–76, 103–112; all listed prose and mathematical derivations read. Plot-glyph extraction artifacts were filtered on pages 108–110.|Discrete/continuous variance, overlap, covariance and correlation proofs. Several worked-example transcription errors require independent correction; conditional decomposition is supplemented by CMU.|
|Core: conditional and multivariate extension|CMU, 36-700, Fall 2016, Siva Balakrishnan.|Lecture 3 pages 7–8; Lecture 4 all eight pages read in official text, with native reinspection of pages 5 and 8.|Quadratic-form variance, Cauchy–Schwarz, conditional variance and the tower law. Correct the dependent-average variance, exponential parameter wording, and chi-square definition.|
|Core: rigorous assumptions and continuous examples|Oxford, Prelims Probability, Michaelmas 2019, James Martin.|PDF pages 1–3, 23–29, 57, 64–68 read completely; earlier unrelated pages 30–35 are not counted as variance coverage.|Absolute-integrability assumptions, joint laws, continuous covariance, Gaussian factorization and Chebyshev/WLLN. Conditional variance needs another course; the Markov proof has a strict-inequality typo.|
|Core: computational examination patterns|Berkeley, CS70, Lecture 17, Spring 2016, Rao and Walrand, hosted in the Fall 2016 archive.|All five variance-note pages read in official text; original PDF acquired.|Indicator expansions, random walks, fixed points, uniform and binomial variance. Fixed-point variance requires the omitted n≥2 condition. It does not establish general independence from zero covariance.|
|Additional: integrability and matrix transformation|ETH Zurich, Probability Theory, FS2020, Johanna F. Ziegel, translated by Alexander Henzi.|Native PDF title page and pages 8 and 16 read in full.|Square-integrability, covariance-matrix definition, independence/product proof, affine matrix transformation. This is a selected section review, not a full reading of the 58-page course.|
|Additional: foundational proof contrast|Cornell, CS2800, Fall2017, Lecture9; no lecturer name established from the lecture page.|Entire official HTML lecture reread.|Expectation as a functional, variance algebra, product expectation and review exercises. Finite-space explanations cannot justify infinite-space manipulations without integrability.|
|Screened only|Stanford, CS109 Summer2019, Noah Arthurs.|Course inventory and instructor verified; advertised variance-note acquisition in an earlier chapter returned mismatched content, so it is not counted here.|Relevant variance/conditional-joint materials exist; no claim that its written variance chapter was actually reviewed in this chapter.|
|Screened only|Harvard, Stat110, Joe Blitzstein; textbook by Joe Blitzstein and Jessica Hwang.|Official course home and free-textbook availability verified.|Promising supplementary probability text; book chapters not read for this delivery and not counted.|
|Screened only|Cambridge, Introduction to Probability 2024–25, Mateja Jamnik and Thomas Sauerwald on indexed handout title.|Official search inventory identifies independence/covariance handout; the directly attempted handout returned HTTP404.|A broken attempted address is not evidence that all Cambridge text is unavailable; not counted as read.|

## Actual comparison and synthesis choices

MIT's foundation is strongest for the progression from probability-weighted distances to jointly varying measurements. Berkeley adds exact indicator reasoning that avoids constructing a large distribution. Oxford supplies assumptions and a derivation of the Gaussian exception. CMU supplies the conditional decomposition missing from those foundations. ETH strengthens matrix and existence conditions; Cornell contrasts probability-space sums with value-space sums. This combination was selected after comparing the available chapter text and identifying these gaps. No random four-course selection or globally-best claim is made.

## Corrections incorporated

1. MIT combined PDF page106 states a cubic joint density but later writes x+y, and substitutes 7/12 for its actual mean13/20 in a centered integral. The chapter recomputes E[XY]=2/5, both variances31/400, covariance−9/400 and correlation−9/31 from the stated cubic density.
2. MIT page76's half-line standard-normal first-moment integral equals 1/sqrt(2π), not1. This does not affect the zero full mean, but the intermediate computation must be corrected.
3. CMU Lectures3/4 write sigma instead of sigma squared for the variance of an average of identical random variables. The correct variance is sigma squared.
4. CMU Lecture4 page6 calls the exponential rate lambda a mean. For density lambda exp(−lambda x), the mean is1/lambda. Its unit-rate MGF diverges also at t=1.
5. CMU Lecture4 page8 initially writes the square of a sum for chi-square. Chi-square is the sum of squares of independent standard normals; equal means do not make these laws equal.
6. Oxford page68 says the conditional mean on {Y≥t} is strictly greater than t. The valid inequality is ≥t, allowing equality and sharpness.
7. Berkeley fixed-point variance equals1 for n≥2; for n=1 the sole permutation has one fixed point and variance0. The general calculation cannot divide by n(n−1) at n=1.
8. Correlation requires both variances finite and strictly positive. Independence implies zero covariance only where covariance is defined; a degenerate variable has zero covariance with every square-integrable variable but no defined Pearson correlation.

## Source links and exact identities

- MIT 18.05 combined probability notes: https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/mit18_05_s22_probability.pdf
- MIT course attribution: https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/
- CMU Lecture3: https://www.stat.cmu.edu/~siva/teaching/700/lec3.pdf
- CMU Lecture4: https://www.stat.cmu.edu/~siva/teaching/700/lec4.pdf
- Oxford Probability: https://courses.maths.ox.ac.uk/mod/resource/view.php?id=48553
- Berkeley CS70 Lecture17: https://fa16.eecs70.org/static/notes/n17.pdf
- ETH Probability Theory: https://people.math.ethz.ch/~ziegelj/WTSkript.pdf
- Cornell Lecture9: https://www.cs.cornell.edu/courses/cs2800/2017fa/lectures/lec09-expect.html
- Stanford screened inventory: https://web.stanford.edu/class/archive/cs/cs109/cs109.1198/
- Harvard screened inventory: https://stat110.hsites.harvard.edu/
- Cambridge attempted handout: https://www.cl.cam.ac.uk/teaching/2425/IntroProb/slides/07-covariance-all-handout.pdf

Cached document hashes and acquisition outcomes are in s_variance-evidence/acquisition.json. MIT combined PDF SHA256: 32896358099cebefe133b2c92fe4324f4ef4745328eed0937f5d04d21c039ab2. Oxford PDF SHA256: 0a04507ba176bbb5185d0eb5111bb8bd2b0274597ad1ac139f1dad0dc753a635. CMU Lecture3 SHA256: 4c0ddda389679134676c5770fd82e6d882b7e4d52d9a1c40df98955f11ced333. Acquisition is not a claim of reading every downloaded page.

## Exercise provenance and remaining boundaries

Original problems are authored independently. Reconstructed course exercise types cite the precise section without reproducing a full university question bank. Iranian items record their immutable repository path, original PDF page, ordered options, verified hash and independently derived answer; no official key is claimed. General measure-theoretic existence proofs, a complete distribution catalogue, estimation theory and multivariate Gaussian integration belong to later chapters. Their required second-moment interfaces are taught here.
