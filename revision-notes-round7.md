# Revision Notes — Round 7 (annotated September 2, 2026 build)

## Scope, source, and transcription conventions

Source: `/Users/adowling/Downloads/main_Sept_2_2026.pdf`, a 227-page PDF created
September 4, 2026. This is a **verbatim-first working transcription** of the
flattened handwriting. It is intentionally not a revision plan and it records
uncertainty rather than resolving it.

- Detailed annotations run from PDF pp. 2–86. The author explicitly wrote
  **“left off here”** on PDF p. 86 (printed p. 70, Chapter 12 opening).
  PDF pp. 87–227 were visually inspected and contain no handwritten markup.
- Printed/book page numbers are given where present. In the body, PDF page = book
  page + 16. Front-matter pages use their printed Roman number.
- `~~struck~~` denotes visible cancellation; square brackets preserve uncertain
  readings, e.g. `[?]`.
- Ink color is recorded only as an aid for locating the mark; no consistent
  semantic meaning is assumed.
- “Action” is the smallest defensible interpretation, **not** an instruction to
  make the change. Every status is `pending` until a later editing pass.

## Open transcription questions raised while parsing

1. **OQ-T1 — Preface, PDF p. 2.** Several overlapping blue/red/green annotations
   around the process-control paragraph are only partly legible. The clearest
   portions are `and be open to models e.g. ... optimization`, `we focus on`,
   and `frequency domain`; the exact replacement sentence and the word following
   “e.g.” are uncertain.
2. **OQ-T2 — Figure 4.1, PDF p. 40 / book p. 24.** Magenta margin text is partly
   obscured by the figure. It clearly asks for an additional visual/explanation
   connecting the Bode asymptotes, but its exact wording is uncertain.
3. **OQ-T3 — Figure 5.3, PDF p. 50 / book p. 34.** Multiple annotations identify
   clarity and visual problems. The circled labels and arrows are clear; a few
   longer phrases are transcribed with `[?]` rather than inferred.
4. **OQ-T4 — PDF pp. 56–84.** A number of marginal questions are readable only as
   a request to explain, move, or add a figure. They are preserved as such; their
   exact intended scope (local expansion versus reorganization) needs author
   confirmation before implementation.

---

## Front matter

### Preface — PDF p. 2 (printed i); `frontmatter/preface.tex`

- [ ] **R7-001** — *Ink: blue.* Location: opening sentence, “from a
  ~~chemical engineer’s~~ control perspective.” Verbatim insertion: **“theory”**
  with an arrow to the phrase. Action: revise the framing to foreground circuit/
  control theory rather than the author’s occupation. Status: applied — the
  opening now says “control-theory perspective.”
- [ ] **R7-002** — *Ink: blue/red/green; ambiguous.* Location: process-control
  paragraph. Verbatim readable portions: **“and be open to [models?] e.g.
  [github.io?] optimization”**, **“we focus on”**, and **“frequency domain”**;
  a red note begins **“In place of”**. Action: author decision; do not infer
  replacement prose. Status: resolved by author direction — the paragraph now links
  the named process-controls course, retains the state-space/nonlinear/optimization
  contrast, and explains why AC circuits make the frequency-domain view natural.
- [ ] **R7-003** — *Ink: green.* Location: AI-assistance sentence. Insertion:
  **“and Codex”** after “Claude Code.” Action: acknowledge Codex alongside
  Claude Code. Status: applied — Codex is now named alongside Claude Code.
- [ ] **R7-004** — *Ink: violet.* Location: final scope paragraph, bracketed list.
  Verbatim: **“Extra exam!”** Action: reconsider whether the long list exceeds
  the claimed circuit-theory scope; target is ambiguous. Status: resolved by author
  direction — the scope is now explicitly framed as the circuit-theory portion of
  the Extra exam syllabus.

### Preface — PDF p. 3 (printed ii); `frontmatter/preface.tex`

- [ ] **R7-005** — *Ink: green.* Location: source/disclaimer paragraph. Strike:
  **“A word on sources.”** Action: remove the throat-clearing lead-in. Status:
  applied — the paragraph now begins directly with the pool statement.
- [ ] **R7-006** — *Ink: orange.* Margin note with arrow to citation sequence:
  **“update citation order”**. Action: renumber/order citations after prose
  changes. Status: reviewed — the citations now follow the source dependency in
  the prose (official pool, machine-readable reprint, then supplementary texts).
  Numeric bibliography labels remain alphabetized by the book-wide `plain` style;
  changing that style would be a book-wide design decision rather than a local
  markup correction.

## Chapter 1 — Study Guide

### PDF p. 21 (book p. 5), §1.4; `chapters/01_study_guide.tex`

- [ ] **R7-007** — *Ink: violet/blue/red.* Beside the time-constant and resonance
  summary: **“first order (RC, RL)”** and **“second order (LC)”**; blue question:
  **“Is this correct? Or is there a mistake in my understanding?”** Red question:
  **“What type of circuits are these for?”** Action: technically audit the
  classification and name the circuit/model assumptions. Status: applied — the
  study guide now identifies RC and RL as first-order ideal single-storage-element
  models, gives the series-RLC context for the displayed \(Q_s\), and states that
  the reusable bandwidth relation applies to series or parallel RLC only with the
  appropriate topology-specific \(Q\).

## Chapter 2 — Complex Numbers and Phasors

### PDF p. 28 (book p. 12), §2.3.1; `chapters/02_complex_numbers_and_phasors.tex`

- [ ] **R7-008** — *Ink: green.* Circle around “Read the right-hand form”; note:
  **“what does this mean?”** Action: replace the vague directional instruction
  with a direct statement of the RMS expression. Status: applied — the prose now
  states the physical meaning of the right-hand power form.
- [ ] **R7-009** — *Ink: violet/orange.* Arrow from physical-insight box and note:
  **“an inexpensive [meter?]”**; strike **“computable rather than mysterious”**
  and insert **“predictable.”** Action: make the meter explanation more concrete
  and use “predictable” if the rewrite retains that claim. Status: applied — the
  meter is already identified as inexpensive; “predictable” replaces the rhetorical
  contrast.

### PDF p. 29 (book p. 13), §2.3.1 / Figure 2.1; `chapters/02_complex_numbers_and_phasors.tex`, `figures/src/phasor_unit_circle.py`

- [ ] **R7-010** — *Ink: green.* Worked example: strike “a heater dissipates
  according to the RMS value”; note **“redundant with above.”** Action: delete
  repetition already established in the preceding explanation. Status: applied —
  the repeated heater/RMS sentence was removed.
- [ ] **R7-011** — *Ink: green.* Figure 2.1: small mark at left/right waveform
  labels; no readable sentence. Action: inspect label placement/readability;
  record as a figure audit item. Status: reviewed — the figure is readable at
  final size and has no overlap or ambiguous label placement; the audit records a
  non-blocking greyscale refinement for any future redraw.

### PDF p. 30 (book p. 14), §2.3.2; `chapters/02_complex_numbers_and_phasors.tex`

- [ ] **R7-012** — *Ink: green.* Strike: **“That is the whole reason phasors earn
  their keep, and it is the machinery”**; insertion **“phasors.”** Action: reduce
  the sentence to the specific connection to Chapter 9. Status: applied — the
  rhetorical phrasing was replaced with the direct Chapter 9 connection.

## Chapter 3 — Modeling LTI Systems

### PDF p. 31 (book p. 15), §3.1; `chapters/03_modeling_lti_systems.tex`

- [x] **R7-013** — *Ink: red.* In the sentence after the four-view list, replace
  visible verbs: **“builds” → “explains”** and **“takes up” → “considers.”**
  Action: adopt the indicated more precise verbs. Status: applied — the revised
  sentence uses the requested verbs without changing the chapter's scope.
- [x] **R7-014** — *Ink: red.* Physical Insight box: strike “not a claim about
  reality” and “Fluency is being able to start from whichever one you are handed.”
  Insertion: **“Each modeling perspective helps develop a different intuition.”**
  Action: rewrite the box around complementary intuitions rather than abstract
  coordinate rhetoric. Status: applied — the box now opens with the insertion and
  gives each representation a concrete explanatory role.

### PDF p. 32 (book p. 16), §3.2; `chapters/03_modeling_lti_systems.tex`

- [x] **R7-015** — *Ink: green/red/violet.* Strike the generic claim that the
  following two sections “do exactly this” and related Part III bridge. Insert:
  **“This also helps us with circuit models for Part III.”** Violet comment:
  **“The following three rules, shown in Figure 3.1, are most helpful.”** Red
  bracket/question: **“This [??]”**. Action: simplify the bridge and explain why
  the three block-diagram rules matter before/with the figure. Status: applied
  (clear portions only) — the Part III bridge now names component laws and
  conservation equations, and the prose introduces the three rules as the
  combinations used throughout the book; the ambiguous red note was not acted on.

### PDF p. 33 (book p. 17), Figure 3.1 / Fourier box; `chapters/03_modeling_lti_systems.tex`

- [ ] **R7-016** — *Ink: blue/red.* Figure 3.1 caption is struck; blue note:
  **“This needs to be [a] better diagram.”** Red note: **“Make this a block
  diagram? The energy is hard to read.”** Action: redesign Figure 3.1 so its
  pedagogical purpose and the three rules are visually clear. Status: applied —
  Figure 3.1 is now a three-panel block diagram that separately shows cascade,
  parallel summation, and negative feedback, with the matching algebra adjacent
  to each topology. The rendered audit found its arrows, signs, and spacing clear.
- [ ] **R7-017** — *Ink: violet/orange/green.* Fourier/odd-harmonics Physical
  Insight: strike **“The transfer function sampled at the harmonics is the
  answer.”** Orange: **“Due to symmetry”** and **“bold”** beside the formula;
  green: **“remove or explain more clearly.”** Action: clarify or remove the
  square-wave symmetry derivation; do not retain a compressed assertion. Status:
  applied — the slogan was replaced with the explicit harmonic-by-harmonic
  procedure, while the square-wave result is derived from half-wave symmetry.

### PDF p. 35 (book p. 19), §3.6; `chapters/03_modeling_lti_systems.tex`

- [x] **R7-018** — *Ink: green.* At (Q=1/(2\zeta)), strike “information” and
  insert **“idea.”** Later note: **“represent the same idea”** beside text saying
  \(\zeta\) and \(Q\) are both used. Action: explain the conceptual relation
  more clearly and avoid the redundant “information” framing. Status: applied —
  the text now names damping and sharpness directly and bounds the equivalence to
  the stated standard second-order form.
- [x] **R7-019** — *Ink: green.* Strike “we read them in the time domain” and
  insert **“focus on.”** Action: use the more direct pedagogical framing. Status:
  applied — “focus on their time-domain behavior” replaces the passive phrasing.

### PDF p. 34 (book p. 18), §3.4; `chapters/03_modeling_lti_systems.tex`

- [ ] **R7-062** — *Ink: green.* In the lower Physical Insight box, strike the
  trailing phrase **“one number, two readings.”** Action: end the explanation
  after the direct physical/frequency-domain connection instead of adding a
  slogan-like summary. Status: applied — the box now ends with the direct
  time-domain/frequency-domain connection.

## Chapter 4 — Frequency Response, Bode, and the s-Plane

### PDF p. 39 (book p. 23), §§4.2–4.3.1; `chapters/04_s_plane_poles_and_zeros.tex`

- [x] **R7-020** — *Ink: blue.* Margin question next to §4.3: **“Where does this
  [come?] from?”** Action: provide a motivation/derivation for the first-order
  response before presenting it. Status: applied — §4.3 now states that the
  frequency response follows by substituting \(s=\jj\omega\) into the
  Chapter 3 transfer function.
- [x] **R7-021** — *Ink: orange/green.* Margin note: **“[Need?] [this] [more]
  [clear] [explanation]”**; green: **“let’s add a third equation … for the
  corner.”** Action: make the asymptote derivation explicitly lead to the corner
  condition. Status: applied — the subsection now identifies the denominator
  factor whose limiting regimes create the asymptotes before deriving them.

### PDF p. 40 (book p. 24), Figure 4.1 / §4.4; `chapters/04_s_plane_poles_and_zeros.tex`, `figures/src/bode_first_order_lowpass.py`

- [ ] **R7-022** — *Ink: magenta/violet/blue.* Figure 4.1 is heavily annotated:
  **“Both asymptotes overlap?”**, **“These lines are the two equations on the
  previous page I suspect we remember”**, and an uncertain request about an
  additional visual / “first order linear system.” Action: redraw/reannotate the
  figure and integrate its equations with the preceding derivation. Status: open
  question (OQ-T2) for the unreadable phrase.
- [x] **R7-023** — *Ink: magenta.* §4.4 bullets, bracketed: **“where does this
  come from?”** Action: derive/justify pole/zero sketching rules rather than only
  list them. Status: applied — §4.4 now derives each pole contribution from the
  preceding first-order factor and identifies a zero as the inverse numerator
  case before the rules are listed.

### PDF p. 41 (book p. 25), Figure 4.2; `chapters/04_s_plane_poles_and_zeros.tex`, `figures/src/bode_second_order.py`

- [ ] **R7-024** — *Ink: magenta/red.* Figure comments: **“Should we add pole
  on? Is there a straight line?”** and **“How does this relate to the actual
  complex [??]?”** Action: add/clarify the pole interpretation and its relation
  to the actual complex-plane picture; precise final phrase is uncertain. Status:
  applied — the revised text and caption connect high \(Q\), low damping, the
  proximity of the pole pair to the imaginary axis, and the visible peak; the
  figure also now distinguishes its response curves without relying on colour.

### PDF p. 42 (book p. 26), §4.7.1; `chapters/04_s_plane_poles_and_zeros.tex`

- [ ] **R7-025** — *Ink: magenta.* Question by \(Q\) statement: **“Is it \(Q\)
  [??] at higher?”** Action: technical audit of the stated (Q)/damping
  relationship. Status: applied — the text now distinguishes the magnitude at
  \(\omega_0\), which equals \(Q\), from the true resonant maximum: the latter
  exists only for \(Q>1/\sqrt{2}\) and is approximately \(Q\) at high \(Q\).

### PDF p. 43 (book p. 27), Figure 4.3; `chapters/04_s_plane_poles_and_zeros.tex`, `figures/src/poles_second_order.py`

- [x] **R7-026** — *Ink: magenta/green/red.* Figure 4.3 notes: **“Which angle is
  \(\theta\)? It is ambiguous here.”**, **“Is \(\theta=45^\circ\) critically
  damped?”**, **“\(\zeta=1?\)”**, and **“remind me which \(\theta\) corresponds
  to critically damped.”** Action: make angle definitions, axis crossings, and
  critical-damping geometry unambiguous. Status: applied — the prose and caption
  now define the measurement direction, state the underdamped range, and identify
  \(\zeta=1\) as the limiting point at \(-\omega_0\).

### PDF p. 44 (book p. 28), Figure 4.4; `chapters/04_s_plane_poles_and_zeros.tex`, `figures/src/poles_zeros_notch.py`

- [ ] **R7-027** — *Ink: orange.* Arrow to Figure 4.4 / caption: **“What signifies
  [a?] lower [??] where [??] is [??]?”** Action: explain the visual meaning of
  pole/zero distance and the named response; exact question is not decipherable.
  Status: applied conservatively — the caption now identifies the pole pair as
  setting the resonance and the imaginary-axis zeros as forcing a null at the
  rejection frequency. No more specific interpretation was inferred from the
  unreadable words.

### PDF p. 45 (book p. 29), §4.9; `chapters/04_s_plane_poles_and_zeros.tex`

- [x] **R7-028** — *Ink: orange/green.* Strike: **“Nothing here is electrical—
  these are just numbers read off the standard second-order form.”** Green note:
  **“versus this.”** Action: remove the dismissive sentence and make the link to
  the Chapter 13 LC realization directly. Status: applied — the generic
  calculation now leads directly to the LC realization and the component roles.

## Chapter 5 — Feedback

### PDF p. 46 (book p. 30), §5.1; `chapters/05_feedback.tex`

- [x] **R7-029** — *Ink: red/orange/green.* Opening sentence: strike “So far”
  and “has treated systems open loop”; insertion **“consider open loop systems:”**.
  Orange bracket: **“show here under [??] response”**. Green: **“This would benefit
  from a circuit diagram.”** Action: use the direct opening and add a simple
  circuit/block diagram if the teaching question supports it. Status: applied
  (prose only) — the chapter now opens with the requested direct open-loop frame;
  the separate diagram request remains deferred for figure review.
- [x] **R7-030** — *Ink: green.* Strike most of the proportional-feedback
  explanation following “Because \(\beta\) here is a constant”; insertion begins
  **“[Let?]”**. Action: shorten/rebuild the paragraph; exact retained wording is
  ambiguous. Status: applied — the paragraph now defines P-only feedback as a
  constant feedback path without importing an unnecessary PID detour.

### PDF p. 47 (book p. 31), §§5.2–5.3; `chapters/05_feedback.tex`

- [x] **R7-031** — *Ink: green/violet/orange.* Strike “The first payoff needs no
  algebra beyond the boxed formula.” Violet: **“what does this mean? Can you
  elaborate?”** Green: **“show a block diagram.”** Orange questions: **“where is
  the bandwidth in this equation?”**, **“What is the DC gain? Is it \(A_0\) or
  \(A_0/(1+A_0\beta)\)?”** Red: **“How to show this with a picture?”** Action:
  add physical/visual explanation, define gains precisely, and make the
  bandwidth result visible. Status: applied (prose only) — loop gain is defined
  before use, the large-loop approximation is bounded by frequency, and the
  first-order derivation explicitly identifies DC gain, pole motion, time
  constant, and bandwidth; a new diagram remains deferred.
- [x] **R7-032** — *Ink: green.* Margin note: **“There are two key features of
  feedback of [??]. This, this [is] referring to Figure 5.1 (left)? We should
  explicitly reference figures in text.”** Action: explicitly tie claims to the
  relevant panel and clarify the two feedback effects. Status: applied — the text
  now names the left/right panels of \cref{fig:fb-first-order} as the pole-motion
  and step-response evidence.

### PDF p. 48 (book p. 32), Figure 5.1 / §5.4; `chapters/05_feedback.tex`, `figures/src/feedback_first_order.py`

- [x] **R7-033** — *Ink: red/magenta/green/violet.* Figure 5.1: **“what \(\beta\)
  and \(A_0\) are in this example”**; **“legend overlaps trends”**; strike
  “gain is traded for bandwidth”; green: **“why? There is a good math reason.
  Let’s elaborate.”** Action: repair legend overlap, identify parameters in the
  figure, and replace unsupported shorthand with an explanation. Status: applied
  (caption/prose only) — the caption identifies \(A_0\), \(\omega_a\), and the
  plotted \(\beta\) values, while the prose derives the paired DC-gain and
  time-constant changes; legend repair is deferred to figure review.
- [x] **R7-034** — *Ink: violet/green/magenta.* Physical Insight asks: **“But PI
  can oscillate, correct, because it stores energy [in the controller?]?”**;
  green: **“where is this defined? What does ‘DC’ mean in this context?”**;
  magenta: **“Are we missing \(A_{cl}\) for the second order system w/ P
  feedback?”** Action: qualify the idealized claim and add/verify missing
  closed-loop expression/definitions. Status: applied — DC gain is defined as
  zero-frequency gain, the second-order \(A_{\mathrm{cl}}\) is displayed, and the
  PI-controller caveat distinguishes added controller dynamics from the constant-
  \(\beta\) model.

### PDF pp. 49–51 (book pp. 33–35), §§5.5–5.6 / Figures 5.2–5.4; `chapters/05_feedback.tex`, `figures/src/feedback_second_order.py`, `figures/src/nyquist_margins.py`, `figures/src/feedback_margins.py`

- [x] **R7-035** — *Ink: violet/green/orange.* At frequency-view setup: **“If we
  draw a block diagram, where is \(L(s)\)?”**; green: **“shorten, more concise”**;
  orange: **“what do we mean by ‘lag’? We have not discussed delay models yet.”**
  Action: locate loop gain in a diagram, compress prose, and define/avoid “lag”
  until it is established. Status: applied (prose only) — the frequency view now
  names \(L(\jj\omega)\) as the plotted loop gain and defines extra phase lag as
  an additional negative phase shift; a new block diagram remains deferred.
- [x] **R7-036** — *Ink: magenta/blue.* Nyquist page notes: **“curve of what?”**,
  **“more so [we?] [??] [example]”**, **“need to [explain] the [??] [on] Figure
  [??]”**, **“move around [??]”**, and **“let’s simplify this. Drop the discussion
  that is not needed (full Nyquist criterion) and instead focus on Ch. 6 + 17.”**
  Action: simplify Nyquist coverage; label its object/curve and retain only the
  content needed for the later stability chapters. Status: applied — Nyquist now
  identifies its curve as \(L(\jj\omega)\), retains the geometric relation to
  Bode margins, and removes the full-criterion detour in favor of forward links
  to \cref{ch:highorder,ch:active}; unreadable fragments remain unacted on.
- [x] **R7-037** — *Ink: blue/violet/green.* Figure 5.4: **“same concept. let’s
  label (a),(b),(c)… points of interest on these figures then refer to the points
  in the explanation”**; **“This should be easier? it is referred to [the]
  Nyquist plot”**; green: **“Many ideal circuits are LTI systems?”** Action:
  label panels and points, coordinate Figure 5.3/5.4 explanations, and qualify
  the LTI statement. Status: applied differently — existing figure sources were
  left unchanged, but the caption names the upper/lower Bode panels, the Nyquist
  prose links the two figures, and the radio bridge now states the LTI and
  feedback-path assumptions.

### PDF p. 52 (book p. 36), §5.6; `chapters/05_feedback.tex`

- [x] **R7-038** — *Ink: green.* Strike/replace “Feedback is the thread tying
  op-amps, active filters, oscillators, and regulators together, and Chapter 17
  pulls it…” with **“is used in [Chapter 17]”**. Action: remove the rhetorical
  “thread tying” construction and state the downstream use plainly. Status:
  applied — the conclusion now states that \cref{ch:active} uses the feedback
  ideas in its named circuit applications.

## Chapter 6 — Higher-Order Systems

### PDF p. 53 (book p. 37), §§6.1–6.2; `chapters/06_higher_order.tex`

- [x] **R7-039** — *Ink: green.* Title/intro: **“Chapters — and — [reconsider]”**;
  strike redundant Chapter 3 restatement; note **“This is [??]”** by real
  coefficients. Action: reconsider title and reduce repetition; exact marginal
  phrase uncertain. Status: resolved in Round 7: simplified the title and intro and
  clarified the real-coefficient statement.

### PDF pp. 54–56 (book pp. 38–40), §§6.2–6.6; `chapters/06_higher_order.tex`

- [x] **R7-040** — *Ink: green.* §6.2: strike “There is no third kind of building
  block, at any order”; note **“Understand?”** and strike/rewrite much of the
  Controls Connection. Action: reduce/unpack the abstraction and retain only a
  clear factorization insight. Status: resolved in Round 7: reduced the callout to
  the factorization and combined-pole interpretation.
- [x] **R7-041** — *Ink: green.* §6.3: **“This is simply [??]”** and **“But why
  -20 dB and why -90°? Let’s make sure that is explained earlier.”** Action:
  ensure the per-pole magnitude/phase rules are derived before they are summed.
  Status: resolved in Round 7: states the established one-pole magnitude/phase
  result before summing it across sections.
- [~] **R7-042** — *Ink: green/red/orange.* §6.4: **“Picture? This would help a
  lot.”**, **“unstable? Is anything missing from this [??]?”**, **“Picture please
  to show this argument.”** §6.5: **“Let’s elaborate on this. Show how delay in a
  first order system w/ feedback can destabilize it.”** Action: add a visual for
  the three-pole argument and develop the delay/feedback connection. Status:
  partially resolved in Round 7: bounded the three-lag argument to its feedback
  model and tightened the delay condition. The requested visual and a worked
  delay-feedback example remain deferred; the later structural split is recorded in
  R7-043 and R7-044.
- [ ] **R7-043** — *Ink: blue/red/orange.* §6.6 and table: **“Suggestion: focus
  this on pole placement for feed[back] systems.”**, **“once [??]”**, **“Show this
  in a [more] [??]”**, **“Then revisit this for (radio) filters.”**, **“Later
  chapters?”**, **“move to later chapters that focus on filters.”** Action:
  reorganize the filter-family/pole-placement material around the feedback
  objective or defer it to the filter chapter. Status: resolved by author direction
  — Chapter 6 retains the generic/feedback derivation; Chapter 15 now introduces the
  filter goals before the named-family pole-placement discussion.

### PDF p. 57 (book p. 41), §§6.8–6.9; `chapters/06_higher_order.tex`

- [ ] **R7-044** — *Ink: orange/red.* Bracketed §6.8 note: **“move to filter
  radio specific [section?]”**; red: **“Can this be presented from the perspective
  of a feed[back] system?”**; red by §6.9: **“This is great. Move it to later
  [chapter?].”** Orange: **“move to later in the book when we discuss this in the
  context of [??].”** Action: move group-delay and/or infinite-pole material to
  a later, motivated setting; the intended exact destination is open. Status:
  resolved by author direction — group delay moved to Chapter 15 as a filter-design
  trade-off; the infinite-pole limit remains in Chapter 6 as generic dynamic-system
  theory that leads into transmission lines.

## Chapter 7 — Circuit Modeling

### PDF p. 59 (book p. 43), §7.1; `chapters/07_circuit_modeling.tex`

- [x] **R7-045** — *Ink: orange/green.* At “fields distributed through space”:
  **“electrical and magnetic?”**; green: **“introduce lags, and thus [??]”**.
  Action: name the relevant fields and make the distributed-model/time-delay
  link explicit. Status: applied in `chapters/07_circuit_modeling.tex`; names
  electric and magnetic fields and connects the lumped approximation to
  negligible propagation delay on the signal time scale.

## Chapters 7–11 — Detailed markup inventory (PDF pp. 60–84)

The remaining annotations are fully visual-inspected below. Several are question
marks/strike-through-only rather than written sentences; those marks are preserved
as editorial or technical-audit requests rather than invented prose.

### PDF pp. 60–62 (book pp. 44–46), §§7.2–7.3; `chapters/07_circuit_modeling.tex`

- [ ] **R7-046** — *Ink: red/green.* Component-law and field-diffusion discussion:
  red questions include **“When/why [??] should this figure [??]?”** and **“Can
  we show this?”**; green asks to **“keep [??] because of the physics.”** Action:
  audit the field-diffusion derivation, identify the physical model first, and
  consider an explanatory figure. Status: deferred; the readable request is a
  technical/visual redesign decision outside the high-confidence prose pass.
- [x] **R7-047** — *Ink: green/orange.* §7.3: **“This is from some current or
  voltage?”** and a bracketed request to explain current/charge accumulation.
  Action: define the circuit context for KCL/charge accumulation before formulae.
  Status: applied in `chapters/07_circuit_modeling.tex`; grounds KCL in a small
  surface around a wire junction and gives the RC-branch current-balance example.

### PDF pp. 64–66 (book pp. 48–50), §§7.5–7.7 / Chapter 8 opening; `chapters/07_circuit_modeling.tex`, `chapters/08_series_parallel_networks.tex`

- [x] **R7-048** — *Ink: green.* Electrical-units section has markings around
  first-use definitions; a note asks **“[??]”** beside voltage/current notation.
  Action: check first-use definition and unit consistency. Status: applied in
  `chapters/07_circuit_modeling.tex`; defines \(q\), \(i\), \(v\), and \(p\) with
  their first-use units while retaining the audited SI discussion.
- [x] **R7-049** — *Ink: green.* Chapter 8 capacitor section: **“This [??] from
  [same?] circuit or [??]?”** Action: clarify the physical origin/assumption of
  series/parallel capacitor rules. Status: applied in
  `chapters/08_series_parallel_networks.tex`; states the ideal-network,
  floating-node, and shared-two-node assumptions behind the derivation.

### PDF pp. 67–69 (book pp. 51–53), §§8.4–8.7; `chapters/08_series_parallel_networks.tex`

- [x] **R7-050** — *Ink: blue.* Voltage-divider page: **“I do not like this and
  want to [??]”**, **“The circuit is [??]”**, **“explain [??] @ [??]”**.
  **Status:** resolved conservatively (2026-09-05). The divider now foregrounds
  the grounded reference node, output node, and unloaded assumption; the later
  Thévenin worked example covers the loaded-divider case.
- [x] **R7-051** — *Ink: blue/red.* Worked example: blue **“Where did this mean?”**
  beside a step and red **“What does this mean?”**. Action: explain the omitted
  algebra/topology step. Status: applied in
  `chapters/08_series_parallel_networks.tex`; distinguishes the live divider
  circuit from the source-deactivated circuit used to calculate \(R_{Th}\).

### PDF pp. 71–76 (book pp. 55–60), §§9.1–9.8; `chapters/09_ac_steady_state.tex`

- [x] **R7-052** — *Ink: red/blue/green.* §9.1–9.2: comments ask **“What is the
  [??] that …?”**, **“This is a [??] of / model?”**, and mark several formulae.
  Action: re-derive impedance/admittance statements and make the current/voltage
  relationship and circuit geometry explicit. Status: resolved — defined a two-terminal
  one-port, stated the passive sign convention, and tied \(V=ZI\)/\(I=YV\) to
  series/parallel geometry.
- [x] **R7-053** — *Ink: green.* Complex-power section: **“[What?] [??] to
  represent current [??]”** plus arrows between formulas. Action: make the
  complex-power derivation and sign/conjugate convention explicit. Status:
  resolved — derived \(VI^*\) from RMS phasor angles and stated absorbed-power,
  reactive-power, and reference-current signs.
- [x] **R7-054** — *Ink: green.* Around average/PEP power: marks distinguish
  **“[average?] vs [peak?]”** and point at an equation. Action: audit and clearly
  distinguish average, peak, and PEP quantities. Status: resolved — distinguished
  instantaneous power, RF-cycle average, whole-transmission average, and PEP; scoped
  the RMS/\(V_{pp}\) formulas to a resistive sinusoidal RF cycle.

### PDF pp. 77–78 (book pp. 61–62), Chapter 10; `chapters/10_one_circuit_four_views.tex`

- [x] **R7-055** — *Ink: red/green.* Chapter opening: red request **“For Part III
  [??]”** and a bracketed note; green asks whether an **“[example?] … system”** is
  needed. Action: clarify the chapter’s role as the bridge from generic models to
  circuits, and consider a visual/system example. Status: resolved in Round 7:
  identifies the chapter as the textual bridge from circuit laws to generic
  dynamics; no additional visual was required.
- [x] **R7-056** — *Ink: red/blue.* §10.3 table: comments point to definitions and
  ask for a **“higher-order system such as [??]”**. Action: specify the mapping
  between circuit topology and generic system order. Status: resolved in Round 7:
  states that independent capacitor voltages and inductor currents set the order,
  and bounds the higher-order/distributed extensions.

### PDF pp. 79–84 (book pp. 63–68), Chapter 11 RC circuits; `chapters/11_rc_circuits.tex`, `figures/src/rc_transient.py`, `figures/src/rc_worked.py`, `figures/src/bode_first_order_highpass.py`

- [x] **R7-057** — *Ink: blue/red/green.* RC schematic page: blue note points to
  the circuit and asks for a definition/interpretation; red/green notes request
  that the circuit relationship be tied to the derivation. Action: ensure the
  schematic, state variable, sign convention, and differential equation are
  introduced in that order. Status: resolved in Round 7: the schematic is followed
  by the state, its reference directions/passive sign convention, and then KVL and
  the ODE.
- [~] **R7-058** — *Ink: orange/green.* RC plots: arrows/notes request **“move
  down”** and label the key curve/point; green marking identifies a formula.
  Action: audit plot annotation placement and explain the plotted RC time-
  constant/frequency relation. Status: partially resolved in Round 7: captions
  now identify \(t/\tau\), \(\omega_c=1/\tau\), and \(f_c=1/(2\pi\tau)\). The
  ambiguous requested annotation move was not made.
- [x] **R7-059** — *Ink: green.* At the pole/root-locus explanation: strike or
  bracketed phrase with a note toward the pole diagram. Action: tighten the
  explanation and ensure the root-locus graphic has an explicit teaching role.
  Status: resolved in Round 7: the text now introduces the root locus as the
  geometric plot of \(s=-1/\tau\), and the caption names the \(s\)-plane role.
- [~] **R7-060** — *Ink: green.* Figure 11.3 Bode/root-locus page: **“move [??]
  but this figure”**, with arrows to the plots. Action: revise the plot’s layout,
  labels, and equation-to-figure narrative. Status: partially resolved in Round 7:
  the worked-example caption connects its Bode corner and root locus explicitly to
  \(\tau\) and \(s=-1/\tau\). The unclear layout/label request was deferred, so no
  figure source was changed.

## Boundary mark

### PDF p. 86 (book p. 70), Chapter 12 opening; `chapters/12_rl_circuits.tex`

- [ ] **R7-061** — *Ink: blue.* At the Chapter 12 title page, verbatim: **“left
  off here.”** Action: none. This records the end of the author’s detailed
  read-through. Status: informational.

## Pages inspected without handwriting

All pages not named above, including PDF pp. 1, 4–20, 22–27, 36, 38,
58, 63, 70, 79–80, 85, and **87–227**, were inspected visually. Aside from
printed text/figures and the end-of-reading mark on p. 86, no handwritten
annotations were found on the latter range.
