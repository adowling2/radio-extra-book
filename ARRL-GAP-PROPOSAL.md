# ARRL Manual Audit — What They Assert, What We Could Derive

**Round 4 deliverable.** Produced 2026-07-28 by auditing ARRL *Extra Class License
Manual* chapters 4, 6, 7 and 9 against `chapters/*.tex`. The proposal is below;
**the LEDGER at the end of this file records what has since been built and what is
still open** — read that first if you are picking this up cold.

Per-chapter working notes with full reasoning live in the session scratchpad as
`arrl_ch{4,6,7,9}_gaps.md`.

---

## ⚠️ Read this first: the manual is one pool cycle behind

The PDF in `references/` is the **12th edition, keyed to the pool effective
1 July 2020 – 30 June 2024**. The book targets **2024–2028**. That matters, and it
already bit once:

- The Ch 4 audit reported power factor as carrying "roughly ten pool questions
  (E5D05, E5D07, E5D08, E5D10–E5D15)". **Wrong for the current pool.** E5D now runs
  E5D01–E5D12 and asks about skin effect, lead inductance, parasitics,
  self-resonance and electrical length. "Power factor" survives only as a
  *distractor* (E8A11, E9A03). It was heavily examined in the previous cycle, which
  is what the manual teaches to.
- Similarly, the PLL proposal cited E7H14/E7H15, which **do not exist**. E7H runs
  01–13. PLLs *are* still examined — the group title names them — so the proposal
  stands; only the citations drifted.

I re-checked every pool ID cited across all four audits against
`references/HamExam.org Extra Question Pool.pdf`. **All others verify.** But treat
any exam-relevance claim sourced from the manual as suspect until checked, and note
the happy accident below.

**A pleasant confirmation:** the current E5D is now largely about skin effect,
parasitics and self-resonance — which is exactly what `sec:selfresonance` added
earlier tonight, arrived at from the General-pool check rather than from the manual.

---

## Already done tonight

One item from the Ch 4 audit was not new content but a place **the book itself
asserted** something, so it was fixed under the existing derive-don't-assert
convention rather than held for review:

- **`sec:instpower` in Ch 9** — Ch 9 called reactive power "energy sloshing back and
  forth" and stopped. Now derives `p(t) = V·I·cosθ + V·I·cos(2ωt − θ)`, so the
  sloshing is a `2ω` term with zero mean, the power factor falls out of the constant
  term, and "reactive elements consume nothing" is a theorem. Committed.

---

## The proposal, ranked across all four chapters

### Tier 1 — build a new chapter: "Noise, Sensitivity, and Dynamic Range"

This is the strongest finding of the whole audit. Greps return **zero hits** for
`noise figure`, `kTB`, `174`, `MDS`, `thermal noise`, `Friis`, `dynamic range`,
`intercept`, `compression`, `desens`. The ARRL asserts every number in this area and
in one place explicitly punts the derivation to the *Handbook*. We own every
prerequisite: RMS and average power, maximum power transfer, `|H(jω)|`, cascades
adding in dB, dBm and link budgets, and the mixer product-to-sum expansion with
`2f₁−f₂` and the two-tone test.

| # | Item | The derivation | Pool |
|---|---|---|---|
| 1 | **Where −174 dBm/Hz comes from** | Johnson–Nyquist `v = √(4kTRB)`, then *our own* maximum-power-transfer result halves the voltage into a matched load, so available power is exactly `kTB`. At 290 K that is `10log₁₀(4.00×10⁻²¹/10⁻³) = −173.98`. The factor of 4 in the voltage formula exists precisely so this comes out clean — worth saying aloud. Bandwidth scaling is then `10log B` by inspection. | E4C |
| 2 | **Noise figure and the Friis cascade** | `F ≡ SNR_in/SNR_out` and `F = 1 + T_e/T₀` makes the ARRL's *addition* of NF in dB a theorem. Referring stage 2's noise back through `G₁` gives Friis. Three consequences it never draws: the first stage dominates; a passive loss `L` ahead of the receiver costs `L` dB of NF directly; therefore a mast-mounted preamp helps and the same preamp in the shack largely does not. | E4C |
| 3 | **One power series generates every dynamic-range number** | Model the nonlinearity as `y = a₁x + a₂x² + a₃x³` — the honest version of Ch 17's "does not multiply cleanly" — and drive it with two tones using the *same* identity already at `sec:mixers`. Out falls: 3 dB/dB for third-order and 2 dB/dB for second (the slopes *are* the exponents); gain compression as the `a₃A²` correction to the fundamental; and `IIP3` from equating IM3 to the fundamental. Dividing the two gives `IIP3 ≈ P₁dB + 9.6 dB` free. | E4D |
| 4 | **The (2/3) in `DR3 = ⅔(IP3 − MDS)`** | From the slopes, `P_IM3 = 3P_in − 2·IIP3`. Set it equal to MDS and solve: the 2/3 is slope-3 geometry and nothing else. Same argument at slope 2 gives `DR2 = ½(IIP2 − MDS)`, which the ARRL omits. Blocking DR is a plain subtraction *because* blocking is 1:1 — putting them side by side explains why they are quoted separately. | E4D |
| 5 | **Reciprocal mixing, and the phase-noise skirt from pole location** | Most on-thesis item in the entire audit. Expanding `cos(ω_LO t + φ)` for small `φ` gives a carrier plus a quadrature noise term — a line plus skirts. The mixer then beats an interferer against the skirt at the same offset, landing *inside* the IF as noise. And the skirt shape is the tank's own single-pole roll-off at half-bandwidth `ω₀/2Q_L`, so phase noise falls at −20 dB/decade and scales as `1/Q_L²`: **doubling loaded Q buys 6 dB.** That upgrades Ch 17's existing qualitative phase-noise box to a number, and makes Ch 21's tank-loading problem a phase-noise decision. | E4C |
| 6 | **Noise bandwidth ≠ −3 dB bandwidth** | `B_n = ∫|H|²df / |H|²_max`. On our own one-pole response the integral is `(π/2)f_c`, so `B_n = 1.57 f_3dB` — a single-pole filter is **1.96 dB noisier than its nameplate**. The Butterworth ratios `(π/2n)/sin(π/2n)` are 1.571, 1.111, 1.047, 1.026, so sharper skirts converge — a second, independent reason to add poles that Ch 15 does not give. Then `SNR(B) = S(B)/(N₀B)` peaks at `B ≈ B_signal`, and the mode-by-mode bandwidth table stops being a memory item. | E4C |

*All six numbers above were independently re-derived and check out.*

**Placement:** a new chapter after Ch 17, before Ch 18. It is receiver *theory*, not
bench technique, and Ch 18 was just expanded. Item 3's expansion itself belongs in
`sec:mixers`, where the two-tone algebra already lives; item 6's `B_n` row belongs in
`sec:filterspecs`.

### Tier 2 — high-value single sections

| # | Item | Why | Home |
|---|---|---|---|
| 7 | **Feedback sets impedance, not just gain** | We own `1/(1+L)` and use it only for gain sensitivity. Extending it to driving-point impedance retires four separate ARRL assertions at once: the op-amp's "ideal" infinite input and zero output impedance become the `L→∞` limit rather than axioms; the emitter follower's high input impedance is the series-feedback case; and a regulator's "load regulation" and "low output impedance" are literally the same number. | Ch 17, before `sec:gbw` |
| 8 | **The PLL as a control loop** | The single best thesis fit in the audit, and wholly absent. A VCO integrates frequency into phase, so it *is* a `1/s`; the loop is therefore type-1. (**The audit's claim that this gives zero steady-state phase error for a frequency step is wrong** — checked symbolically: a phase step gives zero error, a frequency step leaves a constant `Δω/K`. So "locked" means the *frequency* is exact with a residual static phase offset. `sec:pll` states it correctly.) Loop filter and gain give `ω_n` and `ζ` directly. Lock vs capture range is the linear/nonlinear distinction. Phase noise is loop shaping: reference noise passed inside the loop bandwidth, VCO noise suppressed by `1/(1+L)`, and the `1/N` divider multiplying VCO noise by `N` — the real reason synthesizer noise degrades at high output frequency. | Ch 17, after Oscillators |
| 9 | **Where the efficiency numbers come from** | Ch 17 currently states 25 %, 50 %, ~60 %, ~80 % on ARRL's authority. Fourier `a₀` and `a₁` of a truncated cosine give `η = ½(a₁/a₀)(V₁/V_dc)`: `θ=180°` returns ½ (and ¼ resistively loaded — the source of the asserted 25 %), `θ=90°` returns `π/4 = 78.5 %`, and `θ<90°` rises toward 100 % as output power collapses. For switching, `p = vi` with an ideal switch forces one factor to zero at all times, so `∫p dt = 0` identically and no conduction angle enters. | Ch 17 `sec:classes` |
| 10 | **Why push-pull cancels even-order products** | Three lines of pure symmetry, no device model: `f(x) − f(−x) = 2Σ_{n odd} a_n xⁿ`, so even orders cancel *identically for any f* — which is why the pair must be matched, not specially biased. Two corollaries the ARRL never draws: push-pull does **nothing** for third-order IMD, the very product we single out as mattering; and the same algebra is why a *balanced* mixer nulls carrier feedthrough, which `sec:mixers` currently takes on faith. | Ch 17 `sec:classes` + `sec:mixers` |
| 11 | **The crystal is two resonances, not one** | We call a crystal "a resonator of very high Q" and never show the network. `R–L_m–C_m` in parallel with `C₀` gives a series resonance (impedance zero) and a parallel resonance (pole) separated by `√(1+C_m/C₀)` — a few hundred ppm, which *is* the entire pulling range and sets a lattice filter's bandwidth. Between them the reactance is inductive: that narrow window is where a Pierce oscillator lives. `∂f/∂C_L ∝ −C_m/(C₀+C_L)²` is why a few pF of stray matters and why `C_L` must be specified. And `Q = ω_s L_m/R` in the 10⁴–10⁶ range becomes arithmetic. | Ch 13 §, or Ch 17 box |
| 12 | **Two-element array factor** | `|F(θ)| = 2|cos((φ + βd cosθ)/2)|` — pure phasor addition, the same superposition Ch 2 introduces. Then the ARRL's memorized table of four patterns is four substitutions: λ/2 in phase → broadside; λ/2 at 180° → endfire; λ/4 at 90° → cardioid; λ/4 in phase → no null anywhere. Gives the direction-finding sense antenna free, and says what a phasing line is *for*. | Ch 16, after the antenna model |
| 13 | **Feed-point impedance vs feed position** | Radiated power does not depend on where you tap, so `R(z) = R_center/cos²βz`. One formula generates the whole ARRL section: 73 Ω at center; ~146 Ω at λ/8, landing in the OCFD's quoted window and explaining its 4:1 transformer; `R→∞` at the end, which is why an end-fed half wave needs the λ/4 inversion we already derive. Delta and gamma matches become tapped transformers with this as the turns ratio. | Ch 16 |
| 14 | **Radiation resistance vs loss resistance, and efficiency** | The book has `R_rad` but **no loss resistor and no efficiency anywhere**. Series elements share a current, so `η = R_rad/(R_rad+R_loss)` is Ch 8's divider applied to power. Then the payoff: the same `R_T` sets `Q`, so adding loss *widens* SWR bandwidth while *lowering* efficiency — which is why a lossy short antenna can look **better** on an SWR meter than a good one. Nothing in the book says this yet. | Ch 16 |
| 15 | **S-parameters as a change of basis; `S₂₁` is the Bode transfer function** | No S-parameter content exists, yet Ch 16 already splits `V` and `I` into forward and reverse waves — the hard part. Define `a, b` and `S₁₁ = Γ` follows *identically*. The valuable one: `S₂₁` is forward transmission into a matched load, i.e. it **is** `G(jω)`. So a VNA sweep is literally a Bode plot and a filter's `\|S₂₁\|` trace is the Ch 15 response — precisely the controls-to-radio bridge this book exists to build. Three calibration standards because three unknowns. | Ch 16 + Ch 18 |
| 16 | **The named antenna matches are our L-network built from our stubs** | Delta, gamma, hairpin/beta and stub matches appear nowhere, yet we have the L-network *and* stub reactances. Unify: a hairpin is a shorted stub `<λ/4`, hence inductive, hence the L-network **demands** a series capacitance — which is why the driven element must be tuned short. The ARRL asserts "the element must be capacitive"; it is a consequence of the topology. Six pool questions, zero new math. | Ch 15 §Impedance Matching |

### Tier 3 — worthwhile, smaller

17. **Skin depth from the diffusion equation.** We assert `R∝√f` in three places (I added one of them tonight). `δ = √(2/ωμσ)` from `∂²J/∂x² = μσ ∂J/∂t` — the same PDE-to-solution move as the telegrapher's equations. Copper gives 66 µm at 1 MHz and 5.5 µm at 144 MHz, matching the ARRL's own "few thousandths / few ten-thousandths". Then `R_AC ∝ √f` from an annulus of thickness `δ`, and coil `Q ∝ √f` rising until self-resonance pulls it down — the ARRL's figure becomes two competing power laws.
18. **Exact half-power bandwidth.** We state `BW ≈ f₀/Q` four times and never derive it. The half-power condition is a quadratic whose roots differ by *exactly* `ω₀/Q` and multiply to *exactly* `ω₀²` — so `BW = f₀/Q` is an equality for the current response, and the band edges straddle resonance **geometrically**, not arithmetically. Quantifies the error in the usual shortcut.
19. **Series-to-parallel transformation `R_p = (1+Q²)R_s`.** One identity retires four assertions, three of them *ours*: a real tank's `Z_max` is `Q²R_s`, not "approximately the circuit resistance"; `Q_s` and `Q_p` are one quantity through this transformation, sharper than our "where the loss sits"; and solving `R_hi = R_lo(1+Q²)` **is** the L-network's `Q = √(R_hi/R_lo − 1)`, currently asserted in Ch 15.
20. **Time constant of a multi-element network.** `τ = R_Th·C_eq` with `R_Th` seen at the capacitor terminals. This is the honest statement of when the exam's combine-everything recipe is legal — and names the ARRL's unexplained "complication when charging": the source resistance is in `R_Th` when connected and gone when not.
21. **Fourier series as the licence for the book's own method.** We analyze one sinusoid at a time and never say why that is general. `y = Σ G(jnω₀)c_n e^{jnω₀t}` is the justification for all of Part II and belongs stated once. Half-wave symmetry then gives the square wave's odd harmonics from symmetry rather than assertion, and the `1/n` envelope is −20 dB/decade for the same reason a one-pole filter is.
22. **Parseval and form factor.** `X_rms² = X_dc² + ΣX_n²` — RMS adds in quadrature over harmonics, which is why only a true-RMS meter is correct, and gives THD free. An averaging meter measures `mean|x|` calibrated by the sine's 1.111, so it reads a square wave **11 % high**: the whole content of the ARRL's warning, in one line.
23. **Insertion loss is a Q ratio.** `IL = −20log₁₀(1 − Q_L/Q_U)`. Narrow and low-loss are in direct competition, and a duplexer needs both at once — achievable only with `Q_U` in the thousands, i.e. a cavity. Turns E7C10 into an inequality.
24. **Ring-down bounds filter narrowness.** We say a second-order system rings for ~Q cycles but never turn it into a design bound. `τ = Q/(πf₀)`, so a 250 Hz CW filter rings ~4 ms — an appreciable fraction of a fast Morse dot. "Narrower is always better" is false, and now quantifiably so.
25. **Ground reflection as an image source.** Item 12 with `d = 2h`, `φ = π`: `2|sin(βh sinψ)|`. Explains the always-null along the ground, the takeoff angle falling as `sinψ = λ/4h`, and the second lobe entering at exactly the `h > λ/2` the ARRL quotes. Include only if 12 lands.
26. **Folded dipole's 4:1 by even/odd mode.** The odd mode is two λ/4 shorted stubs in series — an open, by our own stub result — so it vanishes, leaving `Z = 4Z_dipole`. Best illustration in the chapter that superposition plus one stub identity solves an antenna problem.
27. **Thermal runaway as a DC loop with `L_th ≥ 1`.** Runaway is our own stability criterion at `ω = 0`. Emitter resistance divides the sensitivity by `(1+g_mR_E)`; the bypass capacitor then makes the feedback DC-only — a pole-zero split between bias loop and signal loop, which the ARRL leaves as a bare statement.
28. **Smaller closures.** Comparator hysteresis as deliberate positive feedback; the parasitic suppressor as a `R∥sL` high-pass *impedance*, converting "found experimentally" into a corner placement; "dip the plate, then load it" as resonance-then-transformation; `VF = 1/√ε_r` closing our own velocity-factor loop (the 0.66 in our table becomes a prediction); the λ/8 stub as the only length where `|X| = Z₀`; ERP/EIRP as our link budget truncated at the antenna; terminated traveling-wave antennas as `Γ_L = 0`; the Wilkinson divider by even/odd symmetry; frequency-counter `±1` count plus ppm; aliasing fold-back `f_alias = |f − nf_s|`; and the attenuator corollary — `L` dB of attenuation improves the IMD ratio by `2L` because the product falls three times as fast.

---

## Needs your decision

**Sampling and DSP.** Both the Ch 6 and Ch 7 audits independently identify this as
the largest genuinely uncovered block, and they make an argument I had not:
**Ch 15 already asserts that FIR filters can be exactly linear phase and IIR cannot.**
That is an unsupported claim in *our* book, which is the strongest case for opening
the topic. The derivations would be unusually cheap because sampling is
multiplication — the mixer algebra we already have, applied to an impulse train,
gives spectral replication, Nyquist, and aliasing as folding. Quantization gives
`SNR = 6.02N + 1.76 dB`, which is pleasingly the same 6 dB as one S unit. Symmetric
FIR coefficients give strictly linear phase, proving Ch 15's assertion.

Against: doing it properly is a chapter, not a section, and it moves the book's
declared boundary. **Not authorized, not started.** My recommendation: do it, scoped
tightly to sampling/aliasing/quantization/linear-phase FIR, and explicitly *not*
I/Q or modulation.

---

## What I rejected

Consistently across all four audits, and worth recording so the boundary stays
stable: modulation and demodulation theory (AM/SSB/FM spectra, reactance modulators,
Carson's rule, discriminators, I/Q, Hilbert transforms); semiconductor and tube
device behaviour (bias points, `r_e`, α and β, electrode correspondences, packaging);
digital logic; radiation-pattern *geometry* (beamwidth, F/B, E- vs H-plane, lobe
counting, dish aperture gain, NEC segmentation); propagation and soil conductivity;
grounding and lightning practice; operating and troubleshooting practice
(noise-hunting, WWV checks, DF triangulation); named-hardware taxonomy; and
metrology vocabulary with nothing to derive. Circulators and isolators were rejected
for a specific reason worth remembering: none of our existing tools produce
nonreciprocal behaviour, so it would need genuinely new machinery.

---

# LEDGER — every audit item, and whether it landed

Added 2026-07-28 after Alex asked whether any suggestion had been orphaned. This
reconciles **all three audits** (the Round 4 read-through, the General-pool coverage
check, and the four ARRL chapter audits) against the book as built, by label lookup
and regex over `chapters/`, `frontmatter/` and `appendices/`.

**Four items initially scored "present" were false positives on inspection and are
listed as open below:** figure provenance (only 2 of 29 captions, not all), feed-point
impedance (the `cos²` hit was the RMS derivation), skin depth (the *term* appears in
`sec:selfresonance`, but `δ = √(2/ωμσ)` is not derived), and the exact half-power
bandwidth (the "geometrically" hits were unrelated).

Score: **33 done, 24 open.** Nothing has been silently dropped.

## ✅ Done (33)

**Read-through (4 of 7 findings + 2 cleanups):** Ch 6 wired in (0 → 27 inbound refs) ·
acronym regressions · Nyquist introduced (`sec:nyquist`) · self-resonance and skin
effect moved out of the practice chapter (`sec:selfresonance`) · Ch 13 ordering ·
orphan labels 9 → 0 · glossary order + 30 → 65 entries · `exambox` in Chs 7/11/13/15/16
· `workedbox` in Chs 11–14 · Ch 17 §Power Supplies rebuilt

**General-pool gaps (all 9):** RMS/PEP (`sec:rms`, `sec:pep`) · lossy lines
(`sec:lineloss`) · rectifiers and ripple · neutralization (`sec:neutralization`) ·
ferrites, common-mode, ground loops (`sec:commonmode`, `sec:groundloops`) · filter
datasheet vocabulary (`sec:filterspecs`) · antenna length and dBi/dBd
(`sec:antennalength`) · mixer roles and the two-tone test · S units and link budgets
(`sec:sunits`)

**ARRL Tier 1 (all 7 → Ch 19):** `kTB` and −174 dBm/Hz · noise figure · Friis ·
the power series and IIP3 · DR3's ⅔ · reciprocal mixing and the `1/Q_L²` skirt ·
noise bandwidth

**ARRL Tier 2 (1 of 10):** the PLL (`sec:pll`)

**Tier A — all 5 done:** the exact half-power bandwidth (`sec:halfpower`) — `BW = f₀/Q` is now derived as an identity, not quoted with a hedge, and the band edges are located: `f₀ = √(f₁f₂)`. The `≈` was relaxed in Chs 1, 4, 13, 14, 16, 22, 23, the formula index and the cheat sheet; it was *kept*, with the reason now stated, in Ch 20 (an analyzer's usable band is an SWR limit, not the half-power one) and in Ch 16's antenna model (the lumped RLC, not the algebra, is the approximation).

**Tier A, second item:** the series↔parallel transformation (`sec:seriesparallel`) — `R_p = (1+Q²)R_s`, `X_p = (1+Q⁻²)X_s`, derived by matching admittances at one frequency. The invariant is `Q` itself (`R_p/X_p = X_s/R_s`), which is the literal form of Ch 14's previously hand-waved claim that “there is only one `Q`.” Retires three of our own assertions: a real tank's peak impedance is `(1+Q²)r ≈ L/(Cr)`, not “roughly the loss resistance”; `Q_s` and `Q_p` are one quantity through the map; and `sec:lnetwork` now *derives* all three L-network formulas from this identity instead of asserting them — including the fact that the transformed reactance is exactly the `R_hi/Q` the shunt element cancels, so an L-network is one transformation plus a cancellation. Ch 23's oscillator-tank problem no longer converts loss to shunt resistance as an unexplained step.

**Tier A, third item:** skin depth (`sec:selfresonance`) — the diffusion equation `∂²J/∂x² = μσ ∂J/∂t` with `e^{jωt}` gives `k = √(jωμσ) = (1+j)/δ` and `δ = √(2/ωμσ)`, so amplitude decay and phase slip share one length *because* `√j` has equal parts. Copper: 66 µm at 1 MHz, 5.5 µm at 144 MHz. An annulus of thickness `δ` then gives `R_AC ∝ 1/δ ∝ √f` — the law asserted in four places (Chs 7, 16, 22 and the glossary), now earned, with `R_AC/R_DC ≈ a/2δ` as a bonus. It also exposed a **wrong claim of our own**: Ch 22 said a coil's `Q` falls at the top of its range "because `R` is rising while `ωL` is." Skin effect alone leaves `Q ∝ √f` *rising*; what pulls it down is the inter-turn capacitance, via `Q_eff ≈ Q₀(1 − (f/f_SRF)²)`, which also puts the peak at `f_SRF/√5 ≈ 0.45 f_SRF`.

**Tier A, fourth item:** the conduction-angle efficiency integral (`sec:conductionangle`) — Fourier `I_dc` and `I₁` of a cosine truncated at half-angle `θ` give `η = ½(I₁/I_dc)(V₁/V_dc)`, two independent factors. The current factor is the conduction angle: exactly `½` at 360° and exactly `π/4` at 180°, so 78.5 % *is* `π/4`. The voltage factor is the load coupling, and it alone explains why Class A is quoted at both 50 % and 25 % — a resistive load must carry the DC, halving the available swing. Four numbers previously on ARRL's authority, now one integral. Also added `sec:switching`: for an ideal switch `p = vi` has one factor zero at every instant, so `∫p dt = 0` identically and there is no ceiling to derive — which fills a real gap, since the book did not cover Class D at all and the pool asks about it three times (E7B02, E7B03, E7B08).

**Tier A, fifth item:** push-pull even-order cancellation (`sec:pushpull`) — `f(x) − f(−x) = 2Σ_odd aₙxⁿ`, three lines and no device model. Every even order vanishes *for any f*, the `aₙ` never entering, which is why the pair must be **matched** rather than specially biased: mismatched devices leave `aₙ − bₙ`, so a drifting pair shows up first as a second harmonic. Two corrections to how this is usually told. It is not two distortions cancelling — the operation extracts the *odd part* of `f` and the even part is absent, not suppressed. And push-pull does **nothing** for third-order IMD: it doubles the fundamentals and the `2f₁−f₂` products by the same factor, leaving the ratio that `sec:powerseries` cares about untouched. The same parity argument, applied to the RF port instead, nulls a balanced modulator's carrier — `sec:mixers` no longer takes that on faith, and its vague “the two inputs cancel at the output” is gone.

**Tier B1 — S-parameters (`sec:sparams`, `sec:vna`).** The bridge Alex flagged. `a = (V+Z₀I)/2√Z₀` and `b = (V−Z₀I)/2√Z₀` collapse, on substituting Ch 16's own `V = V⁺+V⁻` and `Z₀I = V⁺−V⁻`, to `a = V⁺/√Z₀` and `b = V⁻/√Z₀` — an invertible change of basis (det `−½`), with `|a|²` the incident power. Hence `S₁₁ = Γ` *identically*, so return loss and SWR are three readings of one number. `S₂₁` is the forward transmission of the `Z₀`-embedded two-port, i.e. `G(jω)`, so **a VNA sweep is a Bode plot** and `−20log|S₂₁|` is `sec:filterspecs`'s insertion loss. Calibration is three standards because the one-port error model is bilinear with three complex unknowns, and the natural three are the `Γ = −1, 0, +1` that Ch 16 already evaluated. `sec:vna` carries the `controlsbox` where the book's two halves shake hands. **Precision point the usual telling gets wrong:** `S₂₁ ≠ V₂/V₁` in general — `V₂/V₁ = S₂₁/(1+S₁₁)`, equal only when the input is matched — so the identification is safe in a filter's passband and wrong at its band edges; a `mistakebox` says so. Pool: E4B03/04/05/07/09/11, all verified against `references/` (E4B09, "filter frequency response," is literally the `|S₂₁|` sweep).

**Tier B2 — feedback sets impedance (`sec:feedbackz`).** Two test-source derivations retire the op-amp ideals as axioms. Ground the input, drive the output: the loop returns `βV_t`, so the internal source opposes with `−AβV_t` and `Z_out = R_o/(1+L)`. Drive the non-inverting input: the loop squeezes `v_d` to `V_t/(1+L)`, and a resistor with no voltage across it draws no current, so `Z_in = R_id(1+L)`. The ideals are the `L→∞` limit of two ordinary circuit results — 1 MΩ and 75 Ω inside a loop of `L = 10⁵` become 100 GΩ and 750 µΩ. A `controlsbox` collects the payoff: **one factor, five consequences** — `1+L` divides gain, fractional error, distortion and output impedance, and multiplies bandwidth and input impedance, which is also why stability is unavoidable, since `1+L = 0` is where the loop oscillates. A `mistakebox` adds the nuance the usual telling omits: feedback does not always *raise* input impedance — the inverting topology compares currents at a node, so the source sees only `R_in` and `R_id` is irrelevant. That is a property of the topology, not the chip. The `physicalbox` that used to attach all three ideals to the dependent source now attaches only the large-`A` one.

**ARRL Tier 3 (5 of 22):** Fourier series (`sec:fourier`) · Parseval and form factor
(`sec:parseval`) · the aliasing fold-back formula (`sec:samplingthm` — though *not*
its oscilloscope application in Ch 20) · the attenuator corollary (`2L`)

## ⬜ Open (24), ranked

### Tier A — the book asserts these itself, so they are defects by our own convention

| # | Item | Why it ranks here |
|---|---|---|

### Tier B — best remaining thesis bridges

| # | Item | Why |
|---|---|---|
| T2.15 | **S-parameters; `S₂₁` *is* `G(jω)`** | The strongest bridge left. Ch 16 already splits `V` and `I` into forward/reverse waves, so `S₁₁ = Γ` follows identically — and `S₂₁` is the transfer function of Chs 3–4 measured in a matched system, which makes **a VNA sweep literally a Bode plot**. Also E4B03/04/05/07/11. |
| T2.7 | **Feedback sets impedance, not just gain** | We use `1/(1+L)` for gain sensitivity only. Extending it to driving-point impedance turns the op-amp's "ideal" infinite input and zero output impedance from axioms into the `L→∞` limit, and shows a regulator's load regulation and output impedance are the same number. |
| T2.14 | **Antenna efficiency** | The book has `R_rad` but **no loss resistance and no efficiency anywhere**. `η = R_rad/(R_rad+R_loss)` is Ch 8's divider applied to power — and the payoff is counterintuitive: adding loss *widens* SWR bandwidth while *lowering* efficiency, so a lossy short antenna can look **better** on an SWR meter. |
| T2.13 | **Feed-point impedance vs feed position** | `R(z) = R_center/cos²βz` generates the whole ARRL section — 73 Ω at centre, ~146 Ω at λ/8 (explaining the OCFD's 4:1), `R→∞` at the end (explaining why an end-fed half wave needs the λ/4 inversion we derive). |
| T2.12 | **Two-element array factor** | `\|F\| = 2\|cos((φ+βd cosθ)/2)\|` — pure phasor addition. Turns a memorized table of four patterns into four substitutions, and gives the DF sense antenna free. |
| T2.11 | **Crystal as two resonances** | `R–L_m–C_m` parallel `C₀` gives an impedance zero and pole a few hundred ppm apart — which *is* the pulling range, sets lattice-filter bandwidth, and explains why `C_L` must be specified. E6D02, E7H12. |
| T2.16 | **Named antenna matches** | Hairpin, gamma, delta, stub — all absent, though we own both the L-network and stub reactances. The hairpin is a shorted stub `<λ/4`, hence inductive, hence the network **demands** a series capacitance — so "the element must be capacitive" becomes a consequence. Six pool questions, zero new math. |

### Tier C — smaller, still worthwhile

T3.20 τ = `R_Th·C_eq` for multi-element networks (and the honest limit of the
combine-everything recipe) · T3.23 insertion loss as `Q_L/Q_U`, which is why duplexers
need cavities · T3.24 ring-down `τ = Q/(πf₀)` bounding how narrow a filter should be ·
T3.27 thermal runaway as a DC loop with `L_th ≥ 1` · T3.26 folded dipole's 4:1 by
even/odd mode · T3.25 ground reflection as an image source (needs T2.12 first) ·
T3.28a comparator hysteresis · T3.28b parasitic suppressor as `R∥sL` · T3.28c
dip-then-load as resonance-then-transformation · T3.28d `VF = 1/√ε_r` closing our own
velocity-factor loop · T3.28e the λ/8 stub as the only length where `\|X\| = Z₀` ·
T3.28f ERP/EIRP as our link budget truncated · T3.28g terminated traveling-wave
antennas as `Γ_L = 0` · T3.28h Wilkinson divider by even/odd symmetry · T3.28i
frequency-counter ±1 count plus ppm · the oscilloscope fold-back application of
`sec:samplingthm` in Ch 20

### Tier D — housekeeping, carried since Round 3

- **Ch 10 and Ch 21 have no callout boxes and no figures.** Ch 10 is defensible as a
  two-page hinge; Ch 21 is not — it is still the weakest chapter, with four examples
  carrying zero cross-references and component values unrelated to the book's running
  ones.
- **Figure provenance: only 2 of 29 captions** say how the figure was computed
  (`filter_families` and `line_attenuation`). Consider a one-line clause per caption or
  one front-matter note.
- **Ch 22 mixes two structural registers** — numbered sections with starred
  per-question subsections, then abandons the pattern.
- **Appendix B still restates Ch 7's units material** (cross-referenced, not merged).
