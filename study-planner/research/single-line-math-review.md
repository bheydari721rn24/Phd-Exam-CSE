# Complete-equation layout review

The student's October 5 correction concerns equations splitting across lines. This revision removes automatic equation fragmentation from both the chapter renderer and the shared browser layout. STIX Two Math remains the mathematical font. Prose and code fonts are unchanged.

## Corrected behavior

- Each complete equation occupies one horizontal line, including on narrow screens. A long equation can be scrolled horizontally inside its own container; it does not widen the page.
- Real rows inside matrices, piecewise definitions, and intentionally separate equations are preserved. They are mathematical structure, not artificial line wrapping.
- 84 generated wrapping tables were removed from the three affected chapter documents. Nine additional generated wraps were removed from counting-animation checkpoints. Future chapter rendering no longer creates these wrapping tables.
- Plain-text display formulas also retain a single line on mobile.

## Observed checks

The actual browser audit covers 34 chapters at widths of 1280 and 390 pixels. All 20,879 MathML instances preserve their original mathematical text, script/fraction/radical nodes, and genuine matrix/case tables. All 1,999 question entries are retained. No generated wrapping tables or semantic-wrap attributes remain in the displayed chapters; mathematical fonts loaded, horizontal scrolling worked, and the document did not overflow either viewport. Print checks preserve equation structure.

Two unrelated existing laboratory initialization errors in g_gates-lab.js and l_vectors-lab.js were reproduced using the exact pre-edit source commit. They are recorded separately in the browser report; this typography revision introduces no new runtime error. This is a layout audit, not a claim that the complete library has no other defects.

Evidence: single-line-math-audit.json and single-line-math-browser.json. The chapter gate remains awaiting_user_approval for d_pigeonhole; no new chapter was started or promoted.
