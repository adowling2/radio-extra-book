# Revision Notes — from Alex's Tablet Markup (Notability)

Parsed from the marked-up PDF (70 pp) of the current build. Colors group related
comments on a page. This file is the working checklist; we'll go through it item
by item. Each item has an ID (`Sn` structural, `Tn` theme, `Cn` per-location) and
a status box.

---

## 0. Overarching direction (from your voice note)

**Reorganize into three parts:**

- **Part I — Exam-Ready Reference.** The cheat sheet / exam materials (as now,
  cleaned up).
- **Part II — Math & Control-Theory Review.** Review the key math and control
  concepts *generically*, before any specific circuit: complex numbers/phasors,
  first- and second-order linear dynamical systems, state-space form, transfer
  functions, poles/zeros and the s-plane, Bode plots, root locus, damping
  ratio ζ ↔ Q. (This absorbs the current Complex-Numbers, Frequency-Response,
  and s-Plane chapters, plus the Complex-Math appendix.)
- **Part III — The Circuits.** Build the models up circuit by circuit. **RC, RL,
  and RLC each become their own chapter**, and each chapter:
  1. shows the schematic,
  2. derives the differential equation from the schematic,
  3. derives the **state-space** equation,
  4. shows **equivalence to a generic first- / second-order linear dynamical
     system** (from Part II),
  5. makes the **control-theory connections** explicitly,
  6. ends with a **worked example that shows and interprets a Bode plot and a
     root-locus plot**.
  Then the remaining circuit topics (resistive networks, filters/matching,
  active/feedback, transmission lines, measurement) follow.

This is the through-line for almost every page comment below: *show the
schematic, derive it, connect it to the generic linear-system / control picture,
and illustrate + interpret with Bode and root-locus plots.*

---

## 1. Structural / front-matter edits

- [ ] **S1 — Title subtitle (p. title).** Replace the struck line "A concise
  mini-textbook converted and revised from *Ham Radio Circuit Theory…*" with:
  *"…for learning Radio Circuit Theory for the Amateur Extra Exam from the
  perspective of control theory."* (Keep "A Dynamical Systems Perspective for
  Engineers.")
- [ ] **S2 — Preface, ¶1 (p. i, red "not needed" + blue strike).** Delete the
  provenance paragraph ("This mini-textbook is a polished LaTeX edition of the
  supplied Word manuscript… authoritative source…").
- [ ] **S3 — Preface, audience (p. i, green).** Elaborate on the intended
  audience.
- [ ] **S4 — Preface, references (p. i, blue).** Acknowledge the specific
  references here (currently generic).
- [ ] **S5 — Exam Scope & Independence Note (p. iii, red strike + green).**
  Delete as a standalone section; **move its content into the Preface and
  integrate.**
- [ ] **S6 — Notation typography (p. iv, purple).** You circled `j`, `ω`, `s`
  with "italics?" — decide the convention (currently `j` is upright `\mathrm{j}`;
  `ω`, `s` are italic). See Q4.
- [ ] **S7 — Complex Math Refresher appendix (App. C, red).** "Move this
  earlier" → folds into Part II math review.
- [ ] **S8 — Complex Numbers chapter (Ch. 4, green).** "Move after the
  one-circuit / four-perspectives chapter?" — superseded by the reorg: it goes
  into Part II. (Confirm.)
- [ ] **S9 — s-Plane chapter (Ch. 11, red + blue).** "Move earlier and present
  it with generic first- and second-order linear systems." → Part II.

---

## 2. Recurring themes (cross-cutting; each expands into many page items)

- [ ] **T1 — Show circuit schematics.** You are a visual learner and asked for a
  schematic almost everywhere a circuit is named: RC low-pass (5.2), voltage
  divider (7.3), Thevenin/Norton worked example (7.6), second-order section
  (12.4), L-network (12.6.1), typical op-amp circuit (13.4).
- [ ] **T2 — Show *and interpret* Bode plots.** 5.1, 5.4/5.5 ("show me how to
  read them from a Bode plot"), 8.8, 9.6, 10.6, 12.3. Also: how was the existing
  Bode figure generated / what does it mean (5.x).
- [ ] **T3 — Show *and interpret* root-locus plots.** 11.5 ("what does this look
  like for just an RC or RL circuit?"), and as a required element of each RC/RL/
  RLC chapter.
- [ ] **T4 — Show transient-response plots.** v_C(t) for RC (8.2), i(t) for
  RL (9.2).
- [ ] **T5 — More worked examples.** Admittance (4.5), complex power "how is
  this used in a calculation?" (4.6), rectangular/polar (4.2).
- [ ] **T6 — Derive, don't assert.** "How is this derived / does it fall out of
  the math?": RLC impedance (4.1); "how do we go from picture → differential
  equations → transfer functions?" (5.2/5.3); "what about the transfer
  function?" for RL and RLC (6.3/6.4); derive series/parallel from KCL/KVL (7.2).
- [ ] **T7 — Define every variable; add ChE analogies.** impedance (4.4),
  reactance (4.3), admittance/susceptance (4.5), A & β (feedback), R_hi/R_lo &
  X_shunt (matching), loaded/unloaded/component Q (10.5), saturated core (12.7),
  decade vs octave (1.5), Q_s / bandwidth (1.4). "Is there a chemical-engineering
  analogy?" for impedance, reactance, admittance.
- [ ] **T8 — Make control-theory connections explicit & foreshadowed.** "Connect
  it more explicitly" (6.4 Controls Connection), "how does this relate to control
  theory?" (10.5), "what control-theory aspects must we foreshadow?" (Ch. 13),
  "this is a second-order dynamical system" (6.4).
- [ ] **T9 — Physical meaning + applications of damping.** "Physical analogy for
  under/critically/over-damped?" (6.4); "which applications prefer each?" (11.8);
  "what does long-ringing mean?" (11.8).
- [ ] **T10 — Add RF-significance sentences.** e.g. "why is Thevenin/Norton
  important for RF? missing a sentence about significance" (7.5).

---

## 3. Page-by-page comment log

### Cheat sheet (Part I)
- [ ] **C1 (p.2, green).** Distinguish symbols *needed for the exam* vs *extra
  for this book*; how to tell them apart.
- [ ] **C2 (p.2, orange).** Symbol table: when is a quantity lower- vs
  upper-case (q,Q; i,I)?
- [ ] **C3 (p.2, green).** Explain the extra symbols used (ℋ, Q, etc.).
- [ ] **C4 (p.3, blue).** Label groups "time constants" / "resonance"; define
  Q_s and bandwidth (they appear before being introduced).
- [ ] **C5 (p.4, green).** Define "decade vs octave."
- [ ] **C6 (p.4, blue).** Define "bandwidth"; define A and β in the feedback row.
- [ ] **C7 (p.4, green).** Define R_hi, R_lo, X_shunt in the L-network row.
- [ ] **C8 (p.5, red).** Transmission-line section: make sure **all variables are
  defined**.

> Note: several of these reflect that the cheat sheet currently uses symbols
> before Part II/III defines them. If Part I is meant to stand alone for
> exam crunch, it needs its own compact definitions or forward-pointers.

### Ch. 4 — Complex Numbers, Phasors, Impedance  → Part II
- [ ] **C9 (p.11, green).** Move (see S8).
- [ ] **C10 (p.11, green).** 4.2: add a worked example to elaborate rectangular/
  polar.
- [ ] **C11 (p.11, purple).** 4.3: define reactance; ChE analogy?
- [ ] **C12 (p.12, blue).** Fig 4.1 / RLC impedance: how is `R + j(ωL − 1/ωC)`
  derived — does it fall out of the math?
- [ ] **C13 (p.12, green).** 4.4: what is impedance? ChE analogy?
- [ ] **C14 (p.12, orange).** 4.5: "good tip" + "show how to do this" (admittance).
- [ ] **C15 (p.12, red).** 4.5: what is admittance *physically*? ChE analogy?
- [ ] **C16 (p.12, purple).** 4.5: show another example (Y_eq = Σ Y_k).
- [ ] **C17 (p.12, green).** 4.6: how is S = VI* used in an example calculation?

### Ch. 5 — Frequency Response & Bode  → Part II
- [ ] **C18 (p.13, purple).** Should this chapter move later (after transfer
  functions for circuits are introduced)? — resolved by reorg: Bode lives in
  Part II as generic material; circuit-specific Bode examples live in Part III.
- [ ] **C19 (p.13, green).** 5.1: show a pictorial illustration of a Bode plot.
- [ ] **C20 (p.13, green).** 5.2: show a schematic/picture of the RC low-pass.
- [ ] **C21 (p.13, blue).** 5.2: define the corner frequency ω_c.
- [ ] **C22 (p.13, red).** 5.2/5.3: show the full path picture → ODE → transfer
  function.
- [ ] **C23 (p.14, orange/red).** Fig 5.1: explain how to interpret the marked
  points.
- [ ] **C24 (p.14, green).** Fig 5.1: mark the corner on the plot.
- [ ] **C25 (p.14, purple).** Figs 5.1/5.2: what do they mean, how were they
  generated (show code?).
- [ ] **C26 (p.14, red).** How would I use these plots when discussing a circuit?
- [ ] **C27 (p.15, red).** 5.4/5.5: elaborate the concepts; show how to *read*
  them from a Bode plot.

### Ch. 6 — One Circuit, Four Views  → becomes the Part III template
- [ ] **C28 (p.17, blue).** 6.2.4: note the transfer function is what it is
  *because we defined the output across the capacitor* — make that explicit.
- [ ] **C29 (p.17, green).** 6.3: show the transfer function for the RL circuit.
- [ ] **C30 (p.18, green).** 6.4: show the transfer function for the RLC circuit.
- [ ] **C31 (p.18, purple).** 6.4: state "this is a second-order dynamical
  system"; connect to Part II generic system.
- [ ] **C32 (p.18, purple).** 6.4 Controls Connection: "if yes, connect it more
  explicitly / show the connection more explicitly."
- [ ] **C33 (p.18, red).** 6.4: what is the physical analogy for underdamped,
  critically damped, and overdamped?

### Ch. 7 — Resistive Networks
- [ ] **C34 (p.19, green).** 7.2: how to derive series/parallel from KCL, KVL?
- [ ] **C35 (p.19, blue).** 7.3: show the voltage-divider circuit schematic.
- [ ] **C36 (p.20, green).** 7.5: why is Thevenin/Norton / matching important for
  RF? Add a significance sentence.
- [ ] **C37 (p.20, purple).** 7.6: "I need to see schematics to understand the
  connection. This is lost on me." (worked example needs a drawn circuit.)

### Ch. 8 — RC Circuits  → Part III (own chapter, full template)
- [ ] **C38 (p.21, blue).** 8.2: show a plot of v_C(t).
- [ ] **C39 (p.22, blue).** 8.8: why does the cutoff frequency matter? Connect
  back to a Bode plot here.

### Ch. 9 — RL Circuits  → Part III (own chapter, full template)
- [ ] **C40 (p.23, blue).** 9.2: show a plot of i(t).
- [ ] **C41 (p.24, blue).** 9.6: interpret a Bode plot here.

### Ch. 10 — RLC Resonance, Damping, Q  → Part III (own chapter, full template)
- [ ] **C42 (p.26, red).** 10.5: how does Q / sharpness relate to control theory?
- [ ] **C43 (p.26, red).** 10.5: define loaded / unloaded / component Q meanings.
- [ ] **C44 (p.26, red).** 10.6: does the energy/Q picture relate to a Bode plot?
- [ ] **C45 (p.27, red).** 10.7: how does the worked example relate to the
  second-order dynamical system?

### Ch. 11 — s-Plane, Poles, Zeros  → Part II (generic)
- [ ] **C46 (p.28, red+blue).** Move earlier; present with generic first/second-
  order linear systems (S9).
- [ ] **C47 (p.30, blue).** Fig 11.1 root locus: what does this look like for
  just an RC or RL circuit? (Add simpler root-locus illustrations.)
- [ ] **C48 (p.32, red).** 11.8: which applications prefer underdamped,
  overdamped, or critically damped?
- [ ] **C49 (p.32, blue).** 11.8: what does "long-ringing" mean?

### Ch. 12 — Filters, Matching, Transformers
- [ ] **C50 (p.33, red).** 12.3: show a Bode plot for cutoff/slope/order.
- [ ] **C51 (p.34, red).** 12.4: show a circuit schematic of a second-order
  section.
- [ ] **C52 (p.34, red).** 12.5: define "moderate transition."
- [ ] **C53 (p.35, red).** Fig 12.2: show illustrations for *all* the filter
  families ("I am a visual learner").
- [ ] **C54 (p.35, red).** 12.6.1: show the L-network schematic.
- [ ] **C55 (p.35, red).** 12.6.1: show the L-network math (derivation).
- [ ] **C56 (p.35, blue).** 12.6.2: show the π/T-network math.
- [ ] **C57 (p.36, blue).** 12.7: define "saturated core" — what is it, what does
  it mean?

### Ch. 13 — Active Circuits, Feedback, Oscillators
- [ ] **C58 (p.37, red).** What control-theory aspects must we foreshadow (in
  Part II) to make this chapter land?
- [ ] **C59 (p.38, blue).** Fig 13.1: check the sign convention at the summing
  junction.
- [ ] **C60 (p.38, green).** 13.4: show a typical op-amp circuit, or is this fully
  abstracted?

### Ch. 14 — Transmission Lines
- [ ] **C61 (p.42, red).** 14.4: what are typical velocity factors in radio and
  power systems?

---

## 4. Open questions for Alex (see chat)
Captured separately so we can settle them before implementing.
