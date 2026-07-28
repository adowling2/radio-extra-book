# Project Status and Next Steps

**Running status file — update this at the end of each working session.**
Last updated: 2026-07-28 (end of Round 4).

Per-round markup plans live alongside this file and are the archive, not the status:
`revision-notes.md` (Round 1), `revision-notes-round2.md` (Round 2),
`revision-notes-round3.md` (Round 3 — includes the parsed markup, 11 decisions, and
the execution plan). Round 4 had no markup file: it was driven by a front-to-back
read-through plus a coverage check against the General (Element 3) question pool,
and its findings are recorded in §2 below.

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

- **21 chapters + 3 appendices, five parts, 159 pages, 29 figures.**
- **Build is clean:** 0 undefined references, 0 overfull boxes > 20 pt, 0 orphan
  labels, 0 dangling references, 0 hard-coded cross-references.
- **Everything is pushed.** `main` and `origin/main` are identical. (An earlier
  version of this file claimed 19 unpushed commits; that was simply wrong.)
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
Chapter labels: `ch:studyguide` `ch:complex` `ch:linsys` `ch:splane` `ch:feedback`
`ch:highorder` `ch:foundations` `ch:resistive` `ch:ac` `ch:fourviews` `ch:rc` `ch:rl`
`ch:rlc` `ch:rlcpar` `ch:filters` `ch:lines` `ch:active` `ch:measurement`
`ch:exammap` `ch:practice` `ch:crossproblems` `app:formulas` `app:units`
`app:glossary`. (The dead `ch:bode` alias was removed in Round 4.)

Section labels, all 30 of them: `sec:complexrefresher` `sec:rms` `sec:secondorder`
`sec:decibels` `sec:asymptotes` `sec:nyquist` `sec:factoring` `sec:cascadeadd`
`sec:threepoles` `sec:puredelay` `sec:poleplacement` `sec:groupdelay`
`sec:infinitepoles` `sec:selfresonance` `sec:rc-freq` `sec:pep` `sec:commonmode`
`sec:lc-lowpass` `sec:filterspecs` `sec:lineloss` `sec:stubs` `sec:antennalength`
`sec:classes` `sec:beta-resistors` `sec:gbw` `sec:neutralization` `sec:mixers`
`sec:probe` `sec:groundloops` `sec:instpower`.

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

## 2. What Round 4 did (this session)

No markup file this round. The work came from two audits: a front-to-back
read-through of the whole book, and a coverage check against the **General
(Element 3)** pool — 423 questions, of which 236 are circuit/electronics questions,
distilled to a 157-concept checklist. Four commits, all pushed.

### 2a. Ch 6 was an orphan (the biggest finding)

`ch:highorder` and all five of its section labels were referenced **only from inside
Ch 6**. Nothing else in the book pointed into it, so every assertion Ch 6 was written
to retire was still being asserted elsewhere — and Ch 15's `advancedbox` was
independently **re-deriving** the Butterworth pole circle that `sec:poleplacement`
already derives, in violation of the cite-don't-re-derive convention.

Fixed: inbound references went **0 → 27**, from Chs 1, 3, 4, 5, 10, 15, 16, 17, 18.
Ch 6 also gained `sec:puredelay` and `sec:infinitepoles` (§6.5 and §6.9 had no
labels), and contributed its first rows to the formula index — including taking over
the `−20n` dB/decade row, which had been credited to `ch:filters`.

### 2b. Read-through defects

- **Nyquist.** Ch 17 said "the Nyquist −1 point" but the book never introduced the
  Nyquist plot. New `sec:nyquist` in Ch 5 draws `L(jω)` in the complex plane and reads
  both margins off it as one clearance from one point — deliberately **without** the
  encirclement criterion, which nothing here needs. A `mistakebox` separates it from
  the unrelated Nyquist **sampling** theorem, stating `f_s > 2·f_max` and aliasing;
  Alex asked for this explicitly, and it gives a cheap foothold on E7F/E8A.
- **Acronyms.** Ch 6 had introduced regressions: SSB, CW, FIR all appeared unexpanded
  there and were expanded only later. Fixed, along with HF, FET, DSP.
- **Ch 13 ordering.** §13.10 used the worked example's numbers and called them "the
  same worked example" — but the worked example was §13.11. The phasor material is now
  a *subsection* of the worked example, so the chapter again closes with it.
- **Orphan labels: 9 → 0.** Four figures (`fig:phasor`, `fig:series-z`,
  `fig:smith-basic`, `fig:feedback-loop`) were never referenced; the `fig:smith-basic`
  reference now also carries the pool's Smith-chart vocabulary (resistance axis, prime
  center, wavelength scales), closing the old §4B.8 item.
- **Glossary.** Four alphabetization errors fixed; **30 → 47 entries**.
- **Callout coverage.** Every teaching chapter (2–18) now has an `exambox` except the
  two-page hinge Ch 10, and Chs 11–14 each now have a `workedbox` — they had none.

### 2c. Coverage gaps closed

| Gap | Where it landed |
|---|---|
| **RMS never derived** (used in 17 files on the strength of one parenthetical) | new `sec:rms` in Ch 2 — derives it from the cycle-average of `cos²`, which also explains the `√2` in the phasor definition |
| **PEP absent entirely** | new `sec:pep` in Ch 9 — average power, scope readings, `P = V_pp²/8R`, PEP as the average over the largest cycle |
| **Ch 16 was entirely lossless**, yet Ch 18 already used "3 dB of matched-line loss" | new `sec:lineloss` — full complex propagation constant `γ = α + jβ` per Alex's choice, complex `Z_0`, low-loss limit, √f law tested against a cable table, mismatched-line loss with both sanity limits, `\|Γ_in\| = \|Γ_L\|e^{−2αℓ}` |
| Self-resonance and skin effect taught **only in Ch 20**, the practice chapter | new `sec:selfresonance` in Ch 7 |
| Ch 17 §Power Supplies was **7 lines** | rebuilt: conduction angles, ripple at `2f_line`, filter as low-pass, bleeder as RC discharge |
| **Neutralization absent** | new `sec:neutralization` — the one place feedback is deliberately cancelled |
| Mixer roles, image offset, two-tone test | `sec:mixers` — image at `2·f_IF`, four jobs of one multiplier, why the linearity test uses two tones |
| Ferrites, common-mode current | new `sec:commonmode` in Ch 12 — a ferrite choke is a filter in *mode*, not frequency |
| Ground loops | new `sec:groundloops` in Ch 18 — KVL around the return path |
| Filter datasheet vocabulary | new `sec:filterspecs` in Ch 15 — insertion loss, ultimate rejection, shape factor |
| Antenna length, dBi/dBd | new `sec:antennalength` in Ch 16 — **derives** 468/f and 234/f rather than quoting them |
| S units, link budgets | Ch 18 §Decibels in Measurement |
| Reactive power described only as "sloshing" | new `sec:instpower` in Ch 9 — derives the `2\omega` term, so the metaphor becomes an equation and the power factor falls out (from the ARRL Ch 4 audit) |

### 2d. Verification

44 new numeric results re-derived independently in Python — **all pass**. Every new
page rendered at 95 dpi and visually inspected. Cheat sheet gained RMS/PEP/line-loss
rows (and its new section was moved to avoid straddling a column break). No figures
were added or changed, so no figure regeneration was needed.

---

## 3. Exam coverage

### Extra (Element 4) — the book's actual target

Against the 2024–2028 pool: **8 groups covered well** (E5A, E5B, E5C, E7C, E7G, E9E,
E9F, E9G), **13 partial**, **29 absent** — so roughly 21 of 50 generously, ~15
strictly, against **37/50 to pass**. Round 4 improved E4B, E5D, E7B, E7E, E9A and
E9G but did not change the headline: this book alone is not sufficient, and the
preface says so.

### General (Element 3) — checked in Round 4

423 questions, 35 groups; **236 (56%) are circuit/electronics questions** — all of G5
(40), G6 (23), G7 (38), plus most of G4, G8, G9. Distilled to 157 distinct concepts.

**Verdict: the electrical-principles core is now covered, and covered by derivation.**
What remains absent is absent *by design* and named in the preface: device physics
(diode drops, MOSFET/JFET/tube structure, capacitor dielectrics), schematic-symbol
identification, digital logic, modulation theory (Carson's rule, deviation, QPSK/FSK,
I/Q), protocols, electrical code and RF-exposure safety, propagation, operating
practice, and antenna pattern geometry.

Two caveats on the source file: the HamExam General export carries **no cycle dates**
(don't cite 2023–2027 from it — that came from the other PDF's filename), and it is
**missing three IDs**: G6B09, G8C01, G9C06. Cross-check against NCVEC before relying
on any count. Full inventory: see the scratchpad file
`general-pool-circuits-inventory.md` from the Round 4 session, or regenerate it.

---

## 4. Recommended next steps, in priority order

### A. Decide on the ARRL audit findings

**Done, and waiting on you: see [`ARRL-GAP-PROPOSAL.md`](ARRL-GAP-PROPOSAL.md).**

Alex's standing request was to review ARRL Extra manual Chs 4, 6, 7 and 9 for content
that is missing from the book but within its scope and spirit — framed as "they
assert, we derive." That audit ran in Round 4 and produced 28 ranked proposals.
Nothing has been written into the book from it except one item that was a defect by
our own convention (`sec:instpower`, below).

Headline: the strongest finding is a **new chapter, "Noise, Sensitivity, and Dynamic
Range"** (six derivations: the −174 dBm/Hz floor, noise figure and Friis, the power
series that generates every dynamic-range number, the 2/3 in DR3, reciprocal mixing
and the 1/Q_L² phase-noise skirt, and noise bandwidth ≠ −3 dB bandwidth). Then a
tier of ten single sections, of which the best thesis fits are **the PLL as a control
loop** and **S₂₁ *is* the Bode transfer function**.

**⚠️ Critical caveat, recorded in the proposal:** the manual in `references/` is the
**12th edition, keyed to the 2020–2024 pool**, not the current 2024–2028 one. This
already produced one wrong claim (power factor, cited as ten E5D questions — it is
now only a distractor) and one bad citation (E7H14/E7H15 do not exist). Every pool ID
in the proposal has been re-verified against the real pool; treat any *new*
exam-relevance claim sourced from the manual as suspect.

### B. Content gaps still open

1. **Sampling and DSP (E7F, E8A, plus General G7C).** `sec:nyquist`'s mistakebox now
   states the sampling theorem in one sentence, which is a foothold and not coverage.
   A real treatment — Nyquist rate, aliasing as spectral folding, ≈6 dB/bit,
   decimation, FIR/IIR — pairs naturally with `sec:groupdelay`. **Alex has not
   authorized this**; it was deliberately left out of Round 4's scope.
2. **Receiver noise and dynamic range (E4C/E4D).** Still the most defensible
   addition: `sec:mixers` now derives image response *and* third-order products *and*
   the two-tone test, so only the **metrics** are missing — `kTB`, the −174 dBm/Hz
   floor, noise figure, cascaded NF (Friis), MDS, 1 dB compression, IP3 and its 3:1
   slope, blocking/IMD dynamic range. All arithmetic on machinery that now exists.
3. **Phase-locked loops (E7H).** A control loop in radio clothing — the strongest
   thematic fit of anything missing. Chs 5, 6 and `sec:nyquist` supply every tool.
4. **Rebuild Ch 19 (Worked Examples).** Unchanged and still the weakest chapter: four
   examples with zero cross-references, zero poles, and component values unrelated to
   the book's running examples — a direct contradiction of the thesis, in the chapter
   meant to demonstrate it. Either make it a pure map (Ch 21 carries the real
   cross-chapter practice) or rebuild it around the book's running values.
5. **Antenna patterns and gain (E9A/E9B).** `sec:antennalength` added dBi/dBd and
   length; ERP/EIRP and beamwidth remain.
6. **S-parameters and the VNA (E4B).** `S₁₁` *is* `Γ`, already derived; `S₂₁` is
   forward gain. Half a page.

### C. Smaller cleanups still outstanding

- **Ch 10 and Ch 19 have no callout boxes and no figures.** Ch 10 is defensible as a
  two-page hinge; Ch 19 is not (see B4).
- **Figure provenance:** 26 of 27 computed figures still don't say how they were
  generated. Consider a one-line "computed from…" clause per caption, or one note in
  the front matter.
- **Ch 20 mixes two structural registers** — numbered sections with starred
  per-question subsections, then abandons the pattern halfway.
- **Appendix B** still restates Ch 7's units material (cross-referenced, not merged).
- **No figure has been added since Round 3.** Several new sections would benefit from
  one: `sec:nyquist` especially wants a Nyquist plot showing the two margins as one
  clearance, and `sec:lineloss` wants an attenuation-versus-frequency curve.

### D. Still awaiting Alex's judgment

- **Preface personal paragraph** — names the University of Notre Dame and says the
  book was drafted with ChatGPT and developed with Claude Code. Tune the candor.
- **Notation carets (S7 / C-p4 from Round 2)** — the ω/f caret markup was ambiguous;
  notation left as-is.
- **Whether to open the sampling/DSP topic** (B1) — it is the one place where the
  preface's declared scope and the exam's demands genuinely conflict.

---

## 5. How to resume

```bash
cd /Users/adowling/GitHub/radio-extra-book
make book          # -> main.pdf and output/Circuit_Theory_for_the_Amateur_Extra_Exam.pdf
```

Health checks that should all stay at zero:

```bash
make book >/dev/null 2>&1; grep -ci undefined main.log; grep -cE 'Overfull.*\(([2-9][0-9]|[0-9]{3,})\.' main.log
```

Orphan labels and dangling references — both lists should be empty:

```bash
python3 -c "
import re,glob
t=''.join(open(f).read() for f in glob.glob('chapters/*.tex')+glob.glob('frontmatter/*.tex')+glob.glob('appendices/*.tex'))
L=set(re.findall(r'\\\\label\{([^}]+)\}',t)); R=set()
for m in re.findall(r'\\\\[cC]?ref\{([^}]+)\}',t): R.update(p.strip() for p in m.split(','))
print('orphan:',sorted(L-R)); print('dangling:',sorted(R-L))"
```

No hard-coded cross-references (should print nothing):

```bash
grep -nE '(Chapter|Section|Figure|Table|Appendix) *~?[0-9]' chapters/*.tex frontmatter/*.tex appendices/*.tex | grep -v '\\label'
```

Before committing figure changes, render and eyeball them:

```bash
pdftoppm -r 110 -png figures/<name>.pdf /tmp/chk && open /tmp/chk-1.png
```
