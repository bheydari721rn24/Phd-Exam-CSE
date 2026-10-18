# Original-examination recheck for p_functions

Review date: 18 October 2026. Read-only review; no checkout or source-PDF changes.

## Method and provenance

Both original PDFs were reopened, their complete relevant pages rendered with PyMuPDF at 1.5x and visually inspected. The MS options were additionally inspected in 3x and 5x detail renders. Their bytes were independently compared with `git show` output at pinned archive commit `bdadf6e2c9cadc4772ae137a96a3da753c7cfd08`. Both pinned Git-blob SHA256 values match the original files and the existing provenance records. Raster-only original questions were not inferred from deficient PDF text extraction. No official answer key was located or verified; all answers below are independently derived.

## MS CS 1393, Q167, PDF page 34

- Repository path: `Exams/MS/CS/1393/olum_93_konkurcomputer.pdf`.
- Local original: `C:/Users/bheydari/Desktop/Phd-Exam-CSE/Exams/MS/CS/1393/olum_93_konkurcomputer.pdf`.
- SHA256, local and pinned blob: `7ed89fae8eb601a964355fde5e5d297cbb30844e5240b9e3908b798fb86e349d`.
- Full-page render: `MS_CS_1393_Q167.png`.
- Enlarged alternatives 3 and 4: `MS_CS_1393_Q167_options34.png`.

The stem asks to copy alternate elements of an N-element array a, beginning at its final element, into b in forward destination order; a and b are global. The outside call is `store(N-1,0)`.

All four original functions have `if(n<0)return;`. The original alternative bodies are:

1. `b[i]=a[n]; store(n-2,i+1);`
2. `b[i+1]=a[n]; store(n-2,i+1);`
3. `b[i]=a[n]; store(n-2,i+2);`
4. `b[i+1]=a[n]; store(n-2,i+2);`

**Actual error in current p_functions-authentic.json:** alternative 4 has been transcribed as `store(n-1,i+2)`. The original clearly prints `n-2`. Accordingly the existing explanation that alternative 4 uses source stride one is also incorrect. All four alternatives decrease the source index by two. Alternative 4 is wrong because it begins at destination index 1 and then leaves gaps by increasing destination index by two. The independently derived answer remains option 1.

After t valid copies, n=N-1-2t and i=t under alternative 1. The next copy is legal exactly while N-1-2t>=0, giving ceil(N/2) writes. The guard precedes the read. Alternative 2 skips b[0], and alternative 3 skips every other destination position. The printed function syntax is legacy integer pseudocode, not a fully declared C17 interface; the adaptation correctly discloses that distinction.

### Exact teaching-visual recommendation

The original question contains code, not a graph or circuit. An additional schematic is pedagogical rather than a required reproduction of an omitted original image. Use an actual two-array copy trace with the source and destination indices shown on the same step:

- Odd case: N=7, a=[10,20,30,40,50,60,70]. States `(n,i)` are `(6,0),(4,1),(2,2),(0,3),(-2,4)`; the final state takes the guard and performs no read. Destination b=[70,50,30,10].
- Even case: N=6, a=[10,20,30,40,50,60]. States `(5,0),(3,1),(1,2),(-1,3)`; b=[60,40,20].
- Show negative-index guard as a stop state, not as a source-array cell. Show the call stack and that unwinding performs no additional assignments. Do not draw spurious destination writes during returns.
- Optional counterexample selector should faithfully show option 4's same source stride of two and destination positions 1,3,5,7; it must not show source positions decreasing by one.

## PhD CE 1405, Q9, PDF page 3

- Repository path: `Exams/Phd/CE/1405/Q707A-phd1405-[www.konkur.in].pdf`.
- Local original: `C:/Users/bheydari/Desktop/Phd-Exam-CSE/Exams/Phd/CE/1405/Q707A-phd1405-[www.konkur.in].pdf`.
- SHA256, local and pinned blob: `34d7e4f8f1d347be2ede1be4ff027efc2e17680c3aedf633a13857f27955b75a`.
- Full-page render: `Phd_CE_1405_Q9.png`; decisive 5x base-case crop: `base-enlarged.png`.

**Correction to this research report.** My initial strict-`<1` transcription from the full-page render was wrong. The root reviewer produced the enlarged crop, which I then visually inspected: the original unmistakably prints `length(A) <= 1`. The prior recommendation to change the existing chapter base case and the associated 15-call claim are withdrawn. The existing chapter's base-case translation is correct.

The source stipulates distinct elements. Its code is:

```text
SplitSort(A):
  if length(A)<=1 then return A
  let m=median(A)
  L={x in A | x<m}, R={x in A | x>m}
  return concatenate(SplitSort(R), [m], SplitSort(L))
```

Original alternatives, in order:

1. Descending first, then m, then ascending.
2. Approximately random.
3. Ascending.
4. Descending.

**Base-case fidelity confirmed after enlarged inspection:** the source and the existing p_functions translation both return arrays of length at most one immediately. Preserve this condition. A singleton does not call empty children in the printed algorithm.

The independently derived answer remains option 4. Induct on length. Empty and singleton arrays are decreasing. For an array with at least two elements, both recursive inputs are strictly smaller and their decreasing returns contain respectively only elements greater than m and less than m. Their concatenation in R,m,L order is decreasing. The median balances recursive sizes but the return-block order determines direction. No official-key provenance should be inferred.

### Exact teaching-visual recommendation

The original supplies pseudocode, not a graph or diagram. Add a genuine partition-and-return tree, using an odd-length example to avoid an unstated even-length median convention:

- Input A=[7,2,5,1,6,3,4], median 4.
- R=[7,5,6], median 6; its greater child [7], smaller child [5]. Return [7,6,5].
- L=[2,1,3], median 2; its greater child [3], smaller child [1]. Return [3,2,1].
- Final return [7,6,5,4,3,2,1].
- Under the original `<=1` base case, this example has 7 calls and maximum simultaneously live frame count 3. Each singleton returns directly. The prior strict-`<1` claim and its 15-call/depth-4 trace were based on a rejected transcription and must not be used.
- Reveal greater and smaller recursive results separately, then show the exact R,m,L concatenation. A generic sorting bar animation cannot establish the actual return-order invariant or preserve the continuation context.

## Scope

Both are authentic bridge revisits already taught in other chapters, not newly discovered unique questions about lexical scope or pointer lifetimes. They are useful here only for call-parameter evolution, guard-before-access, recursive return contracts, and continuations. Existing disclosure of that limitation should remain.
