# Literature audit, 2026-09-09

## Purpose and scope

This audit checked the book's factual claims, equation-derived assertions, worked
results, and generated figures against a separate collection of 16 textbooks covering
RF and microwave circuits, measurement, receivers, frequency synthesis, analog
baseband design, circuit simulation, and control theory. The goal was not to broaden
the book into a general RF reference. It was to make the existing exam-centered
explanations reliable, expose their assumptions, and point a reader to deeper
treatment.

The audit covered the preface, Chapters 1--26, all appendices, all inline circuit
schematics affected by technical claims, and every Python-generated figure. Claims
were considered at the smallest practical unit: one physical assertion, mathematical
identity, numerical result, or plotted relationship at a time.

## Copyright and privacy boundary

The literature corpus remained outside this Git repository throughout the work. No
source PDF, page image, extracted passage, figure, table, or source-derived working
ledger was copied into the repository. Audit notes used paraphrases rather than source
prose and remained beside the private corpus.

The only corpus-derived information admitted here is conventional bibliographic
metadata and pinpoint page locators. Manuscript corrections and explanations are
independently worded, and the book's equations and figures remain its own derivations
and implementations. Citations are navigation aids and evidence, not permission to
reproduce a source.

## Method

The work used four concurrent audit lanes, including the coordinating reviewer:

1. front matter, Chapter 1, Chapters 24--26, appendices, and cross-book reconciliation;
2. Chapters 2--10, mathematical foundations and basic circuit models;
3. Chapters 11--17, reactive circuits, RF networks, transmission lines, and active
   circuits;
4. Chapters 18--23, DSP, noise, measurement, antennas, receivers, devices, and
   regulation.

Each lane first inventoried claims and equations, located the strongest directly
supporting treatment in the corpus, and recorded the printed page number. Printed page
numbers were preferred to PDF viewer indices. A citation was added only when the cited
page directly supports the nearby statement; general chapter citations and guessed
locators were rejected.

Every item received one of four practical outcomes:

- supported as written;
- supported after stating assumptions or narrowing the claim;
- corrected because the derivation, schematic, or prose was wrong; or
- left without an external citation when the corpus lacked a suitable pinpoint.

The last category was not treated as permission to invent a citation. Where possible,
the book instead derives the result or labels an example as illustrative.

## Simulation and figure verification

All 36 Python figure generators were executed in an isolated copy before repository
reconciliation. Review checked the governing equations, parameters, annotations,
limits, and plotted conclusions rather than relying on byte or raster equality. That
distinction matters because fonts, PDF bounding boxes, and antialiasing can change
without changing numerical content.

Four figure sources required corrections: normalized phasor time labels, first-order
settling annotation, the interpretation of fixed-real-part feedback poles, and the
series-RLC value marked at resonance. Their PDFs and provenance records were then
regenerated through the repository figure workflow.

## Reconciliation result

The audit added 16 books to `references.bib` and 175 page-specific technical citation
commands to the manuscript. Corrections focused on consequential overstatements rather
than adding tangential literature. Examples include:

- transfer-function poles versus state eigenvalues for nonminimal realizations;
- the response for which `BW = f_0/Q` is exact;
- fixed-real-part feedback pole motion;
- frequency-dependent ferrite and transmission-line loss models;
- balanced-mixer, op-amp, and oscillator idealizations;
- ideal quantization SNR versus realizable ADC dynamic range;
- the matched 290 K convention behind -174 dBm/Hz;
- preserving protective earth while addressing ground loops;
- VNA power-wave ratios and their reference impedances; and
- the efficiency assumptions behind fixed-aperture antenna scaling.

The Chapter 8 Norton schematic was also corrected so the ideal current source is not
shorted by a wire.

## Deliberate source gaps

The corpus did not supply a clean pinpoint for every statement. Remaining categories
include the current SI ampere definition; a general Thevenin/Norton theorem statement;
manufacturer-specific cable values and antenna dimensions; selected probe, counter,
and transmitter bench procedures; and some FIR/IIR, Carson-rule, device, rectifier,
regulator, and antenna-modeling details. These claims were qualified or kept as local
derivations where appropriate, but no placeholder citation was added.

## Validation and review

The final build contains 234 pages, 26 chapters, 36 generated figures, 88 section
labels, and 65 glossary entries. `./scripts/check.sh` reports `ALL CHECKS PASSED`: no
undefined citations or references, no multiply defined or orphaned labels, no dangling
references, no overfull boxes above the project threshold, and a passing figure source,
provenance, and grayscale audit.

Representative pages from every major chapter range, every changed generated figure,
the glossary, and the complete bibliography were rendered to images and inspected for
clipping, overlap, unreadable glyphs, and citation-layout problems.

For line-by-line review, run:

```bash
make audit-diff
```

This compares immutable pre-audit commit `4f4100a` with audited manuscript commit
`660dda4` and writes `output/pdf/literature-audit-latexdiff.pdf`. Later documentation
changes are intentionally excluded from that comparison. Circuitikz environments are
treated as atomic pictures so markup cannot split a drawing command; inspect the new
Norton schematic directly where that correction is discussed. The review copy labels
the two revisions and uses the standard latexdiff convention: blue underlining for
added text and red strikeout for deleted text.
