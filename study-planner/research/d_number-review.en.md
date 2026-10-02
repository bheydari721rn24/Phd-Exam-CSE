### A complete conceptual summary

Divisibility states that an integer product witness exists. The division theorem selects a unique quotient and nonnegative remainder for a positive modulus. Euclid preserves the set of common divisors while reducing a positive remainder; extended Euclid additionally carries signed linear-combination coefficients. The resulting Bézout certificate proves that all integer combinations are precisely the multiples of the gcd. Prime factorization then turns divisibility into coordinatewise exponent comparisons, with gcd as minimum and lcm as maximum.

Congruence identifies integers with equal canonical remainders. Addition, subtraction, and multiplication preserve those classes, but ordinary division and arbitrary exponent reduction do not. Units are exactly the residues coprime to the modulus. A linear congruence has an empty fiber unless the gcd divides its target; otherwise the reduced equation has one class modulo the reduced modulus and exactly as many original residue solutions as that gcd. CRT combines compatible residue requirements: a product period is justified by pairwise coprimality, while shared factors require agreement and yield an lcm period.

Euler's theorem concerns unit bases, and multiplicative order is their exact power period. Nonunits may pass through a transient before entering a cycle; prime-power valuations identify vanishing coordinates and CRT recombines them with unit coordinates. Repeated squaring computes powers without requiring Euler's premise. Divisor functions and factorial valuations count exponent choices and contributions without constructing huge integers. Wilson provides a true prime criterion, while passing one Fermat test is not a proof of primality. Mathematical RSA correctness follows coordinate by coordinate, including messages that are nonunits.

### Select the method from the requested conclusion

| Requested conclusion | First decision | Complete method | Final verification |
| --- | --- | --- | --- |
| Canonical remainder | Is the modulus positive? | Use floor division and its interval. | Check the product identity and remainder bounds. |
| Gcd or a common-divisor certificate | Normalize signs and handle zero inputs. | Euclid; carry coefficients if needed. | Check the gcd divides both inputs and substitute Bézout. |
| Integer solutions | Does the gcd divide the target? | Scale a Bézout witness and parameterize every solution. | Substitute and prove the difference family is complete. |
| Nonnegative or bounded solutions | What inequalities constrain the parameter? | Intersect their integer bounds. | Check endpoints and count the allowed parameters. |
| Linear congruence | Does the coefficient/modulus gcd divide the target? | Reduce all three integers and invert in the reduced modulus. | Lift every original residue and substitute. |
| Modular system | Are the reduced residue conditions compatible? | Merge with generalized CRT or use coprime selectors. | Check each equation and justify the lcm period. |
| Huge power | Is the base a unit in each prime-power coordinate? | Use order/Euler for unit coordinates, valuation thresholds for others, or repeated squaring. | Recombine and check boundary exponents. |
| Root count | Is the modulus prime, a prime power, or a product? | Prove local roots and combine coprime coordinates. | Establish completeness, not merely a list of witnesses. |

### Definitions, signs, and zero boundaries

1. To prove $a ∣ b$, exhibit an integer product witness; a rational quotient is insufficient.
2. Every integer divides zero, but zero divides only zero; this does not define arithmetic division by zero.
3. Divisibility is a partial order on nonnegative integers but fails antisymmetry on all integers because opposite signs divide one another.
4. State that the modulus is positive before using the unique interval $0 ≤ r<m$.
5. A negative dividend requires floor division for a nonnegative mathematical remainder; truncation toward zero can produce a different convention.
6. Congruence is a relation, whereas the remainder is a canonical integer; replacing one notation with the other must preserve the statement's type.
7. The canonical gcd is nonnegative; normalize input signs instead of returning a negative common divisor.
8. At the two-zero input, gcd zero is an explicit convention or a divisibility-order extension, not a greatest positive numerical divisor.
9. A congruence modulo one is automatic; handle this before asking for inverses, fields, or orders.
10. A complete answer should state whether it gives one canonical residue, all integer representatives, or all residues in a specified original modulus.

### Euclid, prime factors, and integer equations

11. Prove Euclid's step by showing equality of the entire common-divisor sets through the two linear-combination identities.
12. A decreasing nonnegative remainder proves termination; the gcd invariant alone proves only preservation of the desired value.
13. Count Euclid's divisions logarithmically in input magnitude, then separately account for the bit cost of each division.
14. Consecutive Fibonacci inputs have long quotient chains, but do not assert that every quotient, including the last, is one.
15. Extended Euclid must update remainder coefficients using the old values; parallel assignment or saved temporaries preserve that requirement.
16. Check a Bézout certificate by exact substitution and verify that its claimed gcd divides both inputs.
17. Integer combinations are exactly gcd multiples; nonnegative combinations form a smaller set and require additional inequalities.
18. A linear equation is consistent over integers precisely when its gcd divides its target, except that two zero coefficients must be handled directly.
19. From one particular solution, write both parameter directions and prove that every other solution differs in that way.
20. Convert nonnegative, positive, and inventory constraints into integer bounds on the same parameter before counting.
21. The count of a nonempty parameter interval is its upper endpoint minus its lower endpoint plus one; an inverted interval gives zero solutions.
22. Euclid's prime-product lemma requires primality or an explicit coprimality condition; a composite divisor of a product need not divide one factor.
23. Existence of prime factorization uses strong induction; uniqueness requires the prime-product lemma and matching cancellation.
24. In the infinitude proof, a product of listed primes plus one needs a new prime divisor and need not itself be prime.
25. Pairwise coprimality implies an overall gcd of one for a finite family of at least two members; the converse fails for six, ten, and fifteen.
26. Coprimality is not transitive; two and three, and three and four, are coprime while two and four are not.
27. Take prime-exponent minima for gcd and maxima for lcm; use the signed product identity with absolute value.
28. Gcd and lcm are meet and join for divisibility, so justify their universal divisor and multiple properties instead of relying only on numerical sizes.

### Inverses, cancellation, and solution fibers

29. Reduce intermediate sums and products freely after proving congruence compatibility; that permission does not include an exponent's control value.
30. A residue has an inverse exactly when it is coprime to the modulus; being nonzero is sufficient only under a prime modulus.
31. A nonzero nonunit is a zero divisor and explains why cancellation can lose information in a composite ring.
32. To cancel a factor $a$ from a congruence modulo $m$, replace the modulus by $m/gcd(a,m)$; keeping the old modulus is justified only for a unit.
33. In a linear congruence, first test whether the gcd divides the target; failed divisibility proves inconsistency without searching residues.
34. When reducing a solvable linear congruence, divide the coefficient, target, and modulus by the same gcd.
35. The reduced equation has one residue class, but it corresponds to exactly gcd-many residues in the original interval.
36. If the reduced modulus is one, all original residues solve the equation and no ordinary inverse computation is required.
37. Multiplication by $a$ modulo $m$ has image size $m/gcd(a,m)$ and attainable fibers of size $gcd(a,m)$.
38. The kernel consists of evenly spaced multiples of the reduced modulus; translate it to obtain any other nonempty fiber.
39. A multiplication map on residues is injective, surjective, and bijective under the same unit condition, because its domain and codomain are the same finite set.
40. Validate a lifted solution by substituting it into the original equation, not only into the reduced equation.

### Systems and exponentiation

41. CRT gives uniqueness modulo a period, not a unique integer in the whole integer line.
42. The coprime-selector formula requires pairwise coprime moduli; checking only the gcd of all moduli is insufficient.
43. For two shared-factor moduli, the target difference must be divisible by their gcd, and the solution period is their lcm.
44. For several congruences, pairwise residue compatibility is sufficient because the strongest condition at each prime power dominates all weaker ones.
45. Reduce coefficient equations to residue conditions before applying CRT; the resulting moduli can differ substantially from the originals.
46. After solving a periodic event system, impose any “first after” time threshold with a ceiling operation.
47. CRT preserves multiplication as well as addition, so it can combine power computations and local root choices.
48. Euler reduction requires a unit base; Fermat's unit version additionally requires a prime modulus.
49. The all-base Fermat form is $a^p ≡ a$; it does not assert $a^{p−1} ≡ 1$ for bases divisible by the prime.
50. The exact multiplicative order divides the totient and is the first returning exponent, not necessarily the totient itself.
51. An order claim needs a minimality check; one returning power provides only a period bound.
52. Negative modular exponents require a multiplicative inverse and therefore a unit base.
53. Nonunit power sequences can have a transient; periodicity after a threshold does not authorize reduction to an exponent before that threshold.
54. In a prime-power coordinate, a base with positive valuation vanishes when exponent times valuation reaches the modulus exponent.
55. A power tower requires an explicit exponent modulus for the outer computation; reducing every level by the original modulus is invalid.
56. Repeated squaring works for nonunits too; its invariant uses the remaining exponent rather than assuming Euler's theorem.
57. The iterative power loop has one iteration per binary exponent digit for positive exponents and no iterations for exponent zero.
58. For modulus one, the canonical empty-product residue is zero, even though the integer empty product is one.

### Counting, roots, and primality reasoning

59. Divisor count and sum formulas use independent prime-exponent choices; multiply them across coprime factors, not overlapping ones.
60. A positive integer has an odd number of divisors exactly when it is a square, including one.
61. Factorial valuations count all prime-power contributions; a binomial valuation subtracts both denominator factorial valuations.
62. In a composite base, each trailing zero consumes the base's full prime-exponent pattern, so divide each available valuation by the corresponding base exponent before taking the minimum.
63. Root counts over a field cannot be transferred to a composite ring; prove local prime-power roots and use CRT for completeness.
64. The square-zero condition modulo a prime power is a ceiling valuation threshold, not a demand that the whole modulus divide the unsquared input.
65. Wilson's theorem is an equivalence for integers at least two, but its exactness alone does not provide a fast bit algorithm.
66. A failed coprime-base Fermat congruence proves compositeness; passing one proves only that this base failed to expose it.
67. Additive step cycles have length equal to modulus divided by the step/modulus gcd; an array rotation must visit every disjoint cycle.
68. Prove mathematical RSA recovery in each prime coordinate, treating zero and nonzero messages separately, so that nonunits are included.
69. Distinguish correctness of an arithmetic transformation from claims about practical security or current cryptographic recommendations.
70. End a solution with a completeness argument and a premise check; finding one correct residue is not enough when all solutions or an exact count were requested.

### A reusable solution-writing procedure

State the input domain and modulus conventions. Translate the goal into divisibility, a linear equation, a residue fiber, or prime-power coordinates. Check the theorem's hypotheses before simplifying. Derive a certificate or parameter family and retain the correct modulus. Impose any inequalities, count distinct residues or parameters, and substitute into the original problem. Finally explain why no additional solutions exist and identify the boundary case that would invalidate the tempting shortcut.
