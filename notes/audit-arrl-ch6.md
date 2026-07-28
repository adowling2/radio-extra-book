# ARRL Chapter 6 vs. *Circuit Theory for the Amateur Extra Exam* — gap audit

Source: ARRL ECLM Ch. 6 (6.1 Amplifiers, 6.2 Signal Processing, 6.3 DSP/SDR,
6.4 Filters and Impedance Matching, 6.5 Power Supplies).
Book state verified by grepping `chapters/*.tex`, not by TOC alone.

Headline: chapters 15 and 17 already absorb most of ARRL 6.4 and much of 6.1/6.2.
The genuinely open, genuinely derivable material clusters in four places:
**feedback's effect on impedance**, **the phase-locked loop**, **efficiency and
symmetry arguments about conduction angle**, and **the quartz crystal as a
two-resonance network**. One further cluster (sampling/quantization) is a scope
decision, flagged at the bottom of the HIGH/MEDIUM list.

---

## HIGH

### 1. Feedback Sets Impedance, Not Just Gain
**ARRL asserts.** An op-amp "ideally" has infinite input and zero output
impedance; an emitter follower has high input impedance and low output impedance
(input impedance quoted as a load impedance divided by `1-α`); a common-base
stage has low input and high output impedance; a series regulator holds voltage
against load current. Each is stated as a property of the part.

**Our derivation.** These are one theorem. Take the book's existing loop
(`sec:closing-the-loop`) and compute a driving-point impedance instead of a
transfer function. Sampling the output *current* and feeding it back in series
with the input raises the input impedance to `Z_in(1+L)`; sampling the output
*voltage* and feeding it back in shunt lowers it to `Z_in/(1+L)`; a
voltage-sampled loop lowers the output impedance to `Z_out/(1+L)`. Result: the
"ideal op-amp" input and output impedances are not axioms but the `L→∞` limit of
the same `1/(1+L)` sensitivity formula the book already derives; the emitter
follower's high input impedance is the series-feedback case with `L = g_m R_E`
(ARRL's `R_L/(1-α)` is this with `1-α = 1/(1+β)`); and "good load regulation"
and "low output impedance" are literally the same number for a regulator. Keep
the gain block generic; cite the follower and common-base only as instances, so
no device physics is required.

**Where.** `17_active_circuits.tex`, new subsection in *Feedback as a Loop*,
before `sec:gbw`. Back-reference from *Op-Amp Ideals* (which currently asserts
the two impedances) and from *Power Supplies → Regulation Is a Feedback Loop*.

**Priority: HIGH.** The book already owns `1/(1+L)` and uses it for gain
sensitivity only; extending it to impedance retires four separate ARRL
assertions with one derivation and makes the op-amp ideals earned rather than
postulated.

---

### 2. The Phase-Locked Loop as a Control Loop
**ARRL asserts.** A phase detector, a low-pass loop filter, an amplifier and a
VCO form an "electronic servo loop"; the loop has a lock range and a capture
range; the loop filter and amplifier "determine the stability and tuning speed";
PLLs produce broadband phase noise.

**Our derivation.** This is the book's thesis chapter written for an actual radio
subsystem, and it is completely absent (`grep -i "PLL\|phase-locked\|VCO"` →
nothing). Start from the one physical fact that makes a PLL a control problem:
a VCO's *frequency* follows its control voltage, and phase is the integral of
frequency, so the VCO is an integrator, `Φ_out(s) = K_v V(s)/s`. With a phase
detector of gain `K_d` as the error junction and loop filter `F(s)`, the loop
gain is `L(s) = K_d K_v F(s)/s`. Everything then falls out of Ch. 5:
- the free `1/s` makes it a type-1 loop, hence *zero* steady-state phase error
  for a frequency step — which is exactly what "locked" means, derived rather
  than described;
- with a single-pole `F(s)` the closed loop is the standard second-order system
  of Ch. 3, so `ω_n` and `ζ` (equivalently loop bandwidth and damping) come
  straight from the filter constants, and the ARRL's vague "stability and tuning
  speed" becomes settling time and overshoot;
- lock range vs. capture range is the linear-model/nonlinear-model distinction:
  lock range is set by the detector's usable range and the loop's DC gain, while
  capture requires the beat note to fall inside the loop filter's passband —
  which is why capture range ≤ lock range, a fact ARRL states without reason;
- phase noise is a loop-shaping result: inside the loop bandwidth the reference's
  noise is passed and the VCO's is suppressed by `1/(1+L)`, outside it the
  reverse. That single sentence explains both the PLL's noise signature and why a
  narrow loop is quiet but slow.
Optionally add the divider `1/N` in the loop, which multiplies the VCO's noise
contribution by `N` — the real reason synthesizer phase noise degrades at high
output frequency.

**Where.** `17_active_circuits.tex`, new section after *Oscillators: Poles Placed
on the Axis*. It is the natural sequel: the oscillator chapter places poles on
the axis, the PLL section controls where on the axis they sit.

**Priority: HIGH.** Best thesis fit of anything in ARRL Ch. 6, entirely missing,
and covers E7H14/E7H15 plus the FM-modulator/demodulator role as a by-product of
the loop equations.

---

### 3. Where the Efficiency Numbers Come From (Conduction Angle, and the Switch)
**ARRL asserts.** Class A is 25–30% efficient (Ch. 17 of our book says 25% /50%),
Class B ~60%, Class C up to 80%, switching classes >90% "because the transistor is
either saturated or cut off." Also: series-regulator dissipation is
`(V_in − V_out)·I_out`, and switching regulators are more efficient.

**Our derivation.** Model the device current as a cosine truncated below the bias
point, with half-conduction angle `θ`. Fourier's `a_0` and `a_1` give the DC
input current and the fundamental output current; efficiency is
`η = ½ (a_1/a_0)(V_1/V_dc)`. Evaluating: `θ = 180°` returns `η_max = 1/2` (Class
A, and 1/4 if resistively rather than transformer coupled — which is where
ARRL's 25% comes from, currently asserted in our Ch. 17 with no reason);
`θ = 90°` returns `π/4 = 78.5%` (Class B); `θ < 90°` rises toward 100% while
`a_1` and hence output power collapse — the efficiency-vs-power trade Class C
lives on. For switching, argue from `p(t) = v(t) i(t)`: an ideal switch forces one
factor to zero at all times, so `∫p dt = 0` identically and no conduction angle
enters. Real loss is then only `I²R_on·D` plus transition loss `∝ C V² f_sw`,
which simultaneously explains why >90% is achievable *and* why switching
frequency cannot simply be raised without limit. Close by contrasting the linear
regulator, whose efficiency is exactly `V_out/V_in` because the pass element is a
"smart resistor" carrying the full load current — one line, and it makes ARRL's
Equation 6.6 obvious.

**Where.** `17_active_circuits.tex` `sec:classes` (the conduction-angle integral
and the class table), with the switching half either there or in *Power
Supplies*, where the existing text mentions duty-cycle switching but not why it
is efficient.

**Priority: HIGH.** Four numbers the book currently states on ARRL's authority
become one integral. Also the only place in the book where Fourier series of a
waveform earns its keep, which sets up item 4.

---

### 4. Why Push-Pull Cancels Even-Order Products (and Why a Balanced Mixer Suppresses the Carrier)
**ARRL asserts.** A push-pull circuit "will reduce even-order harmonics." A
balanced modulator/mixer cancels the carrier and the input signals. Both stated
as facts about the topology.

**Our derivation.** Pure symmetry, no device model needed. Let one device realize
`y = f(x)` with Taylor expansion `Σ a_n x^n`. Drive a second device with `−x` and
subtract the outputs: `y_total = f(x) − f(−x) = 2 Σ_{n odd} a_n x^n`. Every
even-order coefficient cancels *identically*, for any `f` — so the cancellation
depends on matching, not on biasing, which is why push-pull pairs are specified
matched. Two important corollaries the ARRL never draws: (i) push-pull does
**nothing** for third-order intermodulation, which is precisely the product our
Ch. 17 already identifies as the one that matters — so a push-pull linear
amplifier still needs an IMD specification; (ii) the same odd-symmetry algebra
run on a mixer's two ports is exactly why a *balanced* mixer nulls the LO and RF
feedthrough while passing the sum and difference. The book's mixer section
already lists the balanced modulator but takes the cancellation on faith.

**Where.** `17_active_circuits.tex` `sec:classes` (push-pull) with the corollary
placed in `sec:mixers` next to the existing intermodulation discussion, or as a
`physicalbox` spanning both.

**Priority: HIGH.** A three-line derivation that retires two ARRL assertions and
sharpens a claim the book already makes about third-order products.

---

### 5. The Quartz Crystal Is Two Resonances, Not One
**ARRL asserts.** A crystal is equivalent to a series-resonant LC in parallel
with the holder capacitance; its Q is 20,000 to 1,000,000; and the manufacturer
specifies a load capacitance that must be placed in parallel for the crystal to
hit its marked frequency.

**Our derivation.** The book mentions crystals only as "a resonator of very high
Q" — the network itself never appears. It is a perfect Ch. 8/9/13 exercise: form
`Z(s)` for a series `R–L_m–C_m` branch in parallel with `C_0`. The numerator
gives a series resonance `f_s = 1/(2π√(L_m C_m))` (an impedance *zero*), the
denominator a parallel resonance `f_p = f_s √(1 + C_m/C_0)` (an impedance
*pole*). Three payoffs:
- since `C_m/C_0 ≈ 1/200`, `f_p − f_s` is a few hundred ppm — this *is* the
  crystal's entire tuning range, and it explains ARRL's rule that a half-lattice
  filter's bandwidth is set by the crystals' frequency separation;
- between `f_s` and `f_p` the reactance is inductive; that narrow window is what
  a Pierce oscillator operates in, replacing the tank inductor;
- pulling: adding load capacitance `C_L` shifts the parallel resonance to
  `f_s√(1 + C_m/(C_0+C_L))`, with sensitivity `∂f/∂C_L ∝ −C_m/(C_0+C_L)²`. That
  derivative, evaluated with real numbers, is why a few picofarads of stray
  matters and why the manufacturer must specify `C_L` (E7H12) — currently an
  unexplained instruction.
Finally, back out `Q = ω_s L_m/R`: because the *motional* inductance is henries
and `R` is a few ohms, `Q` in the 10⁴–10⁶ range is arithmetic, not a material
mystery.

**Where.** `13_rlc_series.tex` as a section (it already names crystal filters in
its opening) or a `physicalbox` in `17_active_circuits.tex` at the crystal
oscillator bullet. Cross-reference from `15_filters_and_matching.tex`'s
"Crystal / cavity" family row.

**Priority: HIGH.** Directly answers E6D02 and E7H12, uses only impedance algebra
the book has, and produces a pole–zero pair — a natural companion to the existing
self-resonance discussion in Ch. 7.

---

## MEDIUM

### 6. Thermal Runaway Is a Positive-Feedback Loop with Loop Gain ≥ 1
**ARRL asserts.** Heating raises gain, which raises current, which raises heating
— "mutually reinforcing conditions" that destroy the device; an emitter resistor
creates "degenerative feedback" that prevents it.

**Our derivation.** Frame it as a DC loop and the vagueness disappears. Around an
operating point, junction temperature rise is `ΔT = θ_JA ΔP` and dissipation
responds to temperature as `ΔP = (∂P/∂T) ΔT`, so the thermal loop gain is
`L_th = θ_JA (∂P/∂T)`. `L_th < 1` is a stable equilibrium; `L_th ≥ 1` is a
real pole crossing into the right half-plane at DC — runaway is the book's own
stability criterion evaluated at `ω = 0`. Adding emitter resistance is negative
electrical feedback that divides the current sensitivity by `(1 + g_m R_E)` and
thereby scales `∂P/∂T` down below the threshold. Note the design tension the
ARRL states without explaining: the same `R_E` divides the signal gain by
`(1 + g_m R_E)`, which is exactly why a bypass capacitor is fitted — it makes the
feedback DC-only, a pole–zero split between the bias loop and the signal loop.
Deliberately avoid junction physics: the only input needed is that dissipation
increases with temperature.

**Where.** `17_active_circuits.tex`, a `controlsbox` in *Feedback as a Loop*, near
the existing sensitivity discussion.

**Priority: MEDIUM.** Very much the book's voice (loop gain at DC, positive
feedback, a pole crossing the axis), and the bypass-capacitor explanation is a
genuine insight ARRL leaves as a bare statement. Slight scope caution: keep it
device-agnostic.

---

### 7. Insertion Loss Is a Q Ratio — Which Is Why Duplexers Use Cavities
**ARRL asserts.** Passive filters always have insertion loss; cavity filters are
chosen for repeater duplexers "because of their extremely low loss and sharp
tuning."

**Our derivation.** The book states insertion loss exists and attributes it to
finite component Q, but never quantifies it. For a resonator loaded to `Q_L` from
an unloaded `Q_U`, midband insertion loss is
`IL(dB) = −20 log₁₀(1 − Q_L/Q_U)`. Two consequences worth writing down: loss
blows up as `Q_L → Q_U`, so *narrow* and *low-loss* are directly in competition
and a sharp filter demands `Q_U ≫ Q_L`; and a duplexer needs both simultaneously
(tens of dB of rejection at a few hundred kHz offset, with a transmitter's full
power passing through), which is achievable only with `Q_U` in the thousands —
i.e. a cavity or a crystal, not an LC section. That turns E7C10 from a memorized
answer into an inequality.

**Where.** `15_filters_and_matching.tex`, *Reading a Filter's Specification*,
extending the existing one-line insertion-loss remark.

**Priority: MEDIUM.** Short, quantitative, and connects loaded/unloaded Q — a
distinction the book uses in matching networks but never applies to filters.

---

### 8. Comparator Hysteresis: Positive Feedback That Splits a Threshold
**ARRL asserts.** Hysteresis is "a form of positive feedback" that moves the
setpoint a few millivolts to stop chatter on noisy inputs.

**Our derivation.** Absent from the book entirely (`grep -i hysteresis` →
nothing), and it is the one clean example of *intentional* positive feedback with
a static nonlinearity, complementing the oscillator section's intentional
marginal stability. With positive feedback fraction `β₊` around a saturating
amplifier, DC loop gain exceeds unity, so no equilibrium exists in the linear
region — the only two stable states are the saturated ones, and the switching
thresholds separate by `ΔV = β₊(V_H − V_L)`. Root-locus language: the pole is
driven into the right half-plane and the trajectory is caught by saturation. The
design rule follows: choose `ΔV` larger than the peak input noise and chatter is
impossible, not merely unlikely (E6C01/E6C02).

**Where.** `17_active_circuits.tex`, short section between *Stability, Phase
Margin, and Gain Margin* and *Oscillators*.

**Priority: MEDIUM.** Small, cheap, and the only bistable-circuit content in the
pool; strengthens the book's positive-feedback narrative.

---

### 9. Why a Filter Cannot Be Made Arbitrarily Narrow: Bandwidth and Ring-Down
**ARRL asserts.** Keep an active audio filter's Q at or below 5 and its gain at
or below 2 "to prevent unwanted filter ringing and audio instability"; ringing is
oscillation persisting beyond the input.

**Our derivation.** The book already says a second-order system rings for roughly
`Q` cycles; what is missing is turning that into a *filter design bound*. The
envelope is `e^{−ω₀t/2Q}`, so the ring-down time constant is `τ = 2Q/ω₀ = Q/(π f₀)`
and the ring duration scales as `Q/f₀` — equivalently, a filter of bandwidth `B`
smears any edge by about `1/B`, the reciprocity the ARRL never states. Numbers
make it concrete: a 900 Hz section with `Q = 5` rings for ~2 ms, tolerable; a
250 Hz CW filter has `τ ≈ 4` ms, an appreciable fraction of a fast Morse dot,
which is why very narrow CW filters *sound* like they ring and why "narrower is
always better" is false. Same argument bounds the number of cascaded sections.

**Where.** `15_filters_and_matching.tex`, *Reading a Filter's Specification* or
*Designing and Tuning a Filter*, cross-referencing Ch. 3's ringing result and
Ch. 6's group delay.

**Priority: MEDIUM.** The book has both halves (Q cycles, group delay) but never
joins them into the time/frequency trade that governs receiver filter choice.

---

### 10. The Parasitic Suppressor Is a Pole–Zero Network, Not a Mystery
**ARRL asserts.** A small resistor shunted by a small inductor, in series with a
grid or plate lead, suppresses VHF parasitic oscillation; the coil "passes HF
easily" while VHF "must pass through the resistor"; values are found
experimentally.

**Our derivation.** The impedance is `R ∥ sL = R·(s/(R/L))/(1 + s/(R/L))` — a
zero at the origin and a pole at `ω = R/L`. So it is a *high-pass impedance*:
essentially a short below `R/L`, tending to `R` above it. It therefore inserts
loss into the feedback path only above a corner the designer chooses by picking
`L` and `R`, dumping VHF loop gain below unity while leaving the HF loop
untouched. This is the same first-order RL algebra the book already uses for the
ferrite common-mode choke in Ch. 12, applied to loop gain instead of to
common-mode current — and it converts "found experimentally" into "the corner
must sit between your operating frequency and the parasitic frequency."

**Where.** `12_rl_circuits.tex` alongside *Why a Ferrite Choke Is Selective*, or
`17_active_circuits.tex` next to `sec:neutralization` (where the book already
handles the other cure for the same problem). A cross-reference either way.

**Priority: MEDIUM.** Small but exemplary: the book's simplest tool explaining a
technique the ARRL presents as empirical folklore. Pairs naturally with the
existing neutralization section, completing E7B05.

---

### 11. What "Dip the Plate, Then Load It" Actually Adjusts
**ARRL asserts.** Adjust the tuning capacitor for minimum plate current, then the
loading capacitor for maximum permissible plate current; repeat because the
adjustments interact.

**Our derivation.** Two knobs, two already-derived facts. Tuning sets resonance:
at `f₀` the parallel tank's impedance is real and *maximal* (Ch. 14), so the
device sees the largest load and draws the least DC current — the "dip" is the
book's parallel-resonance peak observed on a DC ammeter. Loading sets the
transformation ratio: the π network is two back-to-back L-networks (Ch. 15), and
`C₂` moves the virtual resistance `R_v`, hence both the resistance presented to
the device and the loaded `Q = √(R_max/R_v − 1)` the book already derives. The
interaction ARRL notes is not mysterious — `R_v` and `ω₀` are both functions of
`L`, `C₁`, `C₂`, so moving either capacitor moves both quantities, which is
exactly why the procedure iterates. Also worth stating: dip and load are
*resonance* and *impedance match*, two of the book's distinct ideas, and the
mistake box in Ch. 15 warning that matching ≠ filtering applies verbatim.

**Where.** `15_filters_and_matching.tex`, *Pi and T Networks*, as a `workedbox`
or `physicalbox`.

**Priority: MEDIUM.** Uses only results the book has; the value is entirely in
naming which existing result each knob moves (E7B09, E7C12).

---

### 12. Sampling and Quantization — ⚠️ SCOPE DECISION, NOT AUTHORIZED
**Flag first.** DSP is thin in the book by acknowledged omission rather than by
principle, and nothing here should be written until the user decides whether to
open the topic. Currently the only traces are an aside in
`05_feedback.tex` distinguishing the two Nyquists, a passing "anti-aliasing path"
in Ch. 15, and two table rows in Ch. 15 asserting that FIR filters "can be
exactly linear phase" and IIR filters cannot. Those two rows are already
unsupported claims in our own book, which is the strongest argument for opening
the topic — and the strongest argument for *not* opening it is that doing it
properly is a chapter, not a section.

**ARRL asserts.** Sample at ≥ 2× the highest frequency (Nyquist), aliases "are as
real as the fundamental" and cannot be filtered out afterward, an 8-bit converter
gives 256 levels, ADC resolution sets the minimum detectable signal, decimation
requires an anti-aliasing filter beforehand but interpolation does not, and FIR
filters delay all frequency components equally while IIR filters do not.

**What we would derive.**
- *Sampling is multiplication.* ARRL itself notes sampling is "equivalent to a
  mixing process." The book's mixer section already derives that multiplying two
  sinusoids produces sum and difference frequencies — so multiplying by an
  impulse train (a sum of harmonics of `f_s`) produces sum-and-difference copies
  of the whole spectrum around every multiple of `f_s`. Spectral replication and
  Nyquist's `f_s > 2f_max` then follow as a non-overlap condition, and aliasing
  is *folding about `f_s/2`*, which shows why it is irreversible: two input
  frequencies map to identical sample sequences, so no filter can separate them.
  This is a genuinely cheap extension of existing material.
- *Quantization noise and the 6 dB/bit rule.* Step `Δ = V_FS/2^N`; a uniform
  error on `[−Δ/2, Δ/2]` has variance `Δ²/12`; comparing to a full-scale sine
  gives `SNR = 6.02N + 1.76` dB. That single formula gives ARRL's 256 levels,
  its 10-bit/1 V ≈ 1 mV resolution example (E7F06), and its assertion that
  converter resolution sets the minimum detectable signal (E7F11) — plus it
  explains dither, which trades bandwidth for resolution by making the error
  noise-like and averageable.
- *Decimation.* Dropping every `n`th sample lowers `f_s`, hence lowers the fold
  frequency, so content that was legal becomes aliased — the anti-alias filter is
  required *before* the rate change, and interpolation needs none because raising
  `f_s` moves the fold frequency away. Two lines from the folding picture.
- *Linear-phase FIR.* A symmetric coefficient set gives
  `H(e^{jω}) = (real function of ω) · e^{−jω(N−1)/2}`, i.e. phase strictly linear
  in `ω`, i.e. constant group delay `(N−1)/2` samples — the book's own Ch. 6
  group-delay definition, now proved for the case Ch. 15 currently asserts. The
  IIR contrast is immediate: poles off the origin mean phase that is not linear.
- *Reconstruction.* A DAC's stairstep is a zero-order hold, whose transfer
  function is a `sinc` — so the "reconstruction filter" removes images *and*
  compensates a known droop.
- Optional and cheapest of all: DDS output frequency `f_out = f_clk·M/2^N` from
  the phase accumulator, with spurs traced to phase truncation.

**Where.** A short new chapter after Ch. 15, or a Part IV section. Not a
paragraph bolted onto an existing chapter — the derivations above are cumulative.

**Priority: HIGH *if* the scope question is answered yes; otherwise deferred.**
It is the single largest genuinely uncovered block in ARRL Ch. 6, it maps to a
whole pool subelement (E7F, E8A), and two claims already made in Ch. 15 depend on
it. But it is the one item here that changes the book's boundaries, so it needs
the user's decision before drafting.

---

## Considered and rejected

**Already covered — verified in the text, not just the TOC:**

| ARRL topic | Where the book already has it |
| --- | --- |
| Odd- vs. even-order intermodulation, `mf₁±nf₂`, two-tone test | `17_active_circuits.tex` `sec:mixers` — derived, with the 14.20/14.21 MHz worked case |
| Mixer sum/difference; balanced modulator, product detector, frequency multiplier as one circuit | `17_active_circuits.tex` *The Same Multiplier, Four Jobs* |
| Butterworth / Chebyshev / elliptic / Bessel families, ripple-vs-sharpness, `|G|²` specifications, pole placement, section-Q table | `06_higher_order.tex` `sec:poleplacement`; `15_filters_and_matching.tex` family table + figure |
| Shape factor, skirts, order vs. −20n dB/decade, passband/stopband/notch definitions | `15_filters_and_matching.tex` specification table; `06_higher_order.tex` |
| Op-amp ideals, virtual ground, inverting/non-inverting gain, β from resistors, offset-free ideal | `17_active_circuits.tex` *Op-Amp Ideals* (all four E7G gain examples reduce to `−R_f/R_1`) |
| Gain-bandwidth product, unity-gain frequency, open-loop gain falling with frequency | `17_active_circuits.tex` `sec:gbw`, derived from the first-order feedback result with a worked example |
| Oscillator loop conditions, Barkhausen, Colpitts/Hartley/Pierce, crystal → low phase noise, amplitude limiting | `17_active_circuits.tex` *Oscillators: Poles Placed on the Axis* |
| Neutralization, interelectrode feedback capacitance | `17_active_circuits.tex` `sec:neutralization` |
| Active filters, Sallen–Key, capacitor ratio sets Q, why active filters fail at RF | `17_active_circuits.tex` *Active Filters and Their Limits* |
| Class A/B/AB/C conduction angles and the linearity-efficiency trade; Class C tank restoring the sinusoid | `17_active_circuits.tex` `sec:classes` (the *numbers* are not derived — see item 3) |
| L / π / T networks, matching = cancel reactance then transform R, L-network Q fixed by ratio while π and T set Q freely | `15_filters_and_matching.tex` *Impedance Matching* |
| Transformer turns ratio and impedance-squared law; core saturation | `15_filters_and_matching.tex` *Transformers* |
| Rectification, half- vs. full-wave ripple frequency, filter as low-pass, bleeder as RC discharge, equalizing resistors across series capacitors | `17_active_circuits.tex` *Power Supplies* |
| Regulation as a feedback loop; line/load regulation as `1/(1+L)`; regulator ringing | `17_active_circuits.tex` *Regulation Is a Feedback Loop* |
| Ringing as underdamped second-order response, ~Q cycles | `03_modeling_lti_systems.tex`, `04_s_plane_poles_and_zeros.tex` (the *filter design bound* is not — see item 9) |
| Group delay, linear phase, waveform fidelity | `06_higher_order.tex` `sec:groupdelay` |
| Decibels, voltage vs. power gain | `04_s_plane_poles_and_zeros.tex` `sec:decibels` |
| Insertion loss exists because components have finite Q | `15_filters_and_matching.tex` (asserted only — quantified in item 7) |

**Out of the book's declared scope:**
- AM/SSB/DSB-SC spectra, filter-method and quadrature/phasing SSB generation,
  FM vs. PM, reactance modulators, deviation multiplication, pre-emphasis and
  de-emphasis, baseband — all modulation theory, explicitly excluded.
- Envelope/diode detectors, FM discriminators, BFO placement — demodulation, same
  exclusion. (The product detector survives only as a mixer identity, already in
  Ch. 17.)
- I/Q representation and the Hilbert transform — modulation theory *and* DSP;
  even if DSP opens, this belongs to modulation.
- BJT common-emitter/base/collector identification, R1/R2 divider bias, the
  Q-point, `r_e = 26 mV/I_e`, `A_V = −R_C/(R_E + r_e)`, α and β, tube-electrode
  correspondences, grounded-grid characteristics — semiconductor/tube device
  behavior and schematic identification, both excluded. Only the *feedback* content
  of these circuits is proposed, as items 1 and 6.
- Piezoelectricity, crystal cuts, crystal ovens, NP0 temperature coefficients,
  microphonics and mechanical isolation — materials and construction practice.
  (The crystal's *electrical network* is proposed as item 5.)
- SDR system architecture, direct digital conversion block diagrams, sound-card
  vs. embedded SDR, adaptive/automatic notch filters, GPS-disciplined and rubidium
  references, charge controllers, PCB disposal — equipment description, protocols,
  or safety.
- Mechanical and cavity filter *construction*; only the Q argument is proposed
  (item 7).

**In scope but not worth deriving:**
- Series regulator dissipation `P = (V_in − V_out)I_out` and efficiency
  `V_out/V_in` — one line each; folded into item 3 rather than given their own slot.
- Dropout voltage — genuinely explicable as actuator saturation opening the loop,
  but it is one sentence; suggest adding it inside the existing *Regulation Is a
  Feedback Loop* text rather than as a standalone proposal.
- Step-start inrush limiting — an RC charging current limit the book has already
  derived four times; a one-clause mention at most.
- The FFT — an algorithmic complexity result with no circuit content; even under
  an expanded DSP scope, mention only.
- Shunt vs. series regulator comparison, stage/driver/final/loading vocabulary,
  active vs. passive mixer conversion loss — definitions, nothing to derive.
