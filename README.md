# Circuit Theory for the Amateur Extra Exam

This directory contains a polished LaTeX mini-textbook converted from the
authoritative Word draft:

`references/Ham_Extra_Circuits_Study_Guide_First_Draft.docx`

## Prerequisites

- A LaTeX distribution with `pdflatex` and `latexmk`
- Common packages: `amsmath`, `siunitx`, `booktabs`, `tabularx`, `tcolorbox`,
  `tikz`, `circuitikz`, `pgfplots`, `hyperref`, and `cleveref`
- Poppler tools such as `pdfinfo` and `pdftoppm` for render verification

## Build

```bash
make book
make cheat-sheet
make all
make clean
```

The compiled PDFs are copied to `output/`.

## Project Structure

- `main.tex`: textbook entry point
- `preamble.tex`: document style, packages, page geometry, and callout boxes
- `macros.tex`: recurring notation
- `frontmatter/`: title, preface, exam-scope note, and notation
- `chapters/`: textbook chapters
- `appendices/`: formula index, units, complex-number refresher, glossary, and solutions
- `cheat_sheet.tex`: standalone printable two-column formula sheet
- `references.bib`: source and supporting-reference metadata

## Manuscript Mapping

The Word section "Cheat Sheet Summary" became Chapter 1 and the standalone
cheat sheet. "Why the units work" became Chapters 2 and 3. "One circuit, four
modeling approaches" became Chapter 6 and also the organizing pattern for the
RC, RL, and RLC chapters. "First-order transients" became Chapters 8 and 9.
"Phasors, impedance, and polar form" became Chapter 4. "Resonance, Q, and
bandwidth" became Chapter 10. "Bode plots and frequency response" became
Chapter 5. "Decibels and gain" was integrated into Chapters 5, 11, and the
appendices. "Transmission lines and SWR" became Chapter 13. "Exam-focused
reminders" and the minimal formula sheet became Chapter 15 and Appendix A.

## Substantive Revisions

- Standardized notation around \(j\), RMS phasors, passive sign convention,
  \(\omega=2\pi f\), signed impedance, and reactance magnitudes.
- Added dimensional-analysis checks using `siunitx` conventions.
- Expanded the manuscript with original material on dividers, Thevenin/Norton
  equivalents, filters, impedance matching, transformers, active circuits,
  transmission-line quantities, Smith chart interpretation, measurement, and
  worked examples.
- Added original TikZ, circuitikz, and pgfplots figures.
- Added controls and energy sidebars while keeping exam-scope boundaries clear.

## Source-Material Currency Limitations

The Word manuscript is the primary source. The PDFs in `references/` were
used only for topic and terminology checks. Some supporting study guides
correspond to older question pools, so this book does not claim that any
specific question identifier is current. Final exam preparation should be
checked against the official current Amateur Extra question pool and FCC rules.
