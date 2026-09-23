# Revision Notes — Round 3 (from "main 3.pdf" markup, 2026-07-27)

Parsed from Alex's marked-up PDF of the 92-page build (book pages 1–82).
He read **front matter through Chapter 12** in detail; Ch 13+ has no annotations.
Ink colors group related passes (blue/red/green are separate read-throughs).

Page numbers below are **book** pages (PDF page = book page + 10).

---

## 0. BIG STRUCTURAL QUESTIONS RAISED (need decisions)

- **B1 — Chapter 3 identity crisis (p12).** Title "First- and Second-Order
  Systems: Time and State Space" has "Time and State Space" struck, with blue
  "Modeling" written in. Red: *"If this chapter is all about state space, why are
  we examining Laplace transformations?"* and *"This chapter appears to mix state
  space and frequency domain. Rename the chapter?"*
- **B2 — NEW Chapter on feedback (p23, red, prominent).** *"Suggestion: What about
  a Chapter 5 that looks at feedback from both the state space and frequency
  domain perspectives?"* Related: p17 red *"should this be later?"* against §3.5
  (Feedback: Open Loop to Closed Loop) and the "Foreshadowing op-amps" box.
- **B3 — Split Chapter 11 (p45, red).** *"Should we split this into two chapters —
  Series RLC and Parallel RLC?"*
- **B4 — Chapter 12 redundancy (p49, red).** *"Can this chapter get simplified if
  the previous chapters are more precise and more thorough?"* Reinforced by p50
  green/orange *"move to previous chapters?"* on both §12.3.1 (RC low-pass
  first-principles) and §12.3.2 (LC low-pass first-principles).
- **B5 — Worked-example formatting policy (p34, p35).** p35 red: *"Why is this a
  dedicated subsection, but the previous worked example is a subsub section."*
  p34 green: *"What if we add a new callout box for worked examples? That way, we
  do not need a subsection."*
- **B6 — Specific (non-generic) plots for each worked example.** Recurring across
  Ch 9, 10, 11: he wants Bode + root-locus plots *for the specific numeric
  system* in each worked example, not just pointers to the generic Part II
  figures. See W-p41, W-p44, W-p48.

---

## 1. Front matter

### Preface (p2)
- [ ] **F1** "A personal note on where this came from" → **"My** personal note…"
- [ ] **F2** Delete "**and control**" from "process systems engineering and control".
- [ ] **F3** "…and **read in** the frequency domain, **the way I teach control**."
  → "…and **understood in** the frequency domain." (delete "the way I teach control")
- [ ] **F4** "This book is **the** study companion I wished I had" → "**a** study
  companion" (article struck).
- [ ] **F5** "with me steering the pedagogy and **checking the engineering
  throughout**" → "…and **critiquing the text**."

### How to Use This Book (p3)
- [ ] **F6** Part I: "…this part (with the practice in Part IV) **is** enough."
  → "**should be** enough."
- [ ] **F7** Part II: delete "Read this if you want to *understand* rather than
  memorize." → replace with "Read this if you **are rusty on control theory**."
- [ ] **F8** Part III: "This is where the understanding **pays off**." → "This is
  where the **dynamical systems** understanding **(hopefully) happens**."
- [ ] **F9** Delete "The engineering path is to read Part II, then Part III."
- [ ] **F10** (Red "love" beside the 6-step recipe list — **keep as is**, he likes it.)

---

## 2. Chapter 1 — Study Guide

- [ ] **C1-p2** "This chapter is the print-and-review **version**" → **"summary"**.

---

## 3. Chapter 2 — Complex Numbers and Phasors

- [ ] **C2-p9** Opening: "The circuit-specific **payoff**—impedance, admittance,
  and complex power—waits until Chapter 7 ~~once Part III has introduced the
  components themselves~~." → **"connections"** replaces "payoff"; delete the
  trailing clause; end sentence at "Chapter 7."
- [ ] **C2-p9** Red "**Remember!**" beside §2.1.1's closing line *"Use rectangular
  form to add, polar form to multiply."* → **emphasize this** (promote to a
  callout / bold takeaway).
- [ ] **C2-p10** "so that the shared \(\cos\omega t\) can ~~be carried along
  silently~~ **be captured**instead of written out everywhere."
- [ ] **C2-p10 (figure, blue) — FIX OVERLAP in Figure 2.1.** Two ellipses on the
  right panel: the "value at t=0: √2|X|cos φ" label and the "× e^{jωt}: rotate at
  ω (one turn per period)" label both collide with the sinusoid / axis frame.
- [ ] **C2-p10 (figure, red) — θ vs φ inconsistency.** Red mark on the left panel
  title \(X=r\angle\theta=a+\jj b\) and red note: *"Why distinguish between θ and
  φ here?"* → **use ONE symbol** for the phasor angle throughout figure + text.
- [ ] **C2-p10** Red: *"Check that this is defined on first use"* with **RMS**
  circled → make sure RMS is spelled out/defined at its true first use.

---

## 4. Chapter 3 — First- and Second-Order Systems (retitle: see B1)

- [ ] **C3-p12** Title: strike "Time and State Space"; blue insertion
  "**Modeling**". Red: chapter mixes state space and frequency domain — rename
  and/or move the Laplace material. (**B1**)
- [ ] **C3-p13** §3.2: "three of its properties ~~carry the whole load~~ **are
  most useful**".
- [ ] **C3-p13** Green labels + bracket "**move to below**": the two
  ODE→transfer-function lines should be labeled "**First-order LTI:**" and
  "**Second-order LTI:**" and **moved down** into §3.3 (first-order) and §3.4
  (second-order) respectively.
- [ ] **C3-p13** "once they have written a circuit's differential equation from
  ~~KVL and KCL~~ **fundamentals of physics**."
- [ ] **C3-p13** Blue: *"Need to sync the text with the figure"* (block diagrams).
- [ ] **C3-p13** Red: *"I was expecting to see all of these rules in the figure"*
  → **Figure 3.1 must show all three rules**: cascade (multiply), **parallel
  (add — currently missing)**, and feedback.
- [ ] **C3-p14** Green: *"Show ℒ transform here"* → put the first-order
  Laplace/transfer-function derivation in §3.3. (pairs with C3-p13 move)
- [ ] **C3-p14** First-order examples bullet: strike "(electrical)" and the tail
  "—one example among many, not the definition"; red insert "**an ideal**" →
  "**an ideal** capacitor charging through a resistor, \(\tau=RC\)".
- [ ] **C3-p15** Physical Insight: "so it can never overshoot **or ring**" —
  "or ring" circled, red: *"oscillate? or is 'ring' the proper term in controls?"*
  → **settle the terminology** (ring vs oscillate) and use consistently.
- [ ] **C3-p15** Red: *"Let's define Q here"* at the ζ definition in §3.4.
- [ ] **C3-p15** Green: *"move Laplace transform to here"* (second-order case → §3.4).
- [ ] **C3-p15** Second-order examples bullet: strike "(electrically) the LC or
  RLC resonator of Part III." → green "**a resonant circuit with an inductor and
  capacitor**".
- [ ] **C3-p15** Blue bracket on the "ζ, Q, and the damping regimes" Controls
  Connection box: *"either delete this or explain it here"*.
- [ ] **C3-p16** Red: *"pull out into main text above"* → move the sentence
  "Radio work usually states the same information as the *quality factor*
  \(Q=1/(2\zeta)\)…" **out of the callout box into the main text** (satisfies
  "define Q here").
- [ ] **C3-p16** Green "**low Q**" pointing at the ζ=2 (overdamped) legend entry
  → **label high-ζ curves as low Q** in the legend/annotation of Figure 3.3.
- [ ] **C3-p17** §3.5 Feedback — blue bracket: *"Is this a proportional feedback?
  If yes, let's say that and analyze it."*
- [ ] **C3-p17** Green: *"Does proportional feedback for a first order LTI result
  in a second order LTI (closed loop)?"* → **answer this explicitly** (no: a
  single pole stays first order; it just moves).
- [ ] **C3-p17** Red: *"should this be later?"* against §3.5 and the
  "Foreshadowing op-amps" box → candidate for the new feedback chapter (**B2**).

---

## 5. Chapter 4 — Frequency Response, Bode, and the s-Plane

- [ ] **C4-p18** Red circle on "20 dB/decade ≈ 6 dB/octave": *"perhaps have a
  subsection on just dB calculations"* → **add a dedicated decibel subsection**.
- [ ] **C4-p18** Blue circle on "**rolls off at**": *"I am not familiar with this
  language"* → define "roll-off" on first use.
- [ ] **C4-p19** Green circle on the "corner ω_c: −3.01 dB" annotation: *"Why this
  number? Where did it come from?"* → **show that −3.01 dB = 20 log₁₀(1/√2)**.
- [ ] **C4-p19** Blue: *"Why is there a discrepancy?"* (exact curve vs asymptotes
  at the corner) → explain the 3 dB gap explicitly.
- [ ] **C4-p19** Blue bracket on the asymptote bullet list: *"Can we derive the
  asymptotes?"* → **derive** the low-/high-frequency asymptotes.
- [ ] **C4-p19** Red at §4.4: *"Show transfer function for a second order system
  again"* → restate \(G(s)=\omega_0^2/(s^2+2\zeta\omega_0 s+\omega_0^2)\) there.
- [ ] **C4-p20** Red at §4.6 "The Bode plot samples G(s) on the imaginary axis":
  insert "**(sine wave input)**" → make the jω ↔ sinusoidal-input link explicit.
- [ ] **C4-p23** Red (big): **new feedback chapter suggestion** (**B2**).

---

## 6. Chapter 5 — Circuit Modeling: Paradigms and Components

- [ ] **C5-p25** Strike "Part II built a generic linear-systems toolkit ~~with no
  mention of wires~~."
- [ ] **C5-p25** "Everything here is the vocabulary the later chapters
  ~~assume~~ **use**."
- [ ] **C5-p25** "This is ~~legal~~ **reasonable** whenever the circuit is small
  compared with the wavelength…"
- [ ] **C5-p26** Add abbreviations at first use: "Kirchhoff's current law
  **(KCL)**" (§5.3) and "Kirchhoff's voltage law **(KVL)**" (§5.4).
- [ ] **C5-p27** Blue: *"What is 1 A in SI units?"* → note that the **ampere is an
  SI base unit** (and 1 C = 1 A·s follows), i.e. don't imply A is derived.
- [ ] **C5-p28** **Merge §5.7 "Key Equations" + §5.8 "Key Definitions"** into one
  section titled "**Summary: Key Equations and Definitions**".

---

## 7. Chapter 6 — Resistive Networks

- [ ] **C6-p31** Blue: *"What about capacitors in series or parallel?"*
- [ ] **C6-p31** Blue: *"What about inductors in series or parallel?"*
- [ ] **C6-p31** Blue: *"This might have been on the general exam. Good to review
  here in the spirit of assuming no circuits background."*
  → **Add series/parallel combination rules for C and L** (with the note that
  capacitors combine "backwards" relative to resistors).

---

## 8. Chapter 7 — AC Steady State: Impedance, Admittance, and Power

- [ ] **C7-p32** "Recall the ~~payoff~~ **main ideas** of Chapter 2".
- [ ] **C7-p32** Red bracket at \(Z=V/I=R+\jj X\): *"show derivation more
  clearly"*.
- [ ] **C7-p32** Red at \(Z_C=1/(\jj\omega C)\): *"why 1/jω here?"* → show the
  step from \(i=C\,\dd v/\dd t \Rightarrow I=\jj\omega C V\Rightarrow Z_C=V/I\).
- [ ] **C7-p33** Red circle on "**inertance**": *"Is this a real word?"*
  → keep-but-gloss, or replace with "fluid inertia".
- [ ] **C7-p33** Green on §7.2 title "Series and Parallel: Where the RLC Impedance
  Comes From": *"Drop from this subsection title?"* + *"What about parallel? That
  is not discussed."* → **retitle** (drop "and Parallel", since parallel is §7.3)
  **or** actually cover parallel here.
- [ ] **C7-p34** Blue: *"draw picture"* at §7.3.1 (parallel-branch worked example)
  → add a schematic.
- [ ] **C7-p34** Blue (margin, §7.4 Phasor Lead and Lag): *"This falls out of
  differential equations. Show this more clearly. If earlier, add a reference."*
- [ ] **C7-p34** Green: *"Show this with two worked examples"* (lead and lag).
- [ ] **C7-p34** Green: *"What if we add a new callout box for worked examples?
  That way, we do not need a subsection."* (**B5**)
- [ ] **C7-p35** Red at §7.6: *"Show a picture. Why is this a dedicated
  subsection, but the previous worked example is a subsub section."* (**B5**)

---

## 9. Chapter 8 — One Circuit, Four Views

- [ ] **C8-p36** Green near "the AC steady-state view—impedance and phasors—
  Chapter 7": insert "**(especially)**"-type qualifier (wording tweak).
- [ ] **C8-p36** Strike "The views are complementary ~~rather than competing~~".
- [ ] **C8-p36** **Delete the whole paragraph** "The generic systems of Chapter 3
  have no schematic, so there the four views are… entered through the wiring
  diagram." (blue "**Not needed**").
- [ ] **C8-p36** §8.2: "each apply the ~~same~~ **following** recipe to ~~a~~
  specific circuit**s** ~~and it is worth stating once so the pattern is
  visible~~:"
- [ ] **C8-p37** Delete "~~The circuit chapters that follow do exactly this, one
  circuit at a time.~~"

---

## 10. Chapter 9 — RC Circuits

- [ ] **C9-p38** Delete "~~This chapter walks the Part III recipe end to end.~~"
- [ ] **C9-p38** Blue, Figure 9.1 (\(v_o\) circled): *"What is \(v_o\)? Where is
  it defined?"* → **define the output variable** in text and figure.
- [ ] **C9-p39** Red at §9.3/§9.4: *"Should we instead show the transfer function
  too to make this pole more clear?"* → **add \(G(s)\)** alongside the
  state-space model.
- [ ] **C9-p39** Red at Figure 9.2: *"What about a plot of the resistor voltage?
  We are going to look at that below in frequency response."* → **add \(v_R(t)\)**
  to the transient figure (or a companion panel).
- [ ] **C9-p40** Green at §9.6: *"How are these transfer functions derived from
  the state space model? Let's state this more clearly."* → derive \(G_C\) and
  \(G_R\) from the state-space/ODE model.
- [ ] **C9-p40** Red at §9.7 heading: *"refer to Figure 9.4?"* → add the \cref.
- [ ] **C9-p41** Red circle on "(Figure 4.1)" in §9.9: *"Should we remake the Bode
  plot here? Or is the point the Bode plot in Chapter 4 is generic?"* (**B6**)
- [ ] **C9-p41** Blue: *"Show me the root locus plot. How does changing R change
  the dynamics?"* → **specific root-locus figure for the worked example**. (**B6**)

---

## 11. Chapter 10 — RL Circuits

- [ ] **C10-p42** Green bracket on the opening sentence: *"Where are RL circuits
  important? I agree inductors are important… where do they appear w/o a
  capacitor?"* → **motivate genuinely inductor-only (RL) circuits** (chokes,
  relay/solenoid coils, flyback, loading-coil Q, transformer leakage).
- [ ] **C10-p42** Red under Figure 10.1 caption ("the output across the
  resistor"): *"Is the output a current or voltage?"* → state that \(v_o=v_R=Ri\)
  is a **voltage** that is proportional to the state (current).
- [ ] **C10-p42** Red at §10.3: *"What is \(y\) in this case?"* → **give the
  output equation** \(y=v_R=Rx\) (currently only \(\dot x\) is shown).
- [ ] **C10-p44** Red in §10.7: *"reference a specific plot."*
- [ ] **C10-p44** Green: *"Show me the root locus plot for this system. How does
  adjusting R change the dynamics?"* (**B6**)

---

## 12. Chapter 11 — RLC Circuits: Resonance, Damping, and Q

- [ ] **C11-p45** Red: **split into Series RLC and Parallel RLC chapters?** (**B3**)
- [ ] **C11-p45** Green at Figure 11.1: *"Where is the output?"* → mark \(v_o\).
- [ ] **C11-p45** Blue at §11.2: *"Show the system of two differential equations
  to start then simplify via subs. to get the second order equation"* →
  **present the coupled first-order pair first**, then reduce.
- [ ] **C11-p46** Green at §11.3: *"Let's calculate the eigenvalues here for
  completeness"* → compute eig(A) explicitly.
- [ ] **C11-p46** Red at §11.4: *"subs. and show this matches the eigenvalues
  derived from [§11.3]"* → show the standard-form poles equal the eigenvalues.
- [ ] **C11-p46** Blue at §11.6/§11.7: *"How is this different / why? Quality
  factors?"* → explain **why \(Q_p\) inverts** relative to \(Q_s\).
- [ ] **C11-p48** Blue at §11.10 worked example: *"make Bode plot for this
  specific system. Also plot root locus. Convert impedance into a phasor."*
  (**B6** + a phasor/impedance illustration for the specific numbers.)

---

## 13. Chapter 12 — Filters, Matching Networks, and Transformers

- [ ] **C12-p49** Red: *"Can this chapter get simplified if the previous chapters
  are more precise and more thorough?"* (**B4**)
- [ ] **C12-p50** Green at §12.3.1: *"move to previous chapters?"* (RC low-pass
  first-principles → Ch 9)
- [ ] **C12-p50** Blue at Figure 12.1: *"Is the output across the resistor or
  capacitor? I am confused"* → label the figure clearly.
- [ ] **C12-p50** Orange at §12.3.2: *"move to previous chapters?"* (LC low-pass
  first-principles → Ch 11)
- [ ] **C12-p51** Green at Figure 12.2: *"Where is the resistor?"* → the LC
  low-pass schematic shows no \(R\) but the model uses \(R\); **show the source/
  load resistance explicitly**.
- [ ] **C12-p53** Green at Figure 12.4: *"How was this generated? What are the
  equations behind these? Ought to be a table?"* → say how the family curves were
  computed and/or tabulate the defining polynomials.
- [ ] **C12-p54** Green at Figure 12.5: *"Where is the input and output?"* → mark
  input/output ports on the L-network schematic.

---

## 14. Chapters 13+ — no annotations
He did not read Ch 13 (Transmission Lines), Ch 14 (Active), Ch 15 (Measurement),
Ch 16–17 (Practice), or the appendices in detail. **Task 5** is to generalize the
above edits and propose how to apply them there.

---

# PATTERNS TO GENERALIZE (for Ch 13+ and the whole book)

Distilled from the Ch 1–12 markup; these are the *rules* his individual comments
imply:

1. **Every schematic must label input and output.** (Ch 9 \(v_o\), Ch 10 output,
   Ch 11 output, Ch 12 Fig 12.1/12.2/12.5, Ch 7 §7.3.1.) → Ch 13: antenna
   one-port terminals; Ch 14: Sallen–Key in/out, feedback-loop nodes.
2. **Show the derivation, don't assert the result.** (Ch 7 impedance, Ch 9
   transfer functions from state space, Ch 11 two-ODE→second-order, eigenvalues,
   Ch 4 asymptotes, Ch 4 −3.01 dB.) → Ch 13: telegrapher's → wave equation steps,
   Γ from boundary conditions; Ch 14: \(A_{cl}\), GBW algebra.
3. **Specific worked examples deserve their own specific plots** (Bode, root
   locus, phasor/impedance), not just a pointer to the generic Part II figure.
   → Ch 13: Γ(f)/SWR(f) plot for the worked line; Ch 14: specific op-amp numbers.
4. **Define every symbol at first use, including abbreviations.** (KCL, KVL, RMS,
   roll-off, "ring", \(v_o\), \(y\).) → Ch 13: VF, RL, \(\beta\), stub; Ch 14:
   VCVS, AGC, phase/gain margin.
5. **Consistent structural depth for worked examples** — one mechanism
   everywhere (callout box, or uniform section level). (**B5**)
6. **State the physical/engineering motivation for each topic** ("where are RL
   circuits important?"). → Ch 13/14/15: open each with a concrete ham-radio
   reason.
7. **Don't duplicate derivations across chapters**; derive once, reference after.
   (**B4**) → Ch 13/14 vs Ch 11/12 overlap (resonance, Q, poles).
8. **Prefer plain, physical language over jargon** and cut self-referential
   meta-narration ("this chapter walks the recipe end to end", "it is worth
   stating once so the pattern is visible", "one circuit at a time").
9. **Figures must not have overlapping text.** (Ch 2 Fig 2.1.)
10. **Notation must be internally consistent** (θ vs φ; series vs parallel Q).
11. **Say how each computed figure was generated** (Ch 12 Fig 12.4).
12. **Merge redundant summary sections** into one "Summary: …". (Ch 5.)

---

# DECISIONS MADE (Alex, 2026-07-27)

- **D1 (B1)** — Ch 3 retitled **"Modeling LTI Systems"**: accept that one chapter
  covers all model forms (ODE → state space → transfer function). Laplace stays,
  but the per-order derivations move into the first-/second-order sections.
- **D2 (B2)** — **NEW Part II chapter: "Feedback: State-Space and Frequency-Domain
  Views."** Move Ch 3 §3.5 *and* the "Foreshadowing op-amps" box into it.
  **Fully generic** (no circuits); closes with forward references to the active
  circuits chapter.
- **D3 (B3)** — **SPLIT RLC into two chapters**: Series RLC, then a shorter
  Parallel RLC that calls back to the series chapter (parallel to how RC and RL
  are already separate chapters).
- **D4 (B4)** — **Move the first-principles derivations back**: RC-as-filter → RC
  chapter; LC low-pass → Series RLC chapter. Filters chapter becomes purely
  **design** (types, order/roll-off, zeros/traps, families as pole placement,
  matching, transformers).
- **D5 (B5)** — **New "Worked Example" callout box** used for in-line examples,
  **but keep each chapter's main closing worked example as a numbered section**
  (so it stays in the ToC).
- **D6 (B6)** — **Specific plots for every worked example** (~12 new figures, real
  Hz/rad-s axes). Generic Part II figures stay as the concept; each circuit
  chapter adds the concrete instance.
- **D7** — C/L series-parallel combination rules go in the **Resistive Networks
  chapter, retitled "Series and Parallel Networks."**
- **D8** — Angle symbols: **φ = signal phase** (phasor), **θ = generic polar form
  / impedance angle**. Relabel Figure 2.1's left panel to φ; state in Notation.
- **D9** — First-order wording: "can never overshoot **or oscillate**", with a
  parenthetical glossing **ringing** as the decaying oscillation of an
  underdamped second-order system.
- **D10** — **New §4.1 "Decibels: Power, Amplitude, and Roll-Off"** at the start of
  the Bode chapter (10log vs 20log, −3.01 dB = 20log(1/√2), decade vs octave,
  "roll-off" defined).
- **D11** — AC chapter: **add a real parallel-impedance/admittance section** (with
  its own schematic) rather than just retitling.

## Target structure (19 chapters)

- **Part I** — 1 Study Guide
- **Part II** — 2 Complex Numbers and Phasors · 3 **Modeling LTI Systems** ·
  4 Frequency Response, Bode, and the s-Plane (+ new §4.1 Decibels) ·
  5 **Feedback: State-Space and Frequency-Domain Views** *(NEW)*
- **Part III** — 6 Circuit Modeling: Paradigms and Components ·
  7 **Series and Parallel Networks** (was Resistive; + C/L combining) ·
  8 AC Steady State (+ parallel impedance) · 9 One Circuit, Four Views ·
  10 RC Circuits (+ filter derivation) · 11 RL Circuits ·
  12 **Series RLC Circuits** (+ LC low-pass derivation) ·
  13 **Parallel RLC Circuits** *(NEW)* · 14 Filters, Matching, and Transformers
  (design only) · 15 Transmission Lines · 16 Active Circuits · 17 Measurement
- **Part IV** — 18 Worked Examples and Exam Map · 19 Anchored Practice

Labels: `ch:complex`(2) `ch:linsys`(3) `ch:splane`/`ch:bode`(4)
`ch:feedback`(5, new) `ch:foundations`(6) `ch:resistive`(7) `ch:ac`(8)
`ch:fourviews`(9) `ch:rc`(10) `ch:rl`(11) `ch:rlc`(12) `ch:rlcpar`(13, new)
`ch:filters`(14) `ch:lines`(15) `ch:active`(16)

## Execution order
1. **Structure** — new chapters (feedback, parallel RLC), retitles, content moves,
   renumber files, `main.tex`, callout box, keep it building.
2. **Content** — all per-page edits above (F*, C*).
3. **Figures** — 12 new/fixed figures + schematic labeling.
4. **Read-through** — front-to-back consistency pass.
5. **Ch 13+ analysis** — generalize the patterns and propose (not implement).
