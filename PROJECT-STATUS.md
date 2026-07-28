# Project Status and Next Steps

**Running status file — update this at the end of each working session.**
Last updated: 2026-07-28 (Round 4, plus the Round 5 environment check below).

## Round 5 (in progress)

**Start-up check on the new machine:** `make all` and `make figures` both succeed;
figures regenerate byte-identically; `./scripts/check.sh` prints **ALL CHECKS PASSED**
(196 pages, 23 chapters, 29 figures, 57 section labels, 65 glossary entries). One
portability bug was fixed in the checker itself — see §5b.

**The question pools are now in the repo** (§5a), with greppable markdown extracts of
their circuit questions. Pool citations are verifiable again; the ARRL manual is still
gitignored, so the `notes/` audits still cannot be re-run.

**Ledger progress: Tier A is complete (A1–A5)** — the exact half-power bandwidth
(`sec:halfpower`), the series↔parallel transformation (`sec:seriesparallel`, which
also made `sec:lnetwork` a derivation), skin depth (in `sec:selfresonance`),
the conduction-angle efficiency integral (`sec:conductionangle`, plus a new
`sec:switching` that finally covers Class D), and push-pull even-order cancellation
(`sec:pushpull`, which also retired `sec:mixers`'s on-faith carrier-suppression
claim). Two of the five caught errors of our own: A3 found Ch 22 giving the wrong
reason for coil `Q` falling, and A5 found the same mistold for push-pull and IMD.

**Tier B1 (S-parameters) is also done** — `sec:sparams` in Ch 16 and `sec:vna` in
Ch 20, the latter carrying the `controlsbox` where Part II's `G(jω)` and Part IV's
circuits finally meet on an instrument screen. **B2 (feedback sets impedance) is done too** — `sec:feedbackz`. **Next: B3 onward.**
See §6 for the plan, and the LEDGER in `ARRL-GAP-PROPOSAL.md` for the running score.

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

- **23 chapters + 3 appendices, five parts, 196 pages, 29 figures.**
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
| **IV — Applying the Circuit Models** | 15 Filters, Matching, Transformers · 16 Transmission Lines · 17 Active Circuits · 18 Sampling & DSP · 19 Noise, Sensitivity & Dynamic Range · 20 Measurement |
| **V — Practice and Study** | 21 Worked Examples & Exam Map · 22 Anchored Practice · 23 Cross-Chapter Problems |
| **Appendices** | A Formula Index · B Units & Prefixes · C Glossary |

Labels are stable across renumbering — **always `\cref`, never hard-code a number.**
Chapter labels: `ch:studyguide` `ch:complex` `ch:linsys` `ch:splane` `ch:feedback`
`ch:highorder` `ch:foundations` `ch:resistive` `ch:ac` `ch:fourviews` `ch:rc` `ch:rl`
`ch:rlc` `ch:rlcpar` `ch:filters` `ch:lines` `ch:active` `ch:measurement`
`ch:dsp` `ch:noise` `ch:exammap` `ch:practice` `ch:crossproblems` `app:formulas` `app:units`
`app:glossary`. (The dead `ch:bode` alias was removed in Round 4.)

Section labels, all 57 of them: `sec:complexrefresher` `sec:rms` `sec:secondorder`
`sec:decibels` `sec:asymptotes` `sec:nyquist` `sec:factoring` `sec:cascadeadd`
`sec:threepoles` `sec:puredelay` `sec:poleplacement` `sec:groupdelay`
`sec:infinitepoles` `sec:selfresonance` `sec:rc-freq` `sec:pep` `sec:commonmode`
`sec:lc-lowpass` `sec:filterspecs` `sec:lineloss` `sec:stubs` `sec:antennalength`
`sec:classes` `sec:beta-resistors` `sec:gbw` `sec:neutralization` `sec:mixers`
`sec:probe` `sec:groundloops` `sec:instpower` `sec:fourier` `sec:parseval`
`sec:samplingismult` `sec:samplingthm` `sec:quantnoise` `sec:decimation` `sec:firiir`
`sec:noisefloor` `sec:noisefigure` `sec:friis` `sec:powerseries` `sec:compression`
`sec:dynamicrange` `sec:phasenoise` `sec:noisebw` `sec:sunits` `sec:pll`
`sec:halfpower` `sec:polegeometry` `sec:seriesparallel` `sec:lnetwork` `sec:conductionangle` `sec:switching` `sec:pushpull` `sec:sparams` `sec:vna` `sec:feedbackz`.

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
distilled to a 157-concept checklist. Ten commits, all pushed.

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
- **Glossary.** Four alphabetization errors fixed; **30 → 65 entries**.
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

### 2e. Two new chapters (after Alex reviewed the ARRL audit)

Alex authorized both the Tier 1 noise chapter and the sampling/DSP topic that had
been flagged as an open scope question.

**Ch 18 Sampling and DSP.** Thesis: sampling *is* multiplication, so `sec:mixers`
did the hard part. An impulse train is periodic, so it is a sum of *all* harmonics of
`f_s`; multiplying by that comb replicates the spectrum at every multiple of `f_s`,
and everything else follows — the sampling theorem as a non-overlap condition,
aliasing as folding, and the fact that two frequencies give *identical* sample
sequences so no processing can separate them. Then quantization
(`SNR = 6.02N + 1.76`, the same 6 dB as an S unit), oversampling processing gain,
decimation vs interpolation, the zero-order hold's sinc droop, and DDS.
`sec:firiir` **proves Ch 15's asserted linear-phase claim** from coefficient
symmetry.

**Ch 19 Noise, Sensitivity, and Dynamic Range.** Johnson–Nyquist plus *our own*
maximum-power-transfer result gives `kTB` (the resistance cancels) and −174 dBm/Hz.
Noise figure makes the usual dB addition a theorem; Friis gives the
first-stage-dominates and preamp-at-the-mast results. `sec:powerseries` is the
spine: one power series yields the 2 and 3 dB/dB slopes, gain compression, IIP3, and
`IIP3 = P₁dB + 9.6 dB` free — then `DR3 = ⅔(IIP3 − MDS)` with the 2/3 as slope-3
geometry. `sec:phasenoise` derives the `1/Q_L²` skirt (doubling loaded Q buys 6 dB),
and `sec:noisebw` closes the chapter's own `10 log B` assumption.

**Supporting:** new `sec:fourier` in Ch 3 finally states *why* analyzing one sinusoid
at a time is legitimate — `G` at the harmonics is the whole answer, the licence for
Part II's entire method, previously unstated — and gets the square wave's odd
harmonics from half-wave symmetry. New `sec:parseval` in Ch 2 adds Parseval and the
1.111 form factor, so "use a true-RMS meter" becomes "an averaging meter reads a
square wave 11 % high."

The preface no longer lists receiver metrics and DSP as acknowledged thin areas,
because they no longer are.

### 2d. Verification

82 new numeric results re-derived independently in Python — **all pass**. Every new
page rendered at 95 dpi and visually inspected. Cheat sheet gained RMS/PEP/line-loss
rows (and its new section was moved to avoid straddling a column break). No figures
were added or changed, so no figure regeneration was needed.

---

## 3. Exam coverage

### Extra (Element 4) — the book's actual target

Against the 2024–2028 pool, Round 4 moved the needle materially. Previously **8
groups covered well**, 13 partial, 29 absent. The two new chapters add **E4C and E4D**
(receiver performance and dynamic range) and **E7F and E8A** (SDR/DSP and
Fourier/RMS/conversion) as genuinely covered, and Round 4's smaller additions
improved E4B, E5D, E7B, E7E, E9A and E9G. That is roughly **12 groups covered well**
now, against **37/50 to pass** — so the headline is unchanged and the preface still
says so honestly, but the circuit-theory portion of the syllabus is close to
exhausted. What remains absent is overwhelmingly the by-design list.

### General (Element 3) — checked in Round 4

423 questions, 35 groups; **236 (56%) are circuit/electronics questions** — all of G5
(40), G6 (23), G7 (38), plus most of G4, G8, G9. Distilled to 157 distinct concepts.

**Verdict: the electrical-principles core is now covered, and covered by derivation.**
What remains absent is absent *by design* and named in the preface: device physics
(diode drops, MOSFET/JFET/tube structure, capacitor dielectrics), schematic-symbol
identification, digital logic, modulation theory (Carson's rule, deviation, QPSK/FSK,
I/Q), protocols, electrical code and RF-exposure safety, propagation, operating
practice, and antenna pattern geometry.

*Updated in Round 5:* the cycle is confirmed **2023–2027** (valid through 2027-06-30),
and the missing IDs are real absences, not an extraction fault — `G8C01` is a dated
NCVEC withdrawal, while `G6B09` and `G9C06` remain unexplained. The full inventory is
no longer a scratchpad file: it is
[`references/general-pool-circuits.md`](references/general-pool-circuits.md), tracked in
the repo, and it is over-inclusive at 249 questions (all of G4–G9) against the 236 that
Round 4 hand-filtered.

---

## 4. Recommended next steps, in priority order

### A. Decide on the ARRL audit findings

**See [`ARRL-GAP-PROPOSAL.md`](ARRL-GAP-PROPOSAL.md), and in particular the LEDGER at
the end of it.** That ledger reconciles *all three* Round 4 audits — the read-through,
the General-pool check, and the four ARRL chapter audits — against the book as built,
so nothing can be silently dropped. Current score: **33 done, 24 open**, with the open
items ranked in four tiers.

The highest-priority open items are **Tier A: things the book asserts itself**, and so
are defects by our own derive-don't-assert convention rather than new content — the
exact half-power bandwidth (asserted in five places), the series-to-parallel
`(1+Q²)` transformation (which *is* Ch 15's asserted L-network `Q`), skin depth
(asserted in four places), the conduction-angle efficiency integral, and push-pull
even-order cancellation. Then **Tier B**, the best remaining thesis bridges, led by
**S-parameters** (`S₂₁` *is* `G(jω)`, so a VNA sweep is literally a Bode plot) and
**feedback setting impedance** (which retires the op-amp ideals as axioms).

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

1. ✅ **Sampling and DSP — done** (`ch:dsp`). Authorized and written.
2. ✅ **Receiver noise and dynamic range — done** (`ch:noise`). Authorized and written.
3. ✅ **Phase-locked loops (E7H) — done** (`sec:pll`, in Ch 17 after the oscillators).
   With it written, the top remaining content gap is **Tier A of the ledger** (§6),
   which is defect-fixing rather than new content, followed by **B1 S-parameters**.
4. **Rebuild Ch 21 (Worked Examples).** Unchanged and still the weakest chapter: four
   examples with zero cross-references, zero poles, and component values unrelated to
   the book's running examples — a direct contradiction of the thesis, in the chapter
   meant to demonstrate it. Either make it a pure map (Ch 21 carries the real
   cross-chapter practice) or rebuild it around the book's running values.
5. **Antenna patterns and gain (E9A/E9B).** `sec:antennalength` added dBi/dBd and
   length; ERP/EIRP and beamwidth remain.
6. **S-parameters and the VNA (E4B).** `S₁₁` *is* `Γ`, already derived; `S₂₁` is
   forward gain. Half a page.

### C. Smaller cleanups still outstanding

- **Ch 10 and Ch 21 have no callout boxes and no figures.** Ch 10 is defensible as a
  two-page hinge; Ch 21 is not (see B4).
- **Figure provenance:** 26 of 27 computed figures still don't say how they were
  generated. Consider a one-line "computed from…" clause per caption, or one note in
  the front matter.
- **Ch 22 mixes two structural registers** — numbered sections with starred
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
- **Whether to get the 13th-edition ARRL manual.** The copy in `references/` is keyed
  to the 2020–2024 pool, which already produced one wrong finding in the audit
  (see `ARRL-GAP-PROPOSAL.md`).

---

## 5. Resuming on a different computer

Everything needed to build the book is in the repository. **Two things are not**, and
both will silently degrade the workflow if you do not notice:

### 5a. `references/` — the pools now come with the clone; the manuals do not

**Changed in Round 5.** Both question pools are now tracked in git, along with two
greppable markdown extracts of their circuit questions, so **pool identifiers and
answer letters are verifiable on a fresh clone.** See
[`references/README.md`](references/README.md).

| File in `references/` | Tracked | Used for |
|---|---|---|
| `HamExam.org Extra Question Pool.pdf` | ✅ | Verifying every pool ID and answer letter cited in Ch 22; the coverage map in §3 |
| `HamExam.org General Question Pool.pdf` | ✅ | The General coverage check (`notes/audit-general-pool.md`) |
| `extra-pool-circuits.md` | ✅ derived | 420 of 599 Extra questions — the circuits and calculation subelements, greppable |
| `general-pool-circuits.md` | ✅ derived | 249 of 423 General questions, same basis |
| `ARRL_Extra_Class_Lcense_Manual_12th_Edition.pdf` | ❌ | The four ARRL audits in `notes/`. **Get the 13th edition** — see §4D; the 12th is keyed to the 2020–2024 pool and produced one materially wrong finding |
| `Ham_Extra_Circuits_Study_Guide_First_Draft.docx` | ❌ | The original Word draft the book grew from — Alex's own files |
| Other study guides (KB6NU, etc.) | ❌ | Terminology cross-checks only; optional |

Prefer the markdown over the PDFs — checking a coverage claim is now a `grep`:

```bash
grep -n -i "half-power\|bandwidth" references/extra-pool-circuits.md
```

The markdown is **derived data**; never hand-edit it. Regenerate after replacing a PDF:

```bash
./scripts/build_pool_md.sh
```

Three caveats the extracts record for you, and one that is resolved:

- **32 questions depend on a figure** that exists only in the PDF. Each file lists
  them; they are unanswerable from the markdown.
- **Five absences are unexplained**: `E9E10`, `G1C08`, `G1C10`, `G6B09`, `G9C06`. These
  IDs appear nowhere in the PDF text. Round 4 guessed that three of them were an
  extraction fault — that was wrong. Verify against NCVEC before relying on any count.
- Removals *are* now traceable: `E2A13`, `E4D05`, `E6D07`, `G1A04`, `G1C09`, `G1E09`
  and `G8C01` are matched to dated NCVEC withdrawals.
- ✅ **Resolved:** the General cycle. It is the **2023–2027** pool, valid through
  2027-06-30, confirmed from hamexam.org's pool table. Round 4 was right to distrust
  the filename, but the dates were correct.

### 5b. Toolchain

```bash
# macOS
brew install --cask mactex          # or basictex + tlmgr install the packages below
brew install poppler                # pdfinfo, pdftoppm, pdftotext — used for verification
pip3 install numpy scipy matplotlib # figure generation

# Debian/Ubuntu
sudo apt install texlive-full poppler-utils python3-numpy python3-scipy python3-matplotlib
```

LaTeX packages used: `amsmath` `siunitx` `booktabs` `tabularx` `longtable` `tcolorbox`
`tikz` `circuitikz` `pgfplots` `hyperref` `cleveref`. With a minimal TeX Live install,
`circuitikz` and `tcolorbox` are the two most likely to be missing.

`scripts/check.sh` embeds Python heredocs, so it runs under whatever `python3` is first
on `PATH` — on this machine that is an Anaconda 3.9, not the system Python. Keep the
embedded code 3.9-compatible; one check silently reported a `SyntaxError` instead of a
result until it was.

### 5c. First commands on the new machine

```bash
git clone <remote> radio-extra-book && cd radio-extra-book
make all            # book + cheat sheet; PDFs land in output/
./scripts/check.sh  # must print ALL CHECKS PASSED
```

`scripts/check.sh` is the whole verification suite in one command — undefined
references, overfull boxes, multiply-defined labels, orphan labels, dangling
references, hard-coded cross-references, glossary alphabetization, and figure/include
agreement. **It should print `ALL CHECKS PASSED` on a clean checkout.** If it does not,
the toolchain is wrong, not the book.

Regenerating figures is optional — the PDFs are committed — but confirm it works
before you edit one:

```bash
make figures        # or: cd figures/src && python3 <name>.py
```

### 5d. Verifying a figure you changed

Committed figures were all visually inspected. Any change must be too, because
matplotlib will happily overlap two labels:

```bash
pdftoppm -r 130 -png figures/<name>.pdf /tmp/chk && open /tmp/chk-1.png
```

### 5e. Where to start reading

1. This file, §1 (structure and conventions) and §4 (what to do next).
2. The **LEDGER** at the end of `ARRL-GAP-PROPOSAL.md` — the reconciled list of every
   outstanding suggestion, ranked. Alex has approved all four tiers.
3. `notes/README.md` if you need the full reasoning behind a specific item.
4. §6 below for the agreed order of work.

---

## 6. The approved work plan (Tiers A–D)

Alex approved **all four tiers** of the ledger. This is the order to take them in, and
why. Each item is short; none needs a new chapter.

### ✅ Tier A — complete. All five landed in Round 5.

These are not new content. They are places where the book violates its own
**derive-don't-assert** convention, which makes them defects rather than additions.
Fixing them also *removes* text in a couple of cases.

| Order | Item | Home | The move |
|---|---|---|---|
| ✅ A1 | **Exact half-power bandwidth** — done (`sec:halfpower`) | `ch:rlc` §Q and Bandwidth | `\|Z\|² = R²[1 + Q²(ω/ω₀ − ω₀/ω)²]`; half power gives a quadratic whose two roots **differ by exactly `ω₀/Q`** and **multiply to exactly `ω₀²`**. So `BW = f₀/Q` is an equality for the current response, and the band edges straddle resonance *geometrically*: `f₀ = √(f₁f₂)`. Quantify the error in arithmetic centring (≈`1/8Q²`). Then relax the hedge in the four other places that state it. |
| ✅ A2 | **Series↔parallel, `R_p = (1+Q²)R_s`** — done (`sec:seriesparallel`) | `ch:rlcpar`, after §Why Q Inverts | Equate `1/Z_series` with `Y_parallel` at one frequency. Retires three of *our* assertions: a real tank's `Z_max` is `Q²R_s` (not "approximately the circuit resistance"); `Q_s` and `Q_p` are one quantity seen through this map; and solving `R_hi = R_lo(1+Q²)` **is** `ch:filters`'s asserted L-network `Q`. Cross-ref from Ch 23 problem 3, which currently does this conversion as an unexplained step. |
| ✅ A3 | **Skin depth** — done (`sec:selfresonance`) | `sec:selfresonance` | `∂²J/∂x² = μσ ∂J/∂t` with `e^{jωt}` gives `J ∝ e^{−x/δ}e^{−jx/δ}`, `δ = √(2/ωμσ)`. Copper: 66 µm at 1 MHz, 5.5 µm at 144 MHz. Then `R_AC ∝ √f` from an annulus of thickness `δ` — the law we now assert in **four** places. Also explains why coil `Q ∝ √f` rises then falls. |
| ✅ A4 | **Conduction-angle efficiency** — done (`sec:conductionangle`, `sec:switching`) | `sec:classes` | Fourier `a₀`/`a₁` of a cosine truncated at half-angle `θ`; `η = ½(a₁/a₀)(V₁/V_dc)` returns ½ at `θ=180°`, ¼ resistively loaded (the asserted 25 %), `π/4 = 78.5 %` at `θ=90°`. For switching, `p = vi` with an ideal switch forces one factor to zero always, so `∫p dt = 0` identically. Replaces four numbers currently on ARRL's authority. |
| ✅ A5 | **Push-pull even-order cancellation** — done (`sec:pushpull`) | `sec:classes` + `sec:mixers` | `f(x) − f(−x) = 2Σ_{n odd}aₙxⁿ`. Even orders cancel *identically for any f*, which is why the pair must be **matched** rather than specially biased. Two corollaries: push-pull does **nothing** for third-order IMD (the product `sec:powerseries` says matters), and the same algebra is why a *balanced* mixer nulls carrier feedthrough — which `sec:mixers` currently takes on faith. |

### Tier B — the thesis bridges. Start with B1.

**✅ B1 — done** (`sec:sparams`, `sec:vna`). One caveat the plan below did not
anticipate: `S₂₁ = V₂/V₁` only when the input is matched; in general
`V₂/V₁ = S₂₁/(1+S₁₁)`. The book now states that in a `mistakebox` rather than
repeating the usual slogan unqualified.

**B1. S-parameters, and `S₂₁` *is* the transfer function.** Alex specifically flagged
this one, and it is the best remaining bridge in the book. The groundwork is already
laid: `ch:lines` splits `V` and `I` into forward and reverse waves, which is the hard
part. Then

- define `a = (V + Z₀I)/2√Z₀`, `b = (V − Z₀I)/2√Z₀` — an invertible **change of basis**
  from `(V, I)`, exactly the kind of coordinate change the state-space chapters already
  make;
- for a one-port, `S₁₁ = b/a = (Z − Z₀)/(Z + Z₀) = Γ` **identically**, so `\|S₁₁\|²` is
  the reflected power fraction and return loss is `−20log₁₀\|S₁₁\|` — both already in
  the book;
- and the payoff: **`S₂₁` is the forward transmission of a two-port terminated in
  `Z₀`, i.e. it *is* `G(jω)`** from Chs 3–4. Therefore **a VNA's magnitude-and-phase
  sweep is literally a Bode plot**, and a filter's `\|S₂₁\|` trace is the `ch:filters`
  response measured rather than computed.
- Three calibration standards (short, match, open → `Γ = −1, 0, +1`) because the error
  network has three unknown complex terms. Three equations, three unknowns.

Home: definition in `ch:lines` right after §Reflection Coefficient; the VNA reading in
`ch:measurement` §SWR Bridge and Antenna Analyzer. Pool: E4B03/04/05/07/11.

*Suggested framing:* this is the moment the book's two halves shake hands — the
instrument on the bench is measuring the object Part II taught. Worth a `controlsbox`
saying exactly that.

**B2–B7**, in ledger order: feedback sets impedance (retires the op-amp ideals as
axioms) · antenna efficiency `η = R_rad/(R_rad+R_loss)` with the counterintuitive
payoff that loss *widens* SWR bandwidth while lowering efficiency · feed-point
impedance `R(z) = R_center/cos²βz` · the two-element array factor · the crystal as two
resonances · the named antenna matches as our L-network built from our stubs.

### Tier C and D

Tier C is fifteen small items — take them opportunistically, several are two or three
sentences. Tier D is housekeeping: **Ch 21 is the weakest chapter in the book** and
should either become a pure map or be rebuilt on the running examples; figure
provenance is 2 of 29 captions; Ch 22 mixes two structural registers; Appendix B
restates Ch 7.

### Working rules for any of it

- Run `./scripts/check.sh` before every commit. Zero everywhere.
- **Re-derive every number independently** before committing it. This session found
  four errors that way, including one in an audit's central claim.
- Cite, don't re-derive. If an earlier chapter has the result, `\cref` it.
- New section ⇒ give it a `\label` **and reference it from somewhere**, or the orphan
  check will catch you. Ch 6 spent a whole round as an orphan.
- Update the ledger in `ARRL-GAP-PROPOSAL.md` as items land.

---
