# Revision Notes — Round 2 (from "main 2.pdf" markup)

Parsed from Alex's marked-up PDF of the 82-page build. Colors group related
comments. This is the working plan; we'll settle the open questions, then execute.
IDs: `Dn` decisions, `Tn` themes, `Cn-page` per-location.

---

## DECISIONS MADE (2026-07-24)
- **D1 = Split it:** keep a short complex-number/phasor refresher up front (Part II);
  move impedance/admittance/complex-power/reactance (§2.3–2.8) into Part III near
  the circuits. (Landing spot TBD — see follow-up Q.)
- **D2 = Systems-first, general:** lead with generic LTI-systems language, say "LTI
  system" in the generic Part II chapters, add non-EE engineering examples, assume
  minimal EE. (Applies to T2, T3, and much of ch 3–4 voice.)
- **D4 = "Study Guide":** rename "Cheat Sheet Summary" → "Study Guide" (ch 1) and
  update the Part I / how-to-use references.
- **D5 = Color-code callout boxes:** each callout type gets its own accent color
  (palette consistent with the blue/green/amber theme; check light/dark).

## DECISIONS MADE (2026-07-24, second round)
- **Impedance lands = new AC-circuits chapter:** create a Part III chapter
  "AC Steady State: Impedance, Admittance, and Power" (from Ch 2 §2.3–2.8 +
  phasors-applied-to-circuits), placed after Foundations and before "One Circuit,
  Four Views."
- **Units = merged into Foundations** (drop standalone Units chapter).
- **Zeros/RLC-locus = → RLC chapter:** RLC root locus moves into Ch 10 (RLC);
  "Zeros in Radio Circuits" moves near the filters/traps material (Ch 12). Ch 4
  stays generic.
- **Four views = replace "must agree" with "offer complementary intuition"**
  throughout (drop the agreement framing).

### Resulting chapter structure (target)
- **Part I — Exam-Ready Reference:** Ch 1 "Study Guide" (was Cheat Sheet).
- **Part II — Math & Control-Theory Foundations:** Complex Numbers & Phasors
  (refresher only, §2.1–2.2); First/Second-Order Systems: Time & State Space;
  Frequency Response, Bode, and the s-Plane.
- **Part III — The Circuits:** Foundations (+ Units merged); **AC Steady State:
  Impedance, Admittance, Power (NEW)**; One Circuit, Four Views; RC; RL; RLC
  (+ root locus); Resistive Networks; Filters/Matching (+ Zeros in Radio Circuits);
  Active/Feedback; Transmission Lines; Measurement.
- **Part IV — Practice and Study:** Worked Examples; Anchored Practice.
- Voice: systems-first/general (D2); callout boxes color-coded (D5).

## 0. Big decisions (remaining — see Questions at the bottom)

- **D1 — Placement of the phasor/impedance material.** Repeated comments ask
  whether Chapter 2 (Complex Numbers, Phasors, Impedance), or at least §2.3–2.8,
  should come *after* the controls primer (ch 3–4), or move into Part III (the
  circuits), because it "references ideas introduced later in the book"
  (p17: "Is this necessary before the two controls chapters? Or could this move
  to the circuits section?"; p20: "Decision. Should 2.3 to 2.8 live here or after
  the controls refresher?"). Related: p36 wants the **Units chapter (ch 6) merged
  into the previous chapter**, and "discuss phasors applied to circuits here."
- **D2 — Audience level / voice.** Several comments ask to state things "without a
  circuits/EE background," to distinguish "controls language vs circuits
  language," and to generalize "circuit" → "LTI system" (p28). How far toward a
  general-engineering (non-EE) reader should the prose lean?
- **D3 — Personalization & provenance.** Preface should "add a more personalized
  paragraph about me and how this was generated" and "mention ChatGPT and Claude
  Code" (p2). Title page: author → **"Alexander Dowling (KE9FZD)"**, add
  **"control"** to the subtitle (p1). (Bibliography still lists the Word draft as
  the "primary source" — reconcile.)
- **D4 — Rename "Cheat Sheet."** p3 and p12 replace "Cheat Sheet" with
  "Study Guide" / "Quick" (Reference?). New name for Part I / Chapter 1?
- **D5 — Callout-box color coding.** p29: "Should we use different colors for each
  type of callout box?" (Controls Connection, Physical Insight, Energy Insight,
  Exam Relevance, Common Mistake, Units Check, Advanced Note.)

---

## 1. Structural / front-matter edits

- [ ] **S1 — Title subtitle (p1).** Add "control": e.g. "A Dynamical Systems and
  Control Perspective for Engineers." (D3)
- [ ] **S2 — Author line (p1).** "Alexander Dowling (KE9FZD)". (D3)
- [ ] **S3 — Central Framework box (p1).** "A circuit can be *considered* [was:
  read] through several equivalent representations…"
- [ ] **S4 — Preface personalization (p2).** Add a personal paragraph (who Alex
  is) and how the book was generated (ChatGPT + Claude Code). (D3)
- [ ] **S5 — Preface wording (p2).** "these views *offer complementary
  intuition*" (was: "must agree"). (Confirm — "must agree" is a recurring theme
  elsewhere; see Q.)
- [ ] **S6 — How to Use (p3).** Rename "cheat sheet" → "study guide". (D4)
- [ ] **S7 — Notation (p4).** ω/f typography carets — confirm intent (emphasis? no
  change needed?).
- [ ] **S8 — Bibliography.** Reconcile entry [3] (Word draft "primary source")
  with the de-provenanced preface. (D3)

---

## 2. Recurring themes (cross-cutting)

- [ ] **T1 — Complete the symbols table (§1.1).** Missing: Q (quality factor), ζ,
  X (reactance), Z (impedance), and (per p15 audit) Z₀, Γ, VF, β, ℓ, N_p/N_s, α,
  ω₀, ω_d, s, etc. Add the symbols actually used in the book. (p12, p15)
- [ ] **T2 — Audience calibration.** Generalize "circuit" → "LTI system" where the
  statement is generic (p28: "second-order LTI system (e.g., circuit)"); flag
  "controls vs circuits language"; make Bode-building rules readable without EE
  background (p28). (D2)
- [ ] **T3 — Engineering/physics examples.** Add common examples of first-order
  (p27) and second-order (p28) systems in engineering/physics (thermal, mechanical,
  process, etc.), for the non-EE reader.
- [ ] **T4 — Rigor / derivations.** Define the Laplace transform (integral) (p22);
  derive the √2 Re{X e^{jωt}} phasor relation from Euler's formula (p18); state
  explicitly that X is the (complex) phasor (p18).
- [ ] **T5 — Cross-references for "derived later."** Where a result (e.g. reactance
  behavior, p18) is derived in a later chapter, say so and cross-reference.
- [ ] **T6 — "Show it with root locus / Bode."** For the op-amp, feedback,
  oscillator, and active filter (ch 13): add root-locus and/or Bode figures
  (p61, p62, p63). Recurring request.
- [ ] **T7 — Op-amp modeling.** Explain how the op-amp is modeled (dependent-source
  / gain block — not L and C) (p60, p63).
- [ ] **T8 — Figure text overlap.** Fix annotation collisions in the Python
  figures: rc_transient (p41), rl_transient (p45), bode_first_order_highpass (p42).
- [ ] **T9 — Schematics as proper symbols.** Draw R_lo/R_hi as resistor symbols in
  the L-network figure (p58); add missing schematics (π/T network p57, transformer
  p58).

---

## 3. Page-by-page comment log

### Front matter
- [ ] **C-p1** Title: "(control)" into subtitle; author "Alexander Dowling
  (KE9FZD)"; "read"→"considered" in Central Framework box.
- [ ] **C-p2** Preface: personal + generation paragraph; "mention ChatGPT and
  Claude Code"; "must agree"→"offer complementary intuition"; "For example," +
  "exactly" underline (soften/expand).
- [ ] **C-p3** How to Use: "cheat sheet"→"study guide".
- [ ] **C-p4** Notation: ω/f carets (confirm).

### Ch 1 (Cheat Sheet / "Quick Reference")
- [ ] **C-p12** Rename "Cheat Sheet"→"Quick" (Reference/Summary). Symbols table
  missing Q, ζ, X, Z, … (T1).
- [ ] **C-p14** BW ≈ f₀/Q — "Should this be Q_s?" (verify series vs generic Q in
  the cheat sheet). Oscillator/imaginary-axis wording: "or is [it] an oscillator,
  more clearly?" (clarify marginal-stability phrasing).
- [ ] **C-p15** "Need to audit the symbols table in 1.1 — many of these are
  missing." (T1)

### Ch 2 (Complex Numbers, Phasors, Impedance)
- [ ] **C-p17** "Is this necessary before the two controls chapters? Or could this
  move to the circuits section?" (D1)
- [ ] **C-p18** (dense): "What is capital X in this formula? Is X real or complex?"
  (clarify X = complex phasor); "Add a figure that shows unit circle, polar↔
  rectangular, and this formula"; "I am struggling to reconcile this with Euler's
  formula — please derive it for me"; his own understanding of phasors written out
  ("voltage and current are sine waves… convenient to represent as phasors — please
  correct me"); "Are these [reactance facts] derived in a later chapter? If yes,
  say so more explicitly / add a cross-reference." (T4, T5, and H-figure)
- [ ] **C-p20** "Decision: should 2.3–2.8 live here or after the controls
  refresher? This chapter references ideas introduced later." (D1)

### Ch 3 (First/Second-Order: Time & State Space)
- [ ] **C-p21** "Before *analyzing* [a] specific circuit" (insert "analyzing");
  reconsider "electrical clothing" ("simple"?).
- [ ] **C-p22** Laplace: "mathematically define this — is it a[n] integral?"
  (add the Laplace integral definition). (T4)

### Ch 4 (Frequency Response, Bode, s-Plane)
- [ ] **C-p27** §4.2: "What are some common examples of first-order systems in
  engineering/physics?" (T3)
- [ ] **C-p28** §4.3 Bode-building: "Can this be stated without a circuits/EE
  background?"; §4.5 "Is this controls language or circuits language?" and
  "circuit does"→"second-order LTI system (e.g., circuit) does"; "What are some
  common examples of second-order systems in engineering/physics?" (T2, T3)
- [ ] **C-p29** "Should we use different colors for each type of callout box?" (D5)
- [ ] **C-p31** Fig 4.4 (pole-zero notch): "Show unit circle?" (add the ω₀ circle).
- [ ] **C-p32** §4.8 "Zeros in Radio Circuits" — "move to a later [chapter]"; Fig
  4.6 (RLC root locus) — "save this for later." (M — move to RLC/filters)

### Ch 5 (Foundations) / Ch 6 (Units)
- [ ] **C-p36** "This [Units chapter] can get integrated into the previous
  chapter. Also discuss phasors applied to circuits here." (D1)

### Ch 8 (RC) / Ch 9 (RL)
- [ ] **C-p41** Fig 8.2 (rc_transient): "check plots for text overlap." (T8)
- [ ] **C-p42** Fig 8.3 (bode_first_order_highpass): "text overlap." (T8)
- [ ] **C-p44** Fig 9.1 (RL schematic): "Is this true output? If yes, should we
  say that?" (clarify output-across-R). 
- [ ] **C-p45** Fig 9.2 (rl_transient): "text overlap." (T8)

### Ch 12 (Filters, Matching, Transformers)
- [ ] **C-p53** §12.2 filter-types list: "Table? The spacing has issues." (K)
- [ ] **C-p57** §12.6.1 L-network "two reactances": "Show me a schematic"; §12.6.2
  π/T "virtual resistance": "Show me a schematic" (add π/T schematic). (T9)
- [ ] **C-p58** Fig 12.5 L-network: "Should these resistances be shown as
  resistors?" (draw R_lo/R_hi as resistors); §12.7: "Show me a schematic for
  transformer"; §12.8: "What is the problem statement for this worked example?"
  (add explicit problem statement). (T9, N)

### Ch 13 (Active Circuits, Feedback, Oscillators)
- [ ] **C-p60** Fig 13.1 op-amp: "How is the op-amp modeled? Is it an L and C
  component?" (explain the model). (T7)
- [ ] **C-p61** §13.6: "Show me root locus, Bode, etc. plots for an ideal op-amp."
  (T6)
- [ ] **C-p62** §13.7 Oscillators: "Show this with root locus and/or Bode plots."
  (T6)
- [ ] **C-p63** Fig 13.3 Sallen–Key: "Show how this is modeled, then show root
  locus and/or Bode plots." (T6, T7)

### Ch 14 (Transmission Lines)
- [ ] **C-p66** Fig 14.1 Smith chart: "Elaborate on how to interpret this — I own a
  NanoVNA and have made Smith charts for our antennas"; "I want to understand how
  this connects with the math"; **"Idea: generate a Smith chart in Python for an
  idealized antenna. Show me how to model the antenna, then generate the Smith
  chart."** (O — new Python Smith-chart figure + antenna model + deeper interp)

### Parts 4 / appendices: no annotations found (clean).

---

## 4. Scope & sequencing (decided)
- **All figure efforts are must-haves** this round (op-amp/feedback/oscillator
  root-locus+Bode; Python Smith chart for an idealized antenna; phasor/Euler figure
  + derivation; schematic fixes/additions).
- **Execution order:** (1) structure, (2) content, (3) figure-formatting pass,
  (4) read-through passes for consistency.

---

# EXECUTION PLAN (detailed — written to survive context compaction)

Work bottom-up on `/Users/adowling/GitHub/radio-extra-book`. Build with
`make book` (and `make all` for the standalone study-guide card); regenerate
Python figures with `make figures`. Render pages with `pdftoppm` and visually
check every new/changed figure and schematic. Commit after each phase; push to
`main` (Alex works on main). Detect annotated pages / verify with rendering.

## PHASE 1 — Structure (keep it building at every step; renumber files last)

1. **Split Chapter 2.** In `chapters/02_complex_numbers_and_phasors.tex`, KEEP the
   refresher: §"Complex Number Refresher" (rect/polar/Euler, worked conversion)
   and §"Why Complex Numbers Appear: Phasors". Retitle the chapter "Complex
   Numbers and Phasors". MOVE OUT (to the new AC chapter): §Impedance, §Series and
   Parallel (RLC impedance), §Admittance and Susceptance, §Phasor Lead and Lag,
   §Complex Power, §Worked Example (series reactance), AND the chemical-engineering
   analogy `physicalbox` table (it's about impedance). Keep `\label{ch:complex}`.
2. **New AC chapter.** Create `chapters/NN_ac_steady_state.tex`, "AC Steady State:
   Impedance, Admittance, and Power", `\label{ch:ac}`. Contents = the moved §2.3–2.8
   + a new opening that connects phasors to circuits (p36: "discuss phasors applied
   to circuits here") and affirms Alex's own framing from p18 (voltage & current are
   sinusoids in AC steady state; phasors represent them). Place in Part III AFTER
   Foundations and BEFORE "One Circuit, Four Views". `\input` it in `main.tex`.
3. **Merge Units into Foundations.** Fold `chapters/..._units.tex` (Base
   Relationships, Radio Prefixes, Dimensional Tests, Worked Unit Check, Common
   Mistakes) into the Foundations chapter as sections; remove the Units `\input`
   and `git rm` the file. (Appendix B "Units and Prefixes" stays as the reference
   table.)
4. **Move RLC root locus → Ch 10 (RLC).** Move the `fig:rlc-rootlocus` tikz figure
   and its narration from Ch 4 (`..._s_plane...tex`) into the RLC chapter's "Root
   Locus: Damping Set by R" section (it already references it). Keep Ch 4's generic
   `rootlocus_second_order` figure. Update `\cref`s.
5. **Move "Zeros in Radio Circuits" → Ch 12 (Filters).** Move that §4.8 section to
   the Filters chapter near the traps/notch material. Keep Ch 4's generic
   pole-zero/zeros discussion.
6. **Rename "Cheat Sheet Summary" → "Study Guide"** in `chapters/01_cheat_sheet.tex`
   (`\chapter{Study Guide}`), and update references in `frontmatter/how_to_use.tex`
   and `frontmatter/preface.tex`. Also retitle the standalone `cheat_sheet.tex`
   heading (e.g., "Printable Study Guide").
7. **Callout color-coding (D5).** In `preamble.tex`, give each `tcolorbox` a
   distinct accent (colframe) with a matching faint `colback`, legible in light &
   dark. Proposed palette (adjust for contrast):
   - Controls Connection → GuideBlue (`#244B5A`)
   - Physical Insight → teal/cyan accent
   - Energy Insight → GuideGreen (`#2F5D50`)
   - Units Check → GuideAmber (`#7A5C1E`)
   - Exam Relevance → muted indigo/purple
   - Common Mistake → muted red (`#8C2D2D`)
   - Advanced Note → slate/gray
8. **Rebuild, fix cross-refs, then renumber chapter files** to match the new order
   (two-phase `git mv` through temp names, as before) and update `main.tex`.
   Target order in §"Resulting chapter structure" above.

## PHASE 2 — Content

1. **Voice = systems-first/general (D2).** In the generic Part II chapters (3, 4),
   say "LTI system" where the statement is generic; add "(e.g., a circuit)"
   bridges. Apply p28 fix: "the circuit does" → "a second-order LTI system (e.g., a
   circuit) does". Make the Bode-building rules readable without EE background.
2. **Engineering/physics examples (T3).** First-order examples box (thermal
   cooling, a stirred tank's concentration, velocity under drag) in the first-order
   section; second-order examples box (mass-spring-damper, pendulum, vehicle
   suspension, an underdamped process loop) in the second-order section.
3. **Rigor (T4).** (a) Ch 3 §3.2: add the Laplace integral definition
   `\mathcal{L}\{f\}(s)=\int_0^\infty f(t)e^{-st}\dd t` before the derivative
   property (p22). (b) Ch 2 phasor section: derive `x(t)=\sqrt2\,\Re\{X e^{jωt}\}`
   from Euler, and state explicitly that `X` is the complex phasor
   (RMS magnitude ∠ phase) (p18).
4. **Cross-references (T5).** Ch 2 refresher points forward to `\cref{ch:ac}` for
   impedance; wherever a result is used before it's derived, add a `\cref`.
5. **Symbols table (T1).** Complete §1.1 (Study Guide): add Q, ζ, X, Z, Z₀, Γ,
   VF, β, ℓ, N_p/N_s, α, ω₀, ω_d, s. Keep the "exam-essential vs book-context"
   note. Audit against symbols actually used.
6. **Content clarifications.**
   - Study-guide `BW≈f₀/Q`: annotate "Q = the resonant circuit's loaded quality
     factor (= Q_s for series RLC)" (p14).
   - Oscillator/imaginary-axis wording (p14): tighten the marginal-stability phrase.
   - RL schematic (p44): add a sentence that the output is taken across R
     (`v_o=v_R`), low-pass in the current sense; across L gives high-pass.
   - Matching worked example (p58): add an explicit "Problem:" statement.
7. **Op-amp model (T7, p60/p63).** In §Op-Amp Ideals: the op-amp is modeled as a
   voltage-controlled voltage source (dependent source) with large open-loop gain
   A(s), very high input and very low output impedance — NOT an L/C element.
8. **Filter-types → table (p53).** Convert the §12.2 description list to a table.
9. **Provenance/personalization (D3).** Rewrite the preface personal paragraph
   (draft below), mention ChatGPT + Claude Code, reconcile Bibliography [3]. Apply
   title edits (S1–S3).
10. **"must agree" → "offer complementary intuition" (S5).** `grep -rn "must
    agree"` and reword all occurrences (ch 7 four-views, preface, etc.); keep the
    four-views framing itself.

## PHASE 3 — Figures (all must-haves)

New Python figures (`figures/src/*.py`, book palette via `_style.py`):
- **`phasor_unit_circle.py`** — rotating phasor on the unit circle; polar (r∠θ) ↔
  rectangular (a+jb); projection → `x(t)=√2 Re{X e^{jωt}}`. (Ch 2)
- **`opamp_gbw_bode.py`** — single-pole op-amp open-loop vs closed-loop Bode for a
  few β; shows gain–bandwidth product / pole sliding left. (Ch 13)
- **`opamp_rootlocus.py`** — root locus of a 2-pole amplifier as loop gain
  increases; poles approach and cross the jω axis (instability / oscillation). (Ch 13)
- **`oscillator_loopgain.py`** — loop-gain Bode (|L|=1 at ∠L=−180°) and/or the
  pole pair reaching the jω axis (Barkhausen). (Ch 13)
- **`smith_chart_antenna.py`** — hand-built Smith grid (constant-R circles,
  constant-X arcs) with Γ(f) locus for an idealized antenna model
  (series R_rad + jX(f), e.g. a resonant dipole model); no external deps
  (matplotlib only). Text shows the antenna model and ties the chart to the math
  and to a NanoVNA sweep. (Ch 14)
Fix existing figures (text overlap / additions):
- `rc_transient.py`, `rl_transient.py` — move the 63.2%/36.8% annotations clear of
  the curves and legend (p41, p45).
- `bode_first_order_highpass.py` — move the "+45° at ω_c" annotation off the curve
  (p42).
- `poles_zeros_notch.py` — add the `|s|=ω₀` circle (p31).
Schematics (circuitikz, in-text):
- π/T-network schematic (Ch 12, p57).
- Transformer schematic (Ch 12, p58).
- L-network: draw R_lo and R_hi as resistor symbols (Ch 12, p58).
- RL schematic: label/confirm `v_o` across R (Ch 9, p44).
Render-check every one.

## PHASE 4 — Read-through passes (consistency)
- Rebuild; require 0 undefined refs and 0 overfull >20pt.
- Cross-reference audit (new `ch:ac`; moved figures; `ch:splane`/`ch:bode`).
- Terminology: "LTI system" usage; "Study Guide" everywhere; no stray "must
  agree"; four-views framing consistent; symbols-table-vs-used audit.
- Visual render pass over all new/changed figures + schematics.
- Dispatch an end-to-end flow reviewer; apply findings.

---

# DRAFTS (for Alex to correct — personal details need confirmation)

**Title block (proposed):**
- Title: *Circuit Theory for the Amateur Extra Exam*
- Subtitle: *A Dynamical Systems and Control Perspective for Engineers*
- Author: *Alexander Dowling (KE9FZD)*

**Preface personal paragraph (DRAFT — Alex to edit/confirm):**
> I am a chemical engineering professor at the University of Notre Dame, with a
> research and teaching background in process systems engineering and control. I
> recently earned my General ham radio license and am studying for the Amateur
> Extra exam. Rather than memorize the circuit questions, I wanted to *understand*
> them—to see each radio circuit as a dynamical system I could write down, analyze
> in state space, and read in the frequency domain, the way I teach control. This
> book is the study companion I wished I had. It was drafted with ChatGPT and then
> developed, corrected, and typeset iteratively with Claude Code, with me steering
> the pedagogy and checking the engineering throughout.

*(Open confirmations for Alex: exact wording/among of the above; how candid on the
AI tooling; whether to name Notre Dame; and reconciling Bibliography [3], which
still calls the Word draft the "primary source.")*
