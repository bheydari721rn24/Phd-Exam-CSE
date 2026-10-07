# Mathematical delimiter repair — 7 October 2026

## Reproduced defect

The visible fault was reproduced in the expectation chapter's occupancy
section. The source TeX contained the closing parentheses, but the renderer
produced `msup(mo(')'), m)` instead of
`msup(mrow('(', expression, ')'), m)`. That separated the closing glyph from
the expression and allowed the opening glyph to stretch to the height of an
adjacent summation. The resulting asymmetry made closing parentheses difficult
to see. The saved before/after screenshots show the actual browser result.

## Repair

- Normalize matched MathML fences into a complete row; move a script on a
  closing glyph to the complete fenced base. Scope nested fences independently.
- Apply this repair to static lesson, problem, review and animation MathML.
  The scan processed 31,951 instances across published HTML and model data;
  it corrected 785 bare closing-delimiter script bases, including 727 in the
  41 chapter pages. Repeated checkpoint copies are included in these totals.
- Normalize future renderer output and reject unbalanced tokens before writing
  a new formula. Add the same normalization for dynamically inserted formulas.
- Preserve mathematical token order, all non-row token/attribute counts and
  all surrounding prose. Mathematical values and problem contents were not
  edited. Genuine cases rows and matrix structures remain present.
- Refresh the shared layout script URL to prevent cached older code.

The initial simple count scan flagged 132 mixed-parenthesis instances. These
were valid half-open intervals, not missing closing fences. The structural
audit allows those intervals and intentionally one-sided case-table braces;
it found no remaining unmatched ordinary delimiter tokens in published HTML.

## Verification

`delimiter-evidence/qa.json` records a passed real Edge audit of every chapter
at widths 1280 and 390 pixels. It checks 26,639 chapter MathML instances and
the 5,286 cached model instances separately. Both glyphs of every visible
paired row are measurable; matching pairs have equal heights within 2 pixels.
No remaining script has a bare closing delimiter as its base, the mathematical
font loads, and the document does not overflow either viewport.

The complete library retains 41 chapters and 2,593 problems. A comparison
with source commit `188b2be087fa37a99d2e5da8a3ad672629dfbd74` verifies every
formula's decoded text, attributes, non-row token counts and surrounding HTML;
the only allowed non-formula difference is the shared script cache version.
Model JSON values outside mathematical markup are identical.

Nine renderer cases cover nested parentheses, a fraction raised to a power,
a sum, expectation, half-open intervals, a matrix power and a set definition.
Five deliberately malformed examples are rejected. A dynamically inserted old
closing-glyph script is automatically corrected, repeated layout is idempotent,
and print-mode paired-fence geometry passes. Screenshots for the occupancy,
central-moment, fraction-power and mobile examples were visually inspected.

The approval gate remains `awaiting_user_approval` for `s_expectation`; this
repair neither promotes that draft nor starts another chapter. Publication is
recorded only after native saved-source and deployment verification.
