# English chapter math typography audit

Date: 2026-09-30. This is a presentation correction to the four existing English discrete-mathematics chapters; it does not change their mathematical claims or approval states.

## Issue and correction

Raw Unicode small index glyphs were mixed into normal text. Some browsers used a different fallback face or made the indices too small. Summation limits in the induction chapter were placed with ordinary HTML `<sub>/<sup>` after a text sigma; this positioned limits beside the operator. One intermediate renderer also inserted thin spaces into generated `class` attributes, silently disabling the intended index style.

- `research/math_typography.py` now converts raw Unicode indices in rendered lesson text into semantic `<sub>/<sup>` elements wrapped with a consistent math-font class. It leaves SVG, MathML, code, style, and script content intact.
- The induction builder emits MathML under/over limits for all 19 indexed summation/conjunction operators. The diagrams use explicit SVG baseline shifts for indices.
- `chapter.en.css` defines the bundled STIX Two Math face for all indices and adds mobile wrapping for long displayed formulas. A three-line arithmetic-sum derivation preserves equation order at narrow widths.
- `research/check_site_en.py` now detects unconverted raw indices or malformed class attributes in all four published chapter pages.

## Review evidence

All four manuscript builders and their mathematical/structure verifiers passed. Local Edge at a 390-pixel mobile width reported document scroll width 390, loaded fonts, and no internal formula-block overflow in logic, sets, proof, or induction. The index passages of all four chapters were captured and visually inspected. A4 print produced 21, 20, 18, and 20 nonblank pages respectively, with no replacement characters in extracted text. The induction chapter remains a review draft awaiting explicit student approval.
