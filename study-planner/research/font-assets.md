# English study typography

The plan and all English chapters use the same locally hosted font files. This avoids dependence on fonts installed on the student's machine and keeps the appearance stable when the site is opened on another device.

| Role | Font | Local asset | Source and license |
| --- | --- | --- | --- |
| Running text and controls | Source Sans 3, Latin variable, weights 300–700 | `dist/fonts/source-sans-3-latin.woff2` | [Google Fonts distribution](https://fonts.google.com/specimen/Source+Sans+3); SIL Open Font License in `dist/fonts/OFL-SourceSans3.txt` |
| Headings | Newsreader, Latin variable, weights 300–600 | `dist/fonts/newsreader-latin.woff2` | [Production Type project](https://github.com/productiontype/Newsreader); SIL Open Font License in `dist/fonts/OFL-Newsreader.txt` |
| Mathematical symbols and displayed formulas | STIX Two Math, weight 400 | `dist/fonts/stix-two-math.woff2` | [STIX project](https://www.stixfonts.org/); SIL Open Font License in `dist/fonts/OFL-STIXTwoMath.txt` |

The CSS uses the mathematical font as a fallback for symbols that are absent from the Latin text subset. The displayed formulas explicitly use STIX Two Math. A system serif/sans-serif fallback remains for environments that disable web fonts. Font loading, mobile width, and A4 rendering are part of the chapter QA.
