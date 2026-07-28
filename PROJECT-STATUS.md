# Project Status and Next Steps

**Running status file — update this at the end of each working session.**
Last updated: 2026-07-27 (end of Round 3).

Per-round markup plans live alongside this file and are the archive, not the status:
`revision-notes.md` (Round 1), `revision-notes-round2.md` (Round 2),
`revision-notes-round3.md` (Round 3 — includes the parsed markup, 11 decisions, and
the execution plan).

---

## 0. The book's thesis (the lens for every decision)

> Controls provides tools to model and analyze LTI dynamical systems. These tools can
> be used to analyze simple series and parallel circuits made of ideal components.
> Understanding of these simple circuits (and their extension) provides clear insights
> into advanced topics such as filters, antennas, transmission lines, and other
> content on the extra exam.

The Part III / Part IV boundary now encodes this directly: Part III is the simple
circuits, Part IV is what they explain.

---

## 1. Where things stand

- **21 chapters + 3 appendices, five parts, 140 pages.**
- **Build is clean:** 0 undefined references, 0 overfull boxes > 20 pt.
- **19 commits ahead of `origin/main`. Nothing has been pushed.** Decide whether to
  push before continuing.
- Build with `make book`; regenerate figures with `make figures` (or run individual
  scripts in `figures/src/`); `make all` also builds the standalone study-guide card.

### Current structure

| Part | Chapters |
|---|---|
| **I — Exam-Ready Reference** | 1 Study Guide |
| **II — Mathematical and Control-Theory Foundations** | 2 Complex Numbers & Phasors · 3 Modeling LTI Systems · 4 Frequency Response, Bode, s-Plane · 5 Feedback · 6 Higher-Order Systems |
| **III — Circuit Models** | 7 Circuit Modeling · 8 Series & Parallel Networks · 9 AC Steady State · 10 One Circuit, Four Views · 11 RC · 12 RL · 13 Series RLC · 14 Parallel RLC |
| **IV — Applying the Circuit Models** | 15 Filters, Matching, Transformers · 16 Transmission Lines · 17 Active Circuits · 18 Measurement |
| **V — Practice and Study** | 19 Worked Examples & Exam Map · 20 Anchored Practice · 21 Cross-Chapter Problems |
| **Appendices** | A Formula Index · B Units & Prefixes · C Glossary |

Labels are stable across renumbering — **always `\cref`, never hard-code a number.**
Key labels: `ch:studyguide` `ch:complex` `ch:linsys` `ch:splane`/`ch:bode`
`ch:feedback` `ch:highorder` `ch:foundations` `ch:resistive` `ch:ac` `ch:fourviews`
`ch:rc` `ch:rl` `ch:rlc` `ch:rlcpar` `ch:filters` `ch:lines` `ch:active`
`ch:measurement` `ch:exammap` `ch:practice` `ch:crossproblems` `app:formulas`
`app:units` `app:glossary`. Section labels worth knowing: `sec:decibels`
`sec:asymptotes` `sec:rc-freq` `sec:lc-lowpass` `sec:stubs` `sec:probe` `sec:gbw`
`sec:beta-resistors` `sec:mixers` `sec:factoring` `sec:cascadeadd` `sec:threepoles`
`sec:poleplacement` `sec:groupdelay`.

### Conventions in force

- **Notation:** `φ` = a signal's phase (phasor angle); `θ` = generic polar form and
  impedance angle; `j` upright (ISO 80000-2). Double-duty letters are flagged in the
  Study Guide: `Q` (quality factor / reactive power), `β` (feedback fraction / phase
  constant), `L` (inductance / loop gain).
- **Worked examples:** in-line ones use the `workedbox` callout; each chapter's main
  one is a numbered `\section{Worked Example}` **and must close the chapter**.
- **Callout boxes** (all eight are used): `controlsbox` `physicalbox` `energybox`
  `unitsbox` `exambox` `mistakebox` `advancedbox` `workedbox`.
- **Every schematic labels its input and output.** Every figure has a `\label`.
- **Derive, don't assert.** Where a result is reused from an earlier chapter, cite it
  rather than re-deriving it.
- Figures: data plots are Python/matplotlib in `figures/src/` (shared `_style.py`
  palette), committed as PDFs; schematics are circuitikz inline. **Always render new
  or changed figures to PNG and check for overlapping text before committing.**

---

## 2. What Round 3 did (this session)

Driven by Alex's markup of `main 3.pdf` (front matter through Ch 12 read in detail).

**Structure.** Ch 3 retitled *Modeling LTI Systems*; new **Ch 5 Feedback** (generic,
state-space + frequency-domain); RLC **split** into Series + Parallel; filters chapter
became design-only with the RC/LC derivations moved back into the RC and Series-RLC
chapters; new `workedbox`; new **§4.1 Decibels** and Bode asymptote derivation;
C/L combining rules added; parallel-impedance section added.

**Later chapters — the big push, per Alex's instruction to leverage earlier
fundamentals.** Ch 16 (lines) now derives telegrapher's → wave equation *by the same
substitution as the Series RLC chapter*, plus `Z₀`, `Γ` from boundary conditions, SWR,
and quarter-wave `Z_t`; a new **Stubs** section shows a stub *is* the series/parallel
resonator; the antenna gets real values and `Q = 5.7 → BW = 2.5 MHz`. Ch 17 (active)
connects `β = R_g/(R_f+R_g)` so the abstract feedback fraction becomes the textbook
gain formula, derives Sallen–Key `Q`, and adds **Mixers** as the one deliberate break
from linearity. Ch 18 (measurement) was rebuilt from a 47-line stub: meter loading
from Thévenin, **scope probe as pole–zero cancellation**, ground lead as an accidental
145 MHz resonator, analyzer as the Smith locus.

**New Ch 6 Higher-Order Systems.** Thesis: higher order needs *no new machinery*.
Contains the factoring theorem, derives `−20n` dB/decade (previously asserted 4×),
derives why three poles oscillate (`K=8`, `ω=√3ω₀`), pure delay, Butterworth pole
placement with the order-2…6 **section-`Q` table**, zeros at higher order, and
**group delay** (used for Bessel filters but previously never defined).

**Part split.** The old Part III held 12 chapters / 57 % of the book. Split into
*Circuit Models* and *Applying the Circuit Models*; cross-chapter problems promoted
from an appendix to Ch 21.

**Consistency.** Two review passes fixed: Ch 17 crediting feedback to the wrong
chapter and re-deriving Ch 5 four times; Barkhausen stated wrongly in the formula
index; `energybox` defined-but-never-used; a duplicated exam box; missing chapter
openers; worked-example levels and ordering; unlabeled schematics; `\wzero` vs
`\omega_0`; 12 dead macros; unlabeled appendices. Formula index gained a **"Derived
in" column**.

**Verification.** Ch 20's pool citations were checked against the real pool:
**all 16 identifiers exist and all 15 answer letters are correct.**

---

## 3. Exam coverage — measured, and now stated honestly in the preface

Against the real 2024–2028 pool (`references/HamExam.org Extra Question Pool.pdf`,
which **does** carry question IDs and answer letters — an earlier note claiming
otherwise was wrong):

- **COVERED (8 groups):** E5A, E5B, E5C, E7C, E7G, E9E, E9F, E9G
- **PARTIAL (13)**, six of them thin: E4A, E4B, E4D, E5D, E6D, E7B, E7D, E7E, E7F,
  E7H, E8A, E9A, E9D
- **ABSENT (29)**

That is **21 of 50 generously, ~15 strictly. Passing requires 37/50**, so this book
alone is not sufficient. The preface now says so explicitly and names what is out of
scope. "How to Use" no longer claims Part I "should be enough."

---

## 4. Recommended next steps, in priority order

### A. Start here tomorrow — the General-exam check

Paste this prompt verbatim:

> ### BEGIN
> Next, please examine "HamExam.org General Question Pool" in the references folder.
> While this book is intended for the Extra exam, I want to confirm that it covers all
> of the background material required for the circuits questions in the General exam.
> While I did pass the General exam, that was mainly by memory. I want to go back and
> understand the material. I do not want to explicitly mention General exam questions
> in the book or any of its appendices.
> ### END

Note: `references/HamExam.org General Question Pool.pdf` is already present, as is
`General Class Pool and Syllabus 2023-2027 ... Feb 4 2026.pdf`. The General pool runs
on a **2023–2027** cycle (different from Extra's 2024–2028). The constraint is
explicit: **find and fill background gaps, but never mention the General exam in the
book or appendices** — any additions must read as ordinary prerequisite material.

### B. Highest-value content gaps (all in-scope, all reachable from existing tools)

1. **Receiver noise and dynamic range (E4C/E4D).** The most defensible addition and
   the most embarrassing omission: Ch 17 already derives image response and
   third-order products from the mixer algebra — only the *metrics* are missing.
   Needs `kTB`, the −174 dBm/Hz floor, noise figure, cascaded NF (Friis), MDS, 1 dB
   compression, IP3 with its 3:1 slope, blocking/IMD dynamic range, desensitization.
   All arithmetic on the existing decibel machinery. Two exam groups.
2. **Sampling and DSP (E7F, plus E4A01/A06, E8A).** The sampling theorem appears
   **nowhere** in the book, yet Ch 15 mentions anti-aliasing paths and asserts FIR
   linear phase. Needs Nyquist, aliasing as spectral folding, ≈6 dB/bit, decimation,
   FIR/IIR. Pairs naturally with Ch 6's new group-delay material.
3. **Phase-locked loops (E7H).** A control loop in radio clothing — the strongest
   thematic fit of anything missing, and Ch 5/Ch 6 already supply every tool.
4. **Rebuild Ch 19 (Worked Examples).** Its four examples have zero cross-references,
   zero poles, and component values unrelated to the book's running examples — a
   direct contradiction of the thesis in the chapter meant to demonstrate it.
   Either make it a pure map (Ch 21 now carries the real cross-chapter practice) or
   rebuild the examples around the book's running values.
5. **Cheap filter/matching wins (E7C).** Pi-L network, shape factor, crystal-lattice
   and helical filters — 2–3 lines each in an existing table.
6. **Antenna gain and patterns (E9A/E9B).** The book models an antenna's feed-point
   impedance and stops; ERP/EIRP, dBi/dBd, and beamwidth are two more groups.
7. **S-parameters and the VNA (E4B).** `S₁₁` *is* `Γ`, already derived; `S₂₁` is
   forward gain. Half a page connecting two things the book owns.
8. **Smith chart pool vocabulary (E9G).** Attach the pool's terms (reactance axis,
   resistance axis, prime center, wavelength scales) to `fig:smith-basic`. Trivial.

### C. Smaller cleanups still outstanding

- **Ch 10 (Four Views) and Ch 19 have no callout boxes and no figures.** Ch 10 is
  defensible as a 2-page hinge chapter; Ch 19 is not.
- **`exambox` missing from Ch 7, 11, 13, 15, 16** — including the two most exam-dense
  chapters (filters, lines).
- **Chs 11–14 have zero `workedbox`** — the in-line example device is absent exactly
  where step-by-step modelling happens.
- **Figure provenance:** 26 of 27 computed figures don't say how they were generated.
  Consider a one-line "computed from…" clause in each caption, or one note in the
  front matter.
- **Ch 20 mixes two structural registers** — numbered sections with 12 starred
  per-question subsections, then abandons the pattern halfway.
- **Ch 17 §Power Supplies** is 7 lines and the least-integrated passage in Parts
  III–V; a rectifier + filter cap is an RC discharge and a bleeder is a divider.
- **Appendix B** still restates Ch 7's units material (now cross-referenced, not
  merged — revisit if it bothers you).

### D. Still awaiting Alex's judgment

- **Preface personal paragraph** — currently names the University of Notre Dame and
  says the book was drafted with ChatGPT and developed with Claude Code. Tune the
  candor as you like.
- **Notation carets (S7 / C-p4 from Round 2)** — the ω/f caret markup in the markup
  was ambiguous; notation was left as-is.
- **Whether to push** the 19 local commits.

---

## 5. How to resume

```bash
cd /Users/adowling/GitHub/radio-extra-book
make book          # -> main.pdf and output/Circuit_Theory_for_the_Amateur_Extra_Exam.pdf
```

Health check that should stay at zero:

```bash
grep -c undefined /dev/stdin < <(make book 2>&1)
```

Before committing figure changes, render and eyeball them:

```bash
pdftoppm -r 110 -png figures/<name>.pdf /tmp/chk && open /tmp/chk-1.png
```
