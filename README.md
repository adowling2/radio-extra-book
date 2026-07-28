# Circuit Theory for the Amateur Extra Exam

*A Dynamical Systems and Control Perspective for Engineers* — Alexander Dowling (KE9FZD)

A LaTeX mini-textbook that teaches the circuit theory behind the Amateur Extra exam
from a control-theory point of view: controls supplies tools for modeling LTI
dynamical systems, those tools describe simple circuits made of ideal components, and
understanding those simple circuits is what makes filters, antennas, transmission
lines, and the rest of the exam's circuit content intelligible rather than arbitrary.

## 👉 Start here

**[`PROJECT-STATUS.md`](PROJECT-STATUS.md) is the running status file** — current
structure, what the last session did, prioritized next steps, and open decisions.
Read it before doing anything else.

Per-round markup plans are the archive: `revision-notes.md` (Round 1),
`revision-notes-round2.md`, `revision-notes-round3.md`.

## Prerequisites

- A LaTeX distribution with `pdflatex` and `latexmk`
- Packages: `amsmath`, `siunitx`, `booktabs`, `tabularx`, `longtable`, `tcolorbox`,
  `tikz`, `circuitikz`, `pgfplots`, `hyperref`, `cleveref`
- Python 3 with `numpy`, `matplotlib`, `scipy` (for the generated figures)
- Poppler tools (`pdfinfo`, `pdftoppm`, `pdftotext`) for render verification

## Build

```bash
make book          # the textbook
make figures       # regenerate the Python figures
make cheat-sheet   # standalone printable formula card
make all
make clean
```

Compiled PDFs are copied to `output/`. A healthy build reports **0 undefined
references and 0 overfull boxes above 20 pt**.

## Project structure

- `main.tex` — entry point; defines the five parts and the chapter order
- `preamble.tex` — style, geometry, and the eight colour-coded callout boxes
- `macros.tex` — the few pervasive notation macros (deliberately short)
- `frontmatter/` — title, preface (including the scope statement), how-to-use, notation
- `chapters/` — 21 chapters, filenames numbered to match chapter numbers
- `appendices/` — formula index (with a "Derived in" column), units, glossary
- `figures/src/*.py` — figure sources; generated PDFs are committed to `figures/`
- `cheat_sheet.tex` — standalone two-column card
- `references/` — question pools and reference texts (**gitignored**, copyrighted)

## Conventions

- **Cross-references:** always `\cref`/`\Cref`. Never hard-code a chapter, section, or
  figure number — labels are stable across the renumbering that happens every round.
- **Notation:** `φ` = a signal's phase; `θ` = generic polar form and impedance angle;
  `j` upright per ISO 80000-2. Double-duty letters (`Q`, `β`, `L`) are flagged in the
  Study Guide.
- **Worked examples:** in-line ones use the `workedbox` callout; each chapter's main
  one is a numbered section that closes the chapter.
- **Every schematic labels its input and output.** Every figure has a `\label`.
- **Derive, don't assert** — and where an earlier chapter already established a result,
  cite it instead of re-deriving it.
- Data plots are Python/matplotlib (shared palette in `figures/src/_style.py`);
  schematics are inline circuitikz. **Render any new or changed figure to PNG and check
  for overlapping text before committing.**

## Scope

This book covers the **circuit-theory** portion of the Extra syllabus. Measured
against the current pool it reaches 8 of the 50 exam groups well and 13 partially;
passing requires 37 of 50. It deliberately omits rules and regulations, operating
practice, propagation, safety, digital protocols, and device physics. The preface
states this explicitly — see `PROJECT-STATUS.md` §3 for the group-by-group map.

It has also been checked against the **General** (Element 3) pool, whose 236
circuit questions distil to 157 concepts: the electrical-principles core is covered
by derivation, and what remains missing is the same by-design list above. So the
book is usable as the circuits foundation a General licensee needs before Extra,
which is what it was written for — but it never mentions the General exam.

Practice material is anchored to the 2024–2028 Element 4 pool. The question
identifiers and answer letters cited in the Anchored Practice chapter have been
verified against `references/HamExam.org Extra Question Pool.pdf`, but pool wording
changes each cycle, so final preparation should be checked against the official
current pool and FCC rules.

## Provenance

This is an independent educational study guide, not affiliated with the ARRL, NCVEC,
or the FCC. It began as the author's own Word draft (prepared with the aid of ChatGPT)
and was developed, corrected, and typeset iteratively with Claude Code, with the
author steering the pedagogy and critiquing the text. The reference texts in
`references/` were used only for topic-coverage and terminology checks; their prose,
questions, answer choices, and figures were not copied.
