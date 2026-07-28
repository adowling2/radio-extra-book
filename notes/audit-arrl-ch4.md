# ARRL Chapter 4 ("Radio Mathematics" / "Principles of Circuits") — audit against the book

Method: read the extracted chapter, then grepped `chapters/*.tex` for every candidate
before proposing it. Nine proposals, ranked. Everything already covered is listed at the
bottom with the file and section that covers it, rather than padded into the list.

---

## HIGH

### 1. Power factor from instantaneous power

**What the ARRL asserts.** That `P = IE` "is only true when current and voltage are in
phase," that a reactive element carries "wattless" power measured in VAR, and that the
power factor is `cos θ` — three equations handed over with no argument, plus roughly ten
pool questions (E5D05, E5D07, E5D08, E5D10–E5D15) that use them.

**Our derivation.** Start from the definition, not from the formula: with
`v = V_p cos ωt` and `i = I_p cos(ωt − θ)`, form the *instantaneous* power `p(t) = v i`
and apply the product-to-sum identity:

```
p(t) = V_rms I_rms cos θ  +  V_rms I_rms cos(2ωt − θ)
```

Everything follows by inspection. The first term is constant — that is the average power
`P`, and the `cos θ` the ARRL asserts falls out of the algebra instead of being declared.
The second term oscillates at **twice** the signal frequency with zero mean — that is the
reactive power, and "sloshing" becomes a literal reading of a `2ω` term rather than a
metaphor. At `θ = ±90°` the constant term vanishes identically, so "wattless" is a
theorem. Then close the loop with the circuit: `cos θ = R/|Z|`, so
`P = |S| cos θ = I²|Z|·(R/|Z|) = I²R`, proving the ARRL's two separate power formulas are
one formula. Worth adding the observation the ARRL states but does not explain — `PF` is
positive for either sign of `θ`, because `cos` is even, so the power factor alone cannot
tell you whether the load is inductive or capacitive; the sign of `Q = |S| sin θ` can.
This is also the same `cos²` averaging trick already used for RMS in `chapters/02`, so it
reuses machinery the reader has.

**Where it goes.** `chapters/09_ac_steady_state.tex`, as a new subsection under
`\section{Complex Power}` (currently 24 lines: it defines `S = VI*` and stops).

**Priority: HIGH.** The string "power factor" does not appear anywhere in the book, and it
is one of the most heavily examined single ideas in E5D. This is the largest genuine hole
Chapter 4 exposes.

### 2. The exact half-power bandwidth, and why the band edges are *geometrically* centered

**What the ARRL asserts.** `Δf = f_r / Q`, then instructs the reader to find the band edges
by adding and subtracting half the bandwidth from the center frequency.

**Our derivation.** For the series circuit, `|Z|² = R²[1 + Q²(ω/ω₀ − ω₀/ω)²]`, because
`ωL/R = Q(ω/ω₀)` and `1/(ωCR) = Q(ω₀/ω)`. Half power means `|I|` down by `1/√2`, i.e.
`Q|ω/ω₀ − ω₀/ω| = 1`, which is a quadratic: `ω² ∓ (ω₀/Q)ω − ω₀² = 0`. Two results drop
out of its coefficients with no approximation at all:

- the two positive roots differ by exactly `ω₀/Q`, so `BW = f₀/Q` is an **equality**, not
  an estimate, for the band-pass (current) response;
- their product is exactly `ω₀²`, so `f₀ = √(f₁f₂)` — the half-power points straddle
  resonance *geometrically*, and the true arithmetic midpoint is `ω₀√(1 + 1/4Q²)`.

That gives an error bound for the ARRL's shortcut: the arithmetic centering is high by
about `1/(8Q²)` in fractional terms, which at their own worked case (7.1 MHz, `Q = 150`,
`BW = 47.3` kHz) misplaces each edge by roughly 40 Hz — negligible, but now known to be
negligible rather than assumed. Finish by naming when `f₀/Q` is *not* exact: it is exact
for the current/band-pass response and approximate for the capacitor-voltage (low-pass)
response, which is precisely why the book's own `BW ≈ f₀/Q` carries a `≈`.

**Where it goes.** `chapters/13_rlc_series.tex`, `\section{Q and Bandwidth}` (which
currently asserts `BW ≈ f₀/Q` in two lines). `chapters/14` line 188 and
`chapters/01` line 144 both hedge the same formula and should cross-reference the result.

**Priority: HIGH.** The book states this formula four times and never derives it once; the
derivation also upgrades three of those hedges to a theorem with a quantified error.

### 3. The series-to-parallel loss transformation, `R_p = (1 + Q²)R_s`

**What the ARRL asserts.** Three separate claims, all unexplained: that a parallel RLC at
resonance presents an impedance "approximately equal to" the circuit resistance; that
`Q_s = X/R` and `Q_p = R/X` "are reciprocals" because parallel resistance means *lower*
loss; and (as a design recipe) the L-network reactance formulas.

**Our derivation.** One identity covers all three. Force a series `R_s + jX_s` and a
parallel `R_p ∥ jX_p` to have the same impedance at one frequency by equating `1/Z_series`
with `Y_parallel`:

```
R_p = R_s(1 + Q²),    X_p = X_s(1 + 1/Q²),    Q = X_s/R_s  (preserved)
```

Consequences, in order:

- A *real* tank has its loss in series with the coil, not shunting the tank. Transforming
  it gives `Z_max = R_s(1 + Q²) ≈ Q²R_s = L/(R_sC)` — so the ARRL's "approximately equal
  to the circuit resistance" is hiding a `Q²` multiplier, and the resistance it means is
  the *transformed* one.
- The same transformation shows the frequency at which the reactance actually vanishes is
  shifted to `ω₀√(1 − 1/Q²)`; that shift is the other thing "approximately" was covering.
- `Q_s` and `Q_p` are not two definitions but one quantity viewed through this
  transformation, which is a sharper answer than the book's current appeal to "where the
  loss sits."
- Solving `R_hi = R_lo(1 + Q²)` for `Q` *is* the L-network's `Q = √(R_hi/R_lo − 1)`, so
  `chapters/15`'s asserted design recipe becomes a derived result.

**Where it goes.** New subsection in `chapters/14_rlc_parallel.tex` (natural home:
right after `\section{Why Q Inverts}`), cross-referenced from
`chapters/15_filters_and_matching.tex` `\subsection{The L-Network}` and from
`chapters/21` problem 3, which currently performs this conversion as an unexplained
numeric step (`R_p = Q ω₀L`).

**Priority: HIGH.** One derivation that retires four separate assertions, three of them
currently asserted in *our* text as well. Grep confirms `(1+Q^2)` appears nowhere.

### 4. The time constant of a network with several R's and C's

**What the ARRL asserts.** Combine all the resistors and all the capacitors, then use
`τ = RC`. It then admits that for parallel components "there is an added complication when
the circuit is charging" — and never says what the complication is. Question E5B04 depends
on the recipe.

**Our derivation.** For any network with a single independent capacitor, write KCL at the
capacitor node and collapse the rest of the circuit to its Thévenin equivalent
(`chapters/08` already has Thévenin/Norton):

```
C_eq dv/dt = −(v − v_oc)/R_Th     ⟹     single eigenvalue  s = −1/(R_Th C_eq)
```

so `τ = R_Th C_eq`, where `R_Th` is the resistance seen *at the capacitor terminals with
independent sources zeroed*. That single statement answers everything the ARRL leaves
open. The "complication" is now explicit: when charging, the source is connected, so its
internal resistance is part of `R_Th` and the pole moves; when discharging, the source is
gone and `R_Th` is just the parallel resistor bank — which is why the ARRL's recipe
survives for discharge and fails for charge. And the recipe's real boundary appears: `n`
independent energy stores give `n` eigenvalues, so a network with two capacitors that are
*not* in a single parallel bank has no single `τ` at all, and no amount of combining will
produce one. This is the state-space view of `chapters/03` applied to an exam recipe.

**Where it goes.** `chapters/11_rc_circuits.tex`, after
`\section{Matching the Generic First-Order System}`.

**Priority: HIGH.** The book derives `τ = RC` only for the bare single-R single-C circuit;
the exam asks about banks of parts, and the Thévenin argument is both short and the honest
statement of when the shortcut is legal.

### 5. Skin depth from the diffusion equation, and why coil `Q` peaks and then falls

**What the ARRL asserts.** That fields do not penetrate deeply, that at HF all current
flows in "the outer few thousandths of an inch" and at VHF/UHF a few ten-thousandths, and
(as a figure) that inductor `Q` rises with frequency and then degrades. No formula for the
depth, no reason for the turnover.

**Our derivation.** The book already turns a PDE into a wave solution for the
telegrapher's equations in `chapters/16`; this is the same move in a conductor. Inside a
good conductor, Maxwell's equations plus Ohm's law reduce to a diffusion equation
`∂²J/∂x² = μσ ∂J/∂t`; assume `e^{jωt}` and the spatial solution is
`J(x) = J₀ e^{−x/δ} e^{−jx/δ}` with

```
δ = √(2/(ωμσ))
```

— an exponential decay *and* a progressive phase lag into the metal. Copper checks the
ARRL's own numbers: `δ ≈ 66 µm ≈ 2.6 mil` at 1 MHz and `≈ 5.5 µm ≈ 0.2 mil` at 144 MHz,
which is exactly "a few thousandths" and "a few ten-thousandths." Then modeling the
conducting cross-section as an annulus of thickness `δ` gives
`R_AC ≈ ρℓ/(2πaδ) ∝ √f`, which is the `√f` law the book currently asserts without
support in `chapters/07` line 104. Finally the turnover: `Q_L = ωL/R_AC ∝ ω/√ω = √f`
rises, until the inter-turn capacitance of `\ref{sec:selfresonance}` and core/dielectric
loss take over near self-resonance and pull it down — so the ARRL's figure becomes the
product of two competing power laws rather than a shape to memorize.

**Where it goes.** `chapters/07_circuit_modeling.tex`,
`\subsubsection*{Skin Effect: Why the Loss Term Grows Too}` — expand it from the current
qualitative paragraph.

**Priority: HIGH.** The `√f` law is load-bearing in three places (`chapters/07`,
`sec:lineloss` in `chapters/16`, `chapters/20`) and is currently asserted in all of them.
The derivation is exactly the book's PDE-to-solution idiom.

---

## MEDIUM

### 6. Susceptance of a *lossy* branch: `B = −X/(R² + X²)`

**What the ARRL asserts.** Two "rules": `B = −1/X` and `1/j = −j`, with the sign flip on
inversion presented as a bookkeeping convention.

**Our derivation.** Rationalize once:
`Y = 1/(R + jX) = (R − jX)/(R² + X²)`, so `G = R/|Z|²` and `B = −X/|Z|²`. Three things the
ARRL's rule hides become visible: the sign flip is the conjugate in the numerator, not a
convention; `G ≠ 1/R` and `|B| ≠ 1/|X|` unless the other part is zero, so the ARRL's rule
is the pure-reactance special case; and a capacitor has *negative* reactance but *positive*
susceptance (`B_C = +ωC`), which is the sign trap in E5B05. Also worth noting `G` varies
with frequency even when `R` is a fixed resistor, because `|Z|²` does.

**Where it goes.** `chapters/09_ac_steady_state.tex`,
`\section{Admittance and Susceptance}`, which currently gives only `Y = 1/Z = G + jB` and
one numeric example whose `100 Ω → 50 Ω` outcome it explicitly calls non-obvious — this
formula is what makes it obvious. `chapters/20` line 73 already states `B = −1/X` "for a
pure" reactance and would gain the general case.

**Priority: MEDIUM.** Small derivation, but it converts a memorized rule into a formula
and defuses a sign trap the pool actually exploits.

### 7. Where the resonant magnification actually peaks

**What the ARRL asserts.** That voltages across `L` and `C` build to "several times" the
applied voltage, justified by a playground-swing analogy, with `Q` supplied separately.

**Our derivation.** At `ω₀`, `V_C/V_in = −jQ` exactly — one line from
`V_C = I/(jωC)` with `I = V_in/R` — so the magnification factor *is* `Q`, and the `−j`
says it lags by 90°, with `V_L = +jQ V_in` equal and opposite. That is already sharper
than the analogy. Then the refinement: the maximum of `|V_C|` is not at `ω₀` but at
`ω_p = ω₀√(1 − 1/(2Q²))`, with height `Q/√(1 − 1/(4Q²))`, specializing the standard
second-order peak (`ω₀√(1−2ζ²)`, `M_p = 1/(2ζ√(1−ζ²))`) with `ζ = 1/(2Q)`. This finally
connects `chapters/04`'s resonant-peak formula to `chapters/13`'s circuit, which the book
currently leaves as two unrelated results.

**Where it goes.** `chapters/13_rlc_series.tex`, `\section{Series Resonance}` (three lines
long, and it asserts the factor of `Q`), feeding the existing magnification worked box.

**Priority: MEDIUM.** Sharpens a result the book already has numerically rather than
filling a hole — but it is the one place `Q` acquires a *phase*, and it links two chapters.

### 8. Where `L = μN²A/ℓ` comes from, and what saturation does

**What the ARRL asserts.** That inductance is set by turns count and core permeability;
`A_L` formulas with unexplained constants 10,000 and 1,000,000; and that saturation
distorts the waveform and generates harmonics.

**Our derivation.** Ampère's law around the magnetic circuit gives `NI = Hℓ_e`, then
`B = μH` and flux linkage `λ = NBA`, so

```
L = λ/I = μ_r μ₀ N² A / ℓ_e
```

The `N²` is now a theorem (one factor from the flux generated, one from the flux linked) —
`chapters/12` line 193 currently says "roughly as the square" and leaves it there. `A_L`
is just `L/N²`, i.e. a measured `μA/ℓ_e`, and the mystery constants are `100²` and
`1000²`, the turn-count normalizations the two datasheet conventions use. Same relation
with `B → B_sat` gives a maximum ampere-turn product, hence the volt-second rating; and
since the `B–H` curve is odd-symmetric, the compressed `L(i)` generates **odd** harmonics
specifically — which is the missing half of the ARRL's distortion claim, and connects to
`chapters/17`'s treatment of where linearity ends.

**Where it goes.** `chapters/15_filters_and_matching.tex`, `\section{Transformers}` (its
saturation paragraph is qualitative), with the `N²` result cross-referenced from
`chapters/12`'s ferrite section.

**Priority: MEDIUM.** In scope (magnetics and transformers already are; this is not device
physics), and it is the only place the book quantifies a core. Lower than the top group
because the exam payoff is a handful of recall questions.

### 9. When "lumped" stops being legal, and where 25 nH/inch comes from

**What the ARRL asserts.** Keep leads short above VHF; #24 wire has "about 24 nH per
inch"; lead phase shift "leads to oscillation" at microwave frequencies.

**Our derivation.** The per-inch figure is not a property of #24 wire — it is `Z₀/v_p`
for a wire over a return plane. With `Z₀ ≈ 300 Ω` in air, `L' = 300/(3×10⁸) = 1 nH/mm ≈
25 nH/inch`, which reproduces the ARRL's number from the transmission-line parameters of
`chapters/16` and shows why the answer is nearly independent of wire gauge (it sits inside
a logarithm). Then the validity criterion the book never states: expanding the line's
input impedance `jZ₀ tan βℓ = jωL'ℓ[1 + (βℓ)²/3 + …]` shows the lumped inductor model is
the leading term, with fractional error `(βℓ)²/3` — which is where the `ℓ < λ/10` rule of
thumb comes from and pins it to about 3% error. Finally, "leads to oscillation" is not a
new phenomenon: it is delay eating phase margin, i.e. `chapters/06`'s pure-delay section
driving `chapters/17`'s stability criterion.

**Where it goes.** `chapters/07_circuit_modeling.tex`,
`\section{The Lumped-Element Modeling Paradigm}` — which currently says the assumption
"has failed" without giving a threshold.

**Priority: MEDIUM.** The book invokes the breakdown of lumped modeling in four places
(`chapters/07`, `chapters/16`, `chapters/18`, `chapters/20`) and never quantifies it; grep
finds no `λ/10` criterion and no inductance-per-length figure anywhere.

---

## Considered and rejected

**Already covered — do not add.**

- Rectangular/polar conversion, imaginary unit, `1/j = −j`, the complex plane:
  `chapters/02_complex_numbers_and_phasors.tex`, `\section{Complex Number Refresher}`.
- Phasor diagrams, lead/lag, "ELI the ICE man": `chapters/09`,
  `\section{Phasor Lead and Lag}` — and better than the ARRL's, since it derives the 90°
  from the element law rather than walking quarter-cycles; the mnemonic is already in the
  exam box at line 265.
- `X_L = 2πfL`, `X_C = 1/(2πfC)`, `Z = R + jX`, reactances adding in series and cancelling:
  `chapters/09`, `\section{From Element Laws to Impedance}` and
  `\section{Series Impedance}`.
- `f₀ = 1/(2π√(LC))` and the `X_L = X_C` route to it: `chapters/13`
  `\section{Series Resonance}` and `chapters/14`, both also via the eigenvalues — a
  stronger derivation than the ARRL's.
- `Z = R` at series resonance, high `Z` at parallel resonance, `V` and `I` in phase,
  minimum source current: `chapters/14` comparison table, lines 114–127.
- Circulating tank current and reactive voltages being `Q` times the source:
  `chapters/14` physical box (line 129) and worked box (line 166); series dual in
  `chapters/13` line 156. (Proposal 7 sharpens this rather than adding it.)
- `τ = RC`, `τ = L/R`, the 63.2%/36.8% points, five-`τ` settling: `chapters/11` lines
  81–113 and `chapters/12`. (Proposal 4 is about *networks* of parts, not this.)
- Self-resonance, "a part becomes its opposite," inductor as a parallel resonator:
  `chapters/07`, `\subsection{Self-Resonance}` (`sec:selfresonance`) — already more
  quantitative than the ARRL's treatment.
- `S = VI*`, apparent power in VA, reactive power exchanged not consumed: `chapters/09`
  `\section{Complex Power}`. (Proposal 1 adds the *power factor* half, which is absent.)
- Toroid flux containment vs. solenoid, ferrite mixes, common-mode chokes, beads as
  parasitic suppressors: `chapters/12`, `\section{Ferrites and Common-Mode Current}`,
  including the toroid-vs-rod physical box.
- Rising `Q` of a matching network means higher internal voltages and narrower match
  bandwidth (E5A05): `chapters/15` lines 335–346, and `chapters/21` problem 7.
- Ideal-transformer turns ratios and impedance-squared scaling: `chapters/15`,
  `\section{Transformers}`.

**Out of scope or nothing to derive.**

- Left-hand/right-hand rule for field direction around a conductor (E5D06): field
  geometry and a mnemonic, with no quantity to compute; adjacent to the preface's
  exclusion of pattern geometry.
- The gravitational-field analogy, joules, potential vs. kinetic energy, electrostatic
  vs. magnetostatic: motivational framing. The quantitative content (`½Cv²`, `½Li²`,
  exchange per cycle) is already in the four `energybox` sections.
- Powdered-iron vs. ferrite mix trade-offs, brass slug lowering inductance, `A_L` table
  lookups: materials-selection facts. The one derivable piece is proposal 8.
- DIP / through-hole / surface-mount packaging (E6E02, E6E09–E6E12): package
  identification, excluded by the preface, and no mathematics beyond proposal 9's
  lead-inductance argument.
- Measuring `Q` with a dip meter (E4B08): instrument practice. `chapters/18` covers
  measurement-as-a-circuit-problem; there is no derivation to add here.
- Reading points off the pool's impedance-plane figure (E5C10–E5C12): pure arithmetic,
  and already worked in `chapters/20`, `\section{Coordinate Systems and Phasors}`.
