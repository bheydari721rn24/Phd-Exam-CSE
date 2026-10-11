# Orthogonality: written-course comparison and source audit

## Scope and selection

The bounded candidate pool contains seven universities. Selected core courses are Oxford M1 Linear Algebra I, MIT 18.06SC, Berkeley Math54, and ETH Zurich Linear Algebra for Computer Scientists. Selection follows actual chapter-specific reading: Oxford supplies the real and complex axioms and inequality proofs; MIT supplies complements, rectangular orthonormal matrices and two explicitly reconstructed exercises; Berkeley supplies scanned geometric calculations and polynomial examples; ETH supplies a complete inductive Gram–Schmidt proof and precise reduced-QR dimensions. No claim is made to have read every course worldwide or every assignment in a course.

| University and course | Actual reviewed material | Decision |
|---|---|---|
| Oxford, M1 Linear Algebra I 2022–23, lecturer Andrew Wathen | Native PDF pages70–78, including the complex convention checked against the rendered final page | Core for axioms, Gram forms, inequalities and real/complex boundaries |
| MIT, 18.06SC Fall2011, Gilbert Strang | Session2.1 summary teaching pages1–2; Session2.4 summary teaching pages1–3; exercises17.1–17.2 and solution teaching pages1–2 | Core for decompositions, rectangular matrices and exercise reconstruction |
| Berkeley, Math54 Spring2018, Alexander Paulin | All19 native scanned pages: Inner Products4, Orthogonal Sets3, Orthogonal Projections4, Inner Product Spaces4, Gram-Schmidt4 | Core for geometry and worked polynomial/vector examples; one erroneous polynomial example is corrected below |
| ETH Zurich, Linear Algebra for Computer Scientists PartII, Afonso S. Bandeira and Robert Weismantel, updated29October2025 | Entire section6.3, printed/native pages19–23, ending before section6.4 | Core for ordered-span induction and reduced QR; full PDF is not claimed read |
| Stanford, EE263 Autumn2007–08, Stephen Boyd, Lecture3 | Native pages14–16, two slides per physical page | Additional norm, distance, angle and halfspace comparison; this excerpt alone does not cover projections or Gram–Schmidt |
| CMU, 21-241 SummerI2014, William Gunther | Day18 all3pages, Day19 all4pages, Day20 all4pages, official PDF text | Additional orthogonal-set and complement comparison; source typos preclude uncritical adoption |
| Harvard, Math55a Honors Abstract Algebra, official notes under Curtis McMullen's course archive | Native PDF pages12–13 on projection, orthonormal-basis induction and Hermitian/function examples | Additional conceptual comparison; the compressed exposition needs expanded steps and a single declared complex convention |

The four core courses collectively cover the chapter, rather than each individually covering every extension. Weighted geometry, exact implementation, dependent-generator handling, Householder construction, commuting-projector proofs and complex counterexamples below are independently derived synthesis. The advanced numerical algorithm survey is introductory; a full floating-point stability theorem and infinite-dimensional Hilbert-space theory are outside this finite-dimensional chapter.

## Reading and corrections

1. Oxford's trigonometric example on native page74 uses unrestricted distinct integer indices for cosines. Distinct indices are insufficient when they are negatives of one another. With unrestricted integers the condition is distinct absolute frequencies; with nonnegative frequencies ordinary distinctness is enough.
2. Oxford's complex convention is linear in the first argument. This chapter consistently uses conjugate linearity in the first argument and linearity in the second, so every projection coefficient is translated accordingly. Missing conjugate bars in PDF text extraction are not accepted as mathematical statements.
3. Berkeley Inner Product Spaces page4 asks for projection of the odd polynomial x cubed onto the even span of one and x squared on the symmetric interval, but displays a nonzero coefficient. Both relevant integrals are zero. The correct projection is zero. The nearby fourth-power problem, independently derived here, has a nonzero answer and is labelled separately.
4. Berkeley Orthogonal Projections page1 has a vector/subspace equality where membership is required. The residual belongs to the orthogonal complement; it is not equal to that subspace.
5. Stanford's unsigned arccosine angle is in zero through pi. Its later mention of negative pi over two for orthogonality does not follow that convention. A zero vector has no defined angle.
6. CMU Day18 omits the nonzero-vector condition in one independence statement; Day19 restores it. Day18/Day19 printed norm lines omit the square root, confirmed against their native rendered pages; the chapter defines length from the square root of the self-product.
7. CMU Day20's displayed empty intersection is incompatible with both subspaces containing zero. The correct intersection is the singleton zero. The row/null dimension sentence also contains a slip: their dimensions sum to the ambient dimension and are generally unequal.
8. MIT's printed projection expression, confirmed on native summary page2, in Session2.4 is checked by dimensions. For an m-by-r column basis, the correct matrix is Q times inverse of Q transpose Q times Q transpose, with no extra leading transpose. The manuscript derives it independently rather than copying the erroneous printed expression.

## References and written material

- Oxford: [M1 Linear Algebra I notes, native pages70–78](https://courses.maths.ox.ac.uk/pluginfile.php/25471/mod_folder/content/0/lecture_notes22.pdf?forcedownload=1).
- MIT: [Orthogonal Vectors and Subspaces](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/least-squares-determinants-and-eigenvalues/orthogonal-vectors-and-subspaces/); [Session2.1 written summary](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/fdce42d9c8d8dc4eac7a9db3c1978e18_MIT18_06SCF11_Ses2.1sum.pdf); [Session2.4 written summary](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/7ac32be444c25e48590f47573833ccc6_MIT18_06SCF11_Ses2.4sum.pdf); [exercises17.1–17.2](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/b0aca3af754666dff0ab394cf36afaec_MIT18_06SCF11_Ses2.4prob.pdf); [solutions](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/e1f9595692038807071733916a514cbd_MIT18_06SCF11_Ses2.4sol.pdf).
- Berkeley: [Math54 course](https://math.berkeley.edu/~apaulin/54_001(Spring2018).html); [Inner Products](https://math.berkeley.edu/~apaulin/Inner%20Products,%20Length%20and%20Orthogonality.pdf); [Orthogonal Sets](https://math.berkeley.edu/~apaulin/Orthogonal%20Sets.pdf); [Orthogonal Projections](https://math.berkeley.edu/~apaulin/Orthogonal%20Projections.pdf); [Inner Product Spaces](https://math.berkeley.edu/~apaulin/Inner%20Product%20Spaces.pdf); [Gram-Schmidt](https://math.berkeley.edu/~apaulin/Gram-Schmidt.pdf).
- ETH Zurich: [PartII, section6.3, native pages19–23](https://ti.inf.ethz.ch/ew/courses/LA25/notes_part_II.pdf).
- Stanford: [EE263 Lecture3, native pages14–16](https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/lectures/lin-alg2.pdf).
- CMU: [course](https://www.math.cmu.edu/~wgunther/241/m14/index.html); [Day18](https://www.math.cmu.edu/~wgunther/241/m14/notes/week4/18.pdf); [Day19](https://www.math.cmu.edu/~wgunther/241/m14/notes/week5/19.pdf); [Day20](https://www.math.cmu.edu/~wgunther/241/m14/notes/week5/20.pdf).
- Harvard: [Math55a written notes, native pages12–13](https://abel.math.harvard.edu/~ctm/home/text/class/harvard/55a/08/html/home/course/course.pdf).

Acquisition failures are recorded rather than replaced by invented hashes. Actual reading may use the official PDF through the research browser when a local network download fails. Scanned Berkeley originals and the complex Oxford page were viewed natively. A successful later download adds provenance, not a retroactive claim of reading additional pages.
