# ARRL Chapter 7 → Book Gap Audit

Source: ARRL Extra Class License Manual, Ch. 7 (7.1 Test Equipment, 7.2 Receiver
Performance, 7.3 Interference and Noise). Concepts paraphrased only.

**Headline finding.** The predicted gap is real and it is the largest single hole in the
book. Greps over `chapters/*.tex` return **zero hits** for `noise figure`, `noise floor`,
`kTB`, `174`, `MDS`, `thermal noise`, `Boltzmann`, `Johnson`, `Friis`, `SINAD`, `SNR`,
`signal-to-noise`, `dynamic range`, `intercept`, `compression`, `desens`, `noise
bandwidth`, `white noise`, `Taylor`, `attenuator` (except a probe aside). ARRL asserts
every one of these numbers — −174 dBm/Hz, the 3 dB/dB slope, the (2/3) in the IMD DR3
formula, "add noise figure to the theoretical floor" — with no derivation whatsoever, and
in one place explicitly punts the calculation to the *Handbook*. The book already owns
every prerequisite: RMS and average power (`02`, `09`), maximum power transfer (`08`),
`|H(jω)|` for one- and two-pole filters (`04`, `11`, `13`), cascades adding in dB (`06`),
dBm and link budgets (`18`), and the mixer product-to-sum expansion with `2f1−f2` and the
two-tone test (`17`, lines 495–605).

**Structural recommendation.** Items H1–H5 plus M4 and M6b form a coherent new chapter,
**"Noise, Sensitivity, and Dynamic Range,"** placed after Ch. 17 (Active Circuits) and
before Ch. 18 (Measurement). It is receiver *theory*, not bench technique, and Ch. 18 was
just expanded and should not absorb it. H3 belongs partly inside `17_active_circuits.tex`
(extending `sec:mixers`), which is where the two-tone algebra already lives.

---

## HIGH

### H1. Thermal noise: where −174 dBm/Hz actually comes from
**ARRL asserts:** the theoretical noise power at an ideal receiver input in a 1 Hz
bandwidth is −174 dBm at room temperature, that noise power grows linearly with
bandwidth, and that MDS is the level giving a 0 dB SNR (found on the bench as a 3 dB rise
in audio output). It states the number and refers the reader elsewhere for why.

**Our derivation:** start from the Johnson–Nyquist open-circuit noise voltage of a
resistor, `v_rms = sqrt(4 k T R B)`. Then apply the book's own maximum-power-transfer
result (`08_series_parallel_networks.tex`, "Power Transfer and Matching"): a matched load
sees half the voltage, so the **available** noise power is
`P_n = (v_rms/2)^2 / R = k T B` — the factor of 4 in the voltage formula exists precisely
so the available power comes out clean, which is worth saying out loud. Evaluate at
`T_0 = 290 K`: `k T_0 = 4.00e-21 W/Hz`, and `10 log10(4.00e-21 / 1e-3) = −173.98`, so
**−174 dBm/Hz**, with the temperature dependence visible (300 K gives −173.8). The
bandwidth law is then `10 log B` by inspection, not by assertion: 500 Hz costs 27 dB, 400
Hz costs 26 dB. Close with two short corollaries: (i) the 3 dB test is just `S = N ⇒ S+N =
2N`, i.e. equal powers add to twice the noise alone; (ii) the µV↔dBm bridge, `P = V²/R`
with R = 50 Ω, so `P_dBm = 20 log10(V_µV) − 107`, which reproduces ARRL's 0.5 µV ↔
−113 dBm and lets the reader move between the two conventions receivers are specified in.

**Goes in:** new chapter, opening section.
**Priority: HIGH** — it is the origin of every other number in ARRL 7.2, and it is a
five-line derivation that reuses the book's matched-load result.

### H2. Noise figure, noise temperature, and the Friis cascade
**ARRL asserts:** noise figure is the ratio of internally generated noise to the
theoretical MDS, lower is better, and you get a receiver's actual noise floor by *adding*
the noise figure in dB to the theoretical floor (its Equation 7.2). No account of why
addition is the right operation, and no treatment at all of where in a chain the noise
figure is set.

**Our derivation:** define `F ≡ SNR_in / SNR_out` with the source at `T_0`. Writing total
output noise as `N_out = G k B (T_0 + T_e)` gives `F = 1 + T_e/T_0`, which makes ARRL's
addition a theorem: `floor = −174 + 10 log B + NF`, because F multiplies a power ratio and
dB turn multiplication into addition (the same move as `sec:cascadeadd` in `06`). Then
cascade two stages — referring stage 2's excess noise back through `G_1` —
`N_out = G_1 G_2 k B (T_0 + T_e1 + T_e2/G_1)`, hence **Friis**:
`F = F_1 + (F_2−1)/G_1 + (F_3−1)/(G_1 G_2) + …`. Three consequences ARRL never draws:
the first stage dominates and everything after it is discounted by the accumulated gain;
a passive loss of `L` ahead of the receiver has `F = L`, so *n* dB of feedline loss costs
*n* dB of noise figure directly; and therefore a mast-mounted preamp helps while the same
preamp in the shack largely does not. Contrast this with the *signal* link budget of
`sec:decibels` in `18` — that chain adds gains and losses, this chain weights them.

**Goes in:** new chapter, second section; cross-reference `18`'s link budget and `16`'s
line attenuation `α`.
**Priority: HIGH** — turns an asserted formula into a derived one and yields the
"where do I put the preamp" result, which the book's link-budget material sets up but
cannot currently answer.

### H3. One power series generates every dynamic-range number
**ARRL asserts:** second-order products change 2 dB per dB of input and third-order
products 3 dB per dB; intercept points exist and can be extrapolated; the blocking level
is where gain has fallen 1 dB. All four are stated as brute facts, with a figure.

**Our derivation:** model the weak nonlinearity as a truncated power series
`y = a_1 x + a_2 x² + a_3 x³` — the honest generalization of the book's existing statement
that a mixer "does not multiply cleanly" (`17_active_circuits.tex:564`). Drive it with
`x = A(cos ω_1 t + cos ω_2 t)` and expand using the *same* product-to-sum identity already
used at `17:507`. Three results fall out of one expansion:
- The `2ω_1 − ω_2` term has coefficient `(3/4) a_3 A³` → amplitude ∝ `A³` → **3 dB per
  dB**; the `ω_1 ± ω_2` term is `a_2 A²` → **2 dB per dB**. The slopes are the exponents,
  and the exponents are the series order. Nothing to memorize.
- The fundamental's own coefficient becomes `a_1 + (3/4) a_3 A²` (single tone; `(9/4)` for
  two equal tones). With `a_3` opposite in sign to `a_1`, gain *falls* with drive — that
  **is** gain compression, blocking, and desensitization, all one term. Setting the
  bracket to `10^(−1/20) a_1 = 0.891 a_1` gives `A_1dB² = 0.145 |a_1/a_3|`.
- Equating the IM3 amplitude to the fundamental, `(3/4)|a_3| A³ = a_1 A`, gives the
  **input third-order intercept** `A_IIP3² = (4/3)|a_1/a_3|`. Dividing the two boxed
  results: `IIP3 = P_1dB + 9.6 dB` for a pure cubic — a rule of thumb the ARRL does not
  mention and that our algebra hands over for free. It also explains why the intercept is
  a fiction: it is the extrapolation of two straight lines to a level (ARRL's 40 dBm = 10
  W) that would destroy the receiver, so it is a *linearity coefficient* expressed as a
  power, nothing more.

**Goes in:** the expansion itself extends `sec:mixers` in `17_active_circuits.tex`,
immediately after the existing "Intermodulation" paragraph; the named metrics
(P_1dB, IIP2, IIP3) go in the new chapter.
**Priority: HIGH** — one derivation replaces four ARRL assertions and directly serves
E4D01/E4D02/E4D10/E4D11/E4D12. It is also the book's thesis in miniature: the metrics are
consequences of the model, and the model is three coefficients.

### H4. The (2/3) in the IMD dynamic range formula
**ARRL asserts:** `IMD DR3 = (2/3)(IP3 − MDS)`, given as Equation 7.8 with no explanation
of the coefficient, and blocking dynamic range as a plain difference.

**Our derivation:** from H3's slopes, the IM3 product referred to the input obeys
`P_IM3 = 3 P_in − 2·IIP3` in dB (check: at `P_in = IIP3` it returns `IIP3`, as it must).
Define the dynamic range as the input level at which the products just break the noise
floor, `P_IM3 = MDS`. Solve: `P_in = (2·IIP3 + MDS)/3`, so
`DR3 = P_in − MDS = (2/3)(IIP3 − MDS)`. The 2/3 is the slope-3 geometry and nothing else —
and the same argument with slope 2 gives `DR2 = (1/2)(IIP2 − MDS)`, a generalization ARRL
omits. Blocking dynamic range is `BDR = P_1dB − MDS`, a plain subtraction *because*
blocking is a 1:1 phenomenon; putting the two side by side explains why they are not the
same number and why they are quoted separately.

**Goes in:** new chapter, immediately after H3's metrics.
**Priority: HIGH** — a two-line derivation that removes a memorized magic constant, and
the natural home for a worked example computing MDS, floor, BDR and DR3 for one receiver.

### H5. Reciprocal mixing, and the phase-noise skirt from pole location
**ARRL asserts:** excessive LO phase noise lets strong nearby signals raise the apparent
noise floor as you tune toward them, and calls this reciprocal mixing. It attributes phase
noise to DDS artifacts and stops there. Our `17_active_circuits.tex:404` has a good
*qualitative* box ("phase noise is the frequency-domain fingerprint of how firmly the poles
are pinned to the axis") — the gap is that it is never made quantitative and reciprocal
mixing is absent entirely.

**Our derivation:** two steps, both using tools already in the book.
1. *Where the sidebands come from.* Write the LO as `cos(ω_LO t + φ(t))` and expand for
   small `φ`: `≈ cos ω_LO t − φ(t) sin ω_LO t`. A pure carrier plus a noise term in
   quadrature — so a phase-modulated oscillator is a line *plus* skirts, and the skirt
   power spectral density at offset `Δf` is just `S_φ(Δf)`, quoted in dBc/Hz.
2. *Why it raises the floor.* The mixer multiplies, so a strong interferer at offset `Δf`
   from the tuned frequency beats against the LO's skirt component at that same offset and
   lands **inside** the IF passband as noise, at level
   `P_int + L(Δf) + 10 log B`. Setting that equal to the MDS of H1 defines a *reciprocal-
   mixing dynamic range*, `−L(Δf) − 10 log B` — which shows the effect worsens as you tune
   closer (the skirt rises) and that it is a noise-floor problem, not a distortion problem,
   which is exactly why it is a separate specification from H4's.
3. *Where the skirt shape comes from.* The oscillator's tank filters its own internal
   noise with the single-pole roll-off of half-bandwidth `ω_0/2Q_L` that Ch. 13 already
   derives, so above that corner the phase noise falls at −20 dB/decade and its level
   scales as `1/Q_L²`. That is the Leeson picture, and it converts the existing
   qualitative box into a number: doubling loaded Q buys 6 dB. It also explains why
   loading an oscillator tank (already a cross-chapter problem, `21:64`) is a phase-noise
   decision.

**Goes in:** new chapter for the reciprocal-mixing budget; the `1/Q_L²` slope result
upgrades the `physicalbox` at `17_active_circuits.tex:403–409`.
**Priority: HIGH** — it is the one receiver metric that is *purely* a pole-location
statement, so it is the most on-thesis item in the whole ARRL chapter, and the book is
already 80% of the way there.

### H6. Noise bandwidth ≠ −3 dB bandwidth, and why filter width should match signal width
**ARRL asserts:** widening a filter admits noise in proportion to bandwidth; an IF
bandwidth slightly greater than the signal's bandwidth maximizes SNR while minimizing
interference; a table of recommended bandwidths per mode. The `10 log B` scaling is applied
to a receiver's *nominal* −3 dB bandwidth as if the two were the same thing.

**Our derivation:** noise through a filter is `N = N_0 ∫|H(f)|² df`, so the honest figure
is the **equivalent noise bandwidth** `B_n = ∫|H|² df / |H|²_max`. Do the integral on the
book's own one-pole response (`11_rc_circuits.tex`): `∫ df/(1+(f/f_c)²) = (π/2) f_c`, so
`B_n = 1.57 f_3dB` — a single-pole filter is **1.96 dB noisier** than its nameplate
bandwidth suggests. Tabulate the Butterworth ratio `(π/2n)/sin(π/2n)`: 1.571, 1.111,
1.047, 1.026 for n = 1…4, i.e. sharper skirts make nameplate and noise bandwidth converge
— a second, independent reason to add poles that the filter chapter does not currently
give. Then the SNR optimum: `SNR(B) = S(B)/(N_0 B)`, where `S(B)` saturates once `B`
exceeds the signal's occupied bandwidth while the denominator keeps growing, so the
maximum sits at `B ≈ B_signal`. Too wide costs `10 log(B/B_signal)`; too narrow truncates
signal energy. ARRL's mode-by-mode table stops being a list to memorize.

**Goes in:** `B_n` and the Butterworth table extend `sec:filterspecs` in
`15_filters_and_matching.tex` (which currently lists cutoff, insertion loss, ripple,
ultimate rejection, shape factor — noise bandwidth is the missing sixth row); the SNR
optimum goes in the new chapter.
**Priority: HIGH** — cheap, uses an integral the book can already do, and it corrects a
conflation the ARRL text actively encourages.

---

## MEDIUM

### M1. Fourier series: the missing justification for the book's own method
**ARRL asserts:** Fourier analysis "shows" a square wave to be a fundamental plus all odd
harmonics, and a sawtooth/ramp to contain all harmonics. Stated as a fact about waveforms,
with a spectrum-analyzer picture and no argument.

**Our derivation:** the book analyzes everything one sinusoid at a time and never says why
that is general. Fill the hole: for periodic `x(t) = Σ c_n e^{j n ω_0 t}`, LTI
superposition gives `y(t) = Σ G(j n ω_0) c_n e^{j n ω_0 t}` — *the transfer function
evaluated at the harmonics is the whole answer*, which is the licence for Part II's entire
method and belongs stated once. Then get ARRL's two facts from symmetry rather than from a
picture: a square wave satisfies `x(t + T/2) = −x(t)`, and that half-wave symmetry forces
every even coefficient to vanish, leaving `x = (4/π) Σ_{n odd} sin(n ω_0 t)/n`; a ramp has
no such symmetry, so all harmonics survive, again with `1/n`. Two payoffs: the `1/n`
envelope is −20 dB/decade, so a square wave's spectrum has the same slope as a one-pole
filter and for the same reason (a discontinuity is the time-domain signature of a slow
spectral roll-off); and "harmonic distortion" is now a statement about which `c_n` a
nonlinearity creates, linking directly to H3.

**Goes in:** a new section in `03_modeling_lti_systems.tex` (right after "Four Equivalent
Views" / superposition), referenced from the measurement chapter.
**Priority: MEDIUM** (borderline high) — it is a foundational gap of the book's own
making rather than a new topic, and it is short.

### M2. Parseval, form factor, and why a cheap meter lies
**ARRL asserts:** true-RMS meters are the accurate choice for complex waveforms because
they do the full calculation; averaging meters assume a sine wave and are wrong on
non-sinusoids, pulses, or waveforms with DC offset.

**Our derivation:** `02_complex_numbers_and_phasors.tex:104–125` already defines RMS from
the integral and already warns that 0.707 is sinusoid-only (square → 1.0, triangle →
1/√3). Two things are missing. First, **Parseval**: combining that definition with M1's
series gives `X_rms² = X_dc² + Σ_n X_{n,rms}²` — RMS contributions add *in quadrature over
harmonics*, which is both why a true-RMS meter is the only correct instrument for a
distorted wave and, as a free byproduct, the definition of THD,
`sqrt(Σ_{n≥2} X_n²)/X_1`. Second, **form factor**: an averaging meter actually measures
`mean|x|`, and is calibrated by the sine's ratio `(V_p/√2)/(2V_p/π) = 1.111`. Any other
waveform has a different form factor, so the error is computable rather than vague — a
square wave has form factor 1.000, so a sine-calibrated averaging meter reads it
**11% high**. That number is the whole content of ARRL's warning, and it takes one line.

**Goes in:** a subsection of `sec:rms` in `02`, with the meter consequence noted in `18`.
**Priority: MEDIUM** — small, exact, and it makes an existing `mistakebox` quantitative.

### M3. Time–bandwidth: why arcs are broadband and a noise blanker cannot be narrow
**ARRL asserts:** an arc radiates RF energy across the spectrum because the current
through ionized air is irregular; and a noise blanker must detect signals across a wide
bandwidth (hence cannot sit behind the narrow IF filter, hence can be fooled by strong
signals), and the main IF path must be delayed to match the detector.

**Our derivation:** one Fourier-transform pair explains all of it. A rectangular pulse of
width `τ` transforms to `τ sinc(π f τ)`, essentially flat out to `f ≈ 1/(2τ)`: a
microsecond-scale arc is therefore flat across the whole HF spectrum, which is *why*
impulsive sources are broadband — not because the arc is "irregular" but because it is
*short*. Run the same relation backwards for the blanker: passing a pulse of width `τ`
requires `B ≳ 1/τ`, so a detector behind a 500 Hz filter sees the pulse smeared to
milliseconds and can no longer time the gate — hence the wideband sniff path, hence the
compensating delay in the main path, hence the vulnerability to strong in-band signals
that the wide path cannot reject. Same inequality, three consequences.

**Goes in:** new chapter (a short "impulsive noise" section) or `18`; cross-reference
M1 and `06`'s group-delay section.
**Priority: MEDIUM** — genuinely explanatory, in scope (signals and spectra, not DSP
algorithms), and it rescues the one part of ARRL 7.3 that is not operating practice.

### M4. Quantization noise: 6.02N + 1.76 dB, and what actually limits an SDR
**ARRL asserts:** an SDR's strong-signal performance is largely set by ADC sample width —
more bits means a larger linear range — and the receiver is overloaded when the input
exceeds the converter's reference voltage. No quantitative link between bits and dB.

**Our derivation:** a uniform quantizer with step `Δ = V_FS/2^N` has error approximately
uniform on `[−Δ/2, Δ/2]`, so its mean-square value is `Δ²/12`. Compare a full-scale sine,
`V_FS²/8`. The ratio gives `SNR = 6.02 N + 1.76 dB` — **6 dB per bit**, which is
pleasingly the same 6 dB as one S unit (`18`, sec:decibels), so a bit of ADC and an S unit
are the same factor of four in power. Then add the piece ARRL omits: quantization noise is
spread over `f_s/2`, so decimating to a receive bandwidth `B` recovers
`10 log(f_s/2B)` dB of processing gain, which is why an SDR's in-band dynamic range beats
its raw converter spec and why oversampling is worth silicon. Finally, note the asymmetry
of the two ends: the floor is soft and improvable by processing gain, the clipping ceiling
at the reference voltage is hard — no graceful compression as in H3, which is exactly why
ARRL says analog and SDR receivers "behave differently" under overload.

**Goes in:** new chapter, final section; cross-reference `05_feedback.tex:249–256` (which
already distinguishes the two Nyquists and mentions the anti-alias filter).
**Priority: MEDIUM** — clean derivation, answers E4C08/E4C12, and it sits naturally beside
H1's noise floor as "the other floor."

### M5. Frequency-counter resolution: ±1 count plus a ppm
**ARRL asserts:** counter accuracy depends on the crystal time base, error is quoted in
ppm, and gives a maximum-displayed-error expression without deriving it. It also describes
the prescaler purely as a way to reach higher frequencies.

**Our derivation:** the counter reports `f̂ = N/T_gate` with `N = floor(f·T_gate)`, so the
`±1`-count ambiguity is an absolute resolution of `±1/T_gate` **independent of the
frequency being measured** — a 1 s gate resolves 1 Hz whether the input is 1 kHz or 1 GHz,
and a 0.1 s gate resolves only 10 Hz. Superposed on that is a *fractional* error
`f·(δ×10⁻⁶)` from a δ-ppm time base, which scales with frequency. Adding the two
reproduces ARRL's expression and, more usefully, locates the crossover at
`f = 10⁶/(δ·T_gate)`: below it you are quantization-limited (buy a longer gate), above it
you are reference-limited (buy a better crystal). Add one sentence on the prescaler: a
divide-by-M ahead of the counter multiplies the effective quantization error by M, which is
the price of the extra range. Note explicitly that this is the *same* one-count argument as
M4's half-LSB, applied to time instead of amplitude.

**Goes in:** `18_measurement_and_troubleshooting.tex`, a short section beside the meter and
probe material.
**Priority: MEDIUM** — small but it is a real derivation of an asserted formula, and it
gives Ch. 18 the accuracy-vs-resolution distinction ARRL only defines in a vocabulary
sidebar.

### M6. Aliasing on the bench: the fold-back frequency, and the attenuator corollary
Two small items, each a short extension of something the book already has.

**(a) Fold-back.** *ARRL asserts:* a digital scope's usable bandwidth is limited by
sample rate, and too slow a time base produces a false, jittery low-frequency alias.
*Our derivation:* `05_feedback.tex:249–256` already names aliasing and the anti-alias
filter but never gives the formula. Sampling multiplies by an impulse train, whose spectrum
is a comb at `n f_s`, so the input spectrum replicates at every `n f_s` and any component
above `f_s/2` appears at `f_alias = |f − n f_s|`. That single expression predicts the
jittery slow artifact (small `|f − n f_s|` when `f` is near a comb line) and explains why
the practical alias-free bandwidth is *below* `f_s/2`: the anti-alias filter has finite
skirts, which is H6's order argument again. *Goes in:* `18`, two paragraphs, cross-linked
to `05`.

**(b) The attenuator corollary.** *ARRL asserts:* an input attenuator reduces overload on
the low HF bands with little SNR penalty, and separately that attenuation is a remedy for
IMD. *Our derivation:* both follow from H2 and H3 in two lines. From H3's slopes, `L` dB of
input attenuation drops the wanted signal by `L` and the third-order product by `3L`, so
the product-to-signal ratio improves by `2L` dB — attenuation buys linearity at twice the
rate it costs signal. And from H2, the attenuator raises the receiver's noise figure by `L`
dB, which is *free* whenever external atmospheric noise already dominates the receiver's
own contribution, because then signal and noise are attenuated identically and the SNR is
untouched. Two ARRL assertions, one page apart, are the same two facts.
*Goes in:* a worked example closing the new chapter.

**Priority: MEDIUM** for both — neither is a new topic, but (b) in particular is the kind
of "the assertion was a corollary" payoff the book is built around.

---

## CONSIDERED AND REJECTED

**Already covered in the book:**
- *Image response, and why a high IF helps.* Derived in `17_active_circuits.tex:523–541`,
  including `f_image − f_signal = 2 f_IF` and the up-converting-receiver conclusion. ARRL's
  455 kHz / 14.300 MHz arithmetic adds nothing.
- *Third-order product frequencies and the two-tone test.* `17_active_circuits.tex:564–595`
  gives `2f_1−f_2`, `2f_2−f_1`, the worked 14.20/14.21 MHz case, the even-vs-odd-order
  asymmetry, and a `physicalbox` on why two tones rather than one. Better than ARRL's
  four numbered equations. (Only the *amplitude* behaviour was missing — that is H3.)
- *PEP, and PEP-to-average ratio.* `09_ac_steady_state.tex:293–345` derives
  `PEP = V_pp²/(8R)`, the unmodulated-carrier limit of 1.00, and states that the ratio
  depends entirely on the modulation. ARRL's 2.5:1 and 3:1 figures are speech-statistics
  and compressor practice — modulation/operating, excluded by the preface.
- *RMS as the heating-equivalent value.* `02_complex_numbers_and_phasors.tex:96–125`,
  including the sinusoid-only caveat. Only Parseval and form factor are new (M2).
- *Voltmeter sensitivity in Ω/V.* `18_measurement_and_troubleshooting.tex:33–75` already
  works a `20 kΩ/V` analog meter against a 688 Ω and a 1 MΩ node. The *term* "sensitivity"
  is absent; that is a one-clause edit, not a derivation.
- *Scope probe compensation.* `18`, `sec:probe`, derives it as pole–zero cancellation with
  a figure — substantially deeper than ARRL's "adjust for flat tops on the square wave."
- *Short probe ground lead at high frequency.* `18`, "Ground-Lead Inductance: an Accidental
  Resonator."
- *Common-mode current, common-mode chokes, ferrite mix choice, why a toroid.* `12_rl_circuits.tex`,
  "Ferrites and Common-Mode Current" (both subsections). Covers ARRL's E4E07/E4E08 material.
- *Brute-force AC line filter.* A low-pass filter; `15_filters_and_matching.tex` covers the
  mechanism, and there is nothing specific to derive about the topology.
- *Preselectors, front-end band-pass filters, roofing filters as circuits.* Band-pass
  filters, fully covered by `15`. The only uncovered content is *why* they improve dynamic
  range, which is the IP3/blocking story — folded into H3/H4 rather than listed separately.
- *Shape factor / skirt steepness.* `15`, `sec:filterspecs`, including the Chebyshev
  trade. (Noise bandwidth is the genuinely missing row — H6.)

**Out of scope per the preface:**
- *Capture effect, limiters, discriminators, FM's noise behaviour* — modulation theory.
- *Logic analyzers, logic-level display, bus capture* — digital logic.
- *DSP noise reduction, adaptive filters, automatic notch filters* — DSP algorithms. (The
  in-scope kernel about impulse noise is M3; the auto-notch-eats-CW failure mode is an
  algorithm artifact with no circuit-theoretic content.)
- *Power-line noise hunting, breaker-by-breaker bisection, contacting the utility, RF
  sniffers, ultrasonic arc detectors* — operating and troubleshooting practice.
- *Vehicle noise: ignition leads, alternator, bonding the radio to the battery; computer
  and switching-supply interference* — installation practice. The generic mechanism (a
  short pulse is broadband) is M3; the cures are not circuit theory.
- *Repeater intermod arithmetic (181.25 − 36.4 = 144.85), SSB splatter as an on-air
  courtesy issue* — arithmetic on a formula already in `17`, plus operating practice.

**In scope but not worth deriving:**
- *Circulators and isolators.* Nonreciprocal ferrite devices; the book has no
  S-parameter or magnetostatic machinery, and none of its existing tools produce the
  behaviour. The one in-scope nugget — an isolator presents the transmitter a matched load
  regardless of antenna `Γ`, because the reflected wave is routed to a dummy load — is at
  most one sentence appended to `16`'s reflection-coefficient section, not a proposal.
- *Accuracy vs precision vs resolution; percent-of-full-scale specs.* Metrology vocabulary
  with nothing to derive. Worth one sentence in `18` noting that M4's half-LSB and M5's
  ±1-count arguments *are* the quantitative versions of "resolution."
- *SINAD.* A definition (distortion counted with the noise); adds nothing beyond H1's SNR.
- *Prescalers.* A frequency divider; its only quantitative consequence is the ×M
  resolution penalty, folded into M5.
- *Spectrum-analyzer block diagram, swept superhet tuning, scan width, dB/div, ARRL Lab
  test setups.* Instrument operation. The one theoretical idea underneath it — that a
  periodic signal *is* a set of harmonics — is M1.
- *WWV/WWVH checking and ppm bookkeeping* — operating practice; the error model is M5.
