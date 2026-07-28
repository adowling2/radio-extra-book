# ARRL Manual Audit — What They Assert, What We Could Derive

**Round 4 deliverable. This is a proposal, not a plan of record — nothing here has been
written into the book except where noted.** Produced 2026-07-28 by auditing ARRL
*Extra Class License Manual* chapters 4, 6, 7 and 9 against `chapters/*.tex`.

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
| 8 | **The PLL as a control loop** | The single best thesis fit in the audit, and wholly absent. A VCO integrates frequency into phase, so it *is* a `1/s`; the loop is therefore type-1, which is why locked means zero steady-state phase error — derived, not described. Loop filter and gain give `ω_n` and `ζ` directly. Lock vs capture range is the linear/nonlinear distinction. Phase noise is loop shaping: reference noise passed inside the loop bandwidth, VCO noise suppressed by `1/(1+L)`, and the `1/N` divider multiplying VCO noise by `N` — the real reason synthesizer noise degrades at high output frequency. | Ch 17, after Oscillators |
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
