# Round 7 open questions

This record preserves decisions that materially changed scope, meaning, or
organization. All four material questions are now resolved. Routine unreadable
words, local wording, and figure-layout details remain marked `[?]` in
`revision-notes-round7.md`; they do not need a decision before a conservative
editing pass.

## Resolved OQ-1 — Preface: process-control framing

- **Location:** annotated PDF p. 2 (printed p. i), third paragraph; `R7-002`.
- **Markup:** overlapping blue/red/green notes include “and be open to [models?]
  e.g. [github.io?] optimization,” “we focus on,” and “frequency domain.”
- **Resolution (2026-09-05):** name the course and link it as
  \(<https://ndcbe.github.io/controls>\). Retain the contrast between the course’s
  state-space/nonlinear/optimization focus and the natural frequency-domain view of
  AC circuits.

## Resolved OQ-2 — Preface: scope-list bracket “Extra exam!”

- **Location:** annotated PDF p. 2 (printed p. i), lower long list; `R7-004`.
- **Markup:** a violet bracket around the scope list and the note “Extra exam!”
- **Resolution (2026-09-05):** call the reference point “the Extra exam syllabus.”
  The Preface now says that the book develops the circuit-theory portion of that
  syllabus and leaves the rest alone.

## Resolved OQ-3 — Chapter 6: destination for filters/delay material

- **Location:** annotated PDF pp. 56–57 (book pp. 40–41), §§6.6–6.9; `R7-043`,
  `R7-044`.
- **Markup:** “Then revisit this for (radio) filters,” “move to later chapters
  that focus on filters,” “move to filter radio specific [section?],” and “This
  is great. Move it to later [chapter?].”
- **Resolution (2026-09-05):** split the material. Chapter 6 now develops generic
  higher-order/feedback dynamics, pure delay, and the infinite-mode limit. Chapter
  15 introduces filter goals before deriving filter-family pole placement and group
  delay as filter-design trade-offs.

## Resolved OQ-4 — Chapter 8: voltage-divider redesign

- **Location:** annotated PDF p. 67 (book p. 51), §8.4 / Figure 8.1; `R7-050`.
- **Markup:** “I do not like this and want to [??]” with arrows to the divider
  schematic and equations; the desired replacement is not readable.
- **Resolution (2026-09-05):** retain the basic unloaded divider, but redraw it
  around the grounded reference node and a clearly labeled output node. The text
  now makes the unloaded assumption explicit and directs the reader to the later
  Thévenin worked example for the loaded-divider case. This preserves the intended
  early derivation without prematurely introducing a load model.
