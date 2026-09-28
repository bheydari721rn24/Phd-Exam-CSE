# Font QA — d_logic

The user-provided screenshot from 2026-09-28 showed a mixed Persian font in the opening paragraph of §2.1. The prior print PDF reproduced it: some Arabic-script spans used `SegoeUI` (106 characters) and one mathematical result line used `TimesNewRomanPSMT` (13 characters), alongside `BNazanin`.

## Diagnosis and repair

- Optional combining marks in the Persian prose caused browser print fallback across portions of affected lines. The visible wording remains understandable after removing optional marks U+064B–U+065F; the replacement was applied throughout this chapter.
- Persian digits inside `.math` spans had fallen back to `SegoeUI`. `chapter.css` now places `Persian Nazanin` immediately after `Cambria Math` in the math font stack.
- A Persian phrase was embedded in a left-to-right `.math-block`, which caused a Times New Roman fallback. The result now uses a symbolic condition instead.

## Verification

- Reprinted the full local chapter with Microsoft Edge after the edit: 32 nonempty A4 pages.
- Parsed the printed PDF's text spans with PyMuPDF: all 22,276 extracted Arabic-script characters were associated with `BNazanin`; zero were associated with another font. The PDF contained zero U+FFFD replacement characters.
- Visually inspected the §2.1 page and the corrected Boolean-function result line. The user's reported mixed-font line is now uniform.
- This verifies the local Edge print. A reader whose device lacks a locally installed B Nazanin font may still see a fallback; the font file is not redistributed in the public repository.
