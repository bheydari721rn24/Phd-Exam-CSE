# Arrays and linked lists: arrow and label repair

The student rejected detached, oversized and irregular arrows and labels too close to boxes. This repair changes only the arrays chapter's diagram geometry and animation renderer. The 86 problems, 80 examination rules, mathematical statements and 113 checkpoint states remain unchanged.

## Drawing conventions

Every arrow records its source and target box, route points and boundary ports. Small arrowheads use fixed SVG user units rather than scaling with line thickness. Forward links are blue, backward links are amber, and cursor links are violet. Adjacent bidirectional links use separate lanes; longer returns use rounded orthogonal paths outside the nodes. Text and node rectangles move as one group. Cursor-label pills and null boxes have explicit padding. Matrix row and column links attach to their own node ports.

During animated movement, route endpoints follow the actual moving box boundaries. The route itself changes shape rather than translating away from the source. Reduced-motion settings disable this movement.

## Observed verification

The browser inspected all 20 models and 113 checkpoints and 497 editable-laboratory diagram frames. It measured arrow endpoints against source and destination rectangles, inside text padding (at least 8 horizontal and 6 vertical SVG units), and external label clearance (at least 14 units). No measured layout issues remained. Four samples during moving doubly linked nodes found no detached edges. Screenshots of splice, reversal, Floyd and orthogonal-matrix diagrams were visually reviewed.

All 466 independent laboratory numerical references still agree. Desktop, 390-pixel mobile, loaded fonts, controls, reduced motion, and all 113 print checkpoints passed. This is finite browser evidence, not a claim that every possible interpolation or future input is covered.

Evidence: `research/a_arrays-visual-browser-audit.json`. The chapter remains a review draft awaiting explicit student approval.
