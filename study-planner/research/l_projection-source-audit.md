# Orthogonal projections: active source evaluation

Status: in progress. This is a chapter-specific research record, not a completed or published chapter.

## Bounded comparison and actual reading

The previous orthogonality review supplies documented reading from Oxford, MIT, Berkeley, ETH Zurich, Stanford, CMU and Harvard. Those exact ranges remain references, not a claim that their worldwide catalogs have been exhausted. For this chapter, the following additional official written material was actually read:

- Stanford EE263 Autumn2007–08, Stephen Boyd, Lecture5, Least-squares: all23 teaching pages were returned and read through the official PDF research browser. Pages1–10 supply the projection matrix, orthogonality principle, rectangular/full QR and complementary-space representations. Later estimation examples are contextual reading; detailed regression/statistical estimation is reserved for the scheduled least-squares chapter.
- MIT18.06SC Fall2011, Gilbert Strang, Session2.3 summary: all three teaching pages read; page4 is the license. The worked fitting example and Gram-invertibility proof were checked conceptually.
- MIT Session2.3 solutions: both teaching pages were read, covering exercises16.1–16.6; page3 is the license. Their short answers require independent derivations before chapter use.

Four prospective core courses are MIT, Stanford, Oxford and Berkeley, with ETH's precise QR proof as an additional reference. Final selection will be recorded after the chapter-specific coverage matrix and native figures are reviewed. A local cached download is not required for official-PDF reading, but no hash will be invented for an unavailable cache.

## Conventions and qualifications found

1. Stanford uses the residual Ax minus y; MIT uses data minus fitted values. This chapter will consistently use r=b-Pb. Both residuals are perpendicular, but their signs must not be mixed in formulas or diagrams.
2. The inverse of A transpose A requires independent columns. Dependent-generator examples must retain a column basis or use a correctly derived Moore–Penrose inverse; the physical projection remains unique even when its generator coefficients do not.
3. MIT's line-fitting text first refers to distance to a line and then explicitly describes vertical residuals. Vertical least squares in the data plot differs from shortest perpendicular distance to that plotted line. The column-space residual is perpendicular in the observation-vector space.
4. MIT exercise16.5 places the solution coefficients in the row space under its full-column-rank hypothesis. This statement must not be extended to every solution of a rank-deficient normal equation; only the minimum-norm coefficient solution has that property generally.
5. Stanford's introductory definition of unbiasedness is a deterministic left-inverse condition. Statistical BLUE statements additionally need explicit noise assumptions. They are outside the core projection chapter and will be qualified in the next scheduled least-squares chapter.

## Written references

- [Stanford EE263 Lecture5, Stephen Boyd](https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/lectures/ls.pdf).
- [MIT Session2.3 summary, Gilbert Strang](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/198bde3a6536b62989b6cc09495575c1_MIT18_06SCF11_Ses2.3sum.pdf).
- [MIT Session2.3 exercise solutions](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/815ad23f78e11c1a7d282022fc2db3a9_MIT18_06SCF11_Ses2.3sol.pdf).
- [Oxford M1 Linear Algebra I, Andrew Wathen, pages70–78](https://courses.maths.ox.ac.uk/pluginfile.php/25471/mod_folder/content/0/lecture_notes22.pdf?forcedownload=1).
- [Berkeley Math54, Alexander Paulin, Orthogonal Projections](https://math.berkeley.edu/~apaulin/Orthogonal%20Projections.pdf).
- [ETH Zurich Linear Algebra PartII, section6.3, Bandeira and Weismantel](https://ti.inf.ethz.ch/ew/courses/LA25/notes_part_II.pdf).

## Pending work

Complete the coverage matrix, reconstruct the selected exercises, derive the advanced projector identities and dependent/weighted/affine cases, author the full solved bank and final rules, build mechanism-specific models, and perform independent mathematical and actual-browser review. This record supplies no completed chapter count.
