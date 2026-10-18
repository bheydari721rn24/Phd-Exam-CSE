# Rank chapter: original examination recheck, 18 October 2026

Both original PDFs were downloaded from the pinned repository commit `bdadf6e2c9cadc4772ae137a96a3da753c7cfd08`. Their actual source pages were rendered and visually inspected. Both hashes match the chapter's pinned fingerprints. These are two existing authentic revisits, not newly added distinct examination questions. No official answer key was used.

## MSc Computer Science 1405, Q41, PDF p. 9

Original wording and all four options agree with the English record: real symmetric 4-by-4 matrices with zero trace; proposed dimensions 10, 9, 8 and 7.

Symmetry leaves four independent diagonal coordinates and six independent off-diagonal coordinates. Trace is a nonzero linear functional on that ten-dimensional space. Its kernel consequently has dimension nine. A concrete basis consists of six matrices `Eij+Eji`, with `i<j`, together with `E11−E44`, `E22−E44` and `E33−E44`. Independently flattening these nine matrices into 16-component columns gives exact rank nine; every matrix is symmetric with trace zero.

**Independently derived answer:** option 2, dimension 9. No translation or answer correction is required.

SHA-256: `198f75f9f9d195adc5c09ab14d17029e63a3cd11030d62cffcdfcb5df7627527`.

## PhD Computer Science 1404, Q30, PDF p. 8

Original wording and all four options agree with the English record: a real square matrix has a positive uniform lower bound `||Ax|| ≥ θ||x||`; identify the false assertion. The options are the inverse norm upper bound, positive definiteness, nonsingularity and the eigenvalue modulus lower bound.

The lower bound first makes the kernel trivial, hence the finite square matrix invertible. Substituting `x=A^{-1}y` gives `||A^{-1}y|| ≤ θ^{-1}||y||`, which yields the induced inverse norm bound. Under the Euclidean convention, applying the squared real inequality to the real and imaginary parts extends it to complex vectors, so a complex eigenvector gives `|λ| ≥ θ`. Finally, `A=−I` preserves norm while its nonzero-vector quadratic form is negative. Positive definiteness is therefore not implied.

**Independently derived answer:** option 2. No translation or answer correction is required. The source page does not explicitly name the norm; the current solution correctly labels the Euclidean hypothesis used in its complex-eigenvector derivation. That scope must remain explicit rather than silently assuming an arbitrary complexified norm is an isometry.

SHA-256: `928e51b55059b3094583f9c190e260b405ec775da05f6c7679675e332a8a6f40`.

## Provenance

- [Pinned MSc source](https://github.com/bheydari721rn24/Phd-Exam-CSE/blob/bdadf6e2c9cadc4772ae137a96a3da753c7cfd08/Exams/MS/CS/1405/Q257A-Arshad1405-%5Bwww.konkur.in%5D.pdf).
- [Pinned PhD source](https://github.com/bheydari721rn24/Phd-Exam-CSE/blob/bdadf6e2c9cadc4772ae137a96a3da753c7cfd08/Exams/Phd/CS/1404/Q892A-PHD1404-%5Bwww.konkur.in%5D.pdf).

The companion JSON records acquisition URLs and local image paths. Original full PDFs and source-page renderings are kept outside repository assets. Mathematical solutions are independent derivations, not claimed official answer-key entries.
