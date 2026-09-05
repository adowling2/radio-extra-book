# Round 7 Technical-Claim Audit — Part 2

## Scope and method

This read-only audit covers Chapters 15–26 and the formula-index entries that principally depend on those chapters. It re-derives displayed formulas and worked examples where feasible, checks units and limiting cases, compares named examination-pool claims with the tracked Extra-pool extract, and separates definite corrections from deliberately simplified models.

The audit was originally read-only; the implementation disposition below records the
scoped Round 7 resolutions. No external citations were invented. The repository’s pool
extract is suitable evidence for the cited question wording and answers, but it is not
an official NCVEC release record. Cable performance, material, instrument, and
regulatory claims needing external primary documentation are identified explicitly.

## Findings requiring action

| ID | Location and claim | Method and evidence | Result | Impact | Recommended action |
|---|---|---|---|---|---|
| T2-1 | [Ch. 15, order/energy stores, lines 56–63](../chapters/15_filters_and_matching.tex): every independent reactive element contributes one pole; an order-\(n\) filter has \(n\) reactive elements. | This is a sound counting heuristic for independent, lumped passive states. It is not a general realization theorem: dependent/reactively constrained stores may not add independent states; active filters gain their order from capacitors plus active elements; and zeros alter the asymptotic slope. | **Qualification needed.** | Medium; it is used as a general design rule. | State the intended scope: independent energy stores in the lumped passive models used here. Describe order as pole count first, then offer component count as the common passive realization. |
| T2-2 | [Ch. 15, ring-down, lines 264–283](../chapters/15_filters_and_matching.tex): \(\tau=1/(\pi BW)\) depends only on bandwidth, “not on order” or realization. | \(\tau=Q/(\pi f_0)=1/(\pi BW)\) follows for the amplitude envelope of a single lightly damped second-order resonator, using that resonator’s current/bandpass half-power width. A higher-order filter can have several modes, non-minimum-phase zeros, and a different impulse/group-delay response; its settling is not fixed by one quoted bandwidth. | **Correct needed.** | High; it converts a second-order result into a universal filter claim. | Restrict the boxed relationship and examples to a single resonant pole pair (or an isolated narrowband resonator). For higher-order filters, describe bandwidth as informative but insufficient to determine transient settling. |
| T2-3 | [Ch. 15, filter-family table, lines 109–115](../chapters/15_filters_and_matching.tex): Bessel maximally flat group delay is equated with linear phase. | Bessel filters are designed for maximally flat group delay around zero frequency. Their phase is not exactly linear across all frequency; exact linear phase requires additional structure, such as a symmetric FIR response. | **Qualification needed.** | Medium. | Replace “i.e. linear phase” with “nearly linear phase / maximally flat group delay near the passband origin.” Keep the pulse-fidelity motivation. |
| T2-4 | [Ch. 16, velocity factor and example values, lines 105–135](../chapters/16_transmission_lines.tex), and representative cable-loss table around lines 430–475. | \(v_p=1/\sqrt{L'C'}\) and \(Z_0=\sqrt{L'/C'}\) pass for the stated lossless TEM line. \(VF=1/\sqrt{\varepsilon_r}\) additionally assumes a homogeneous, non-magnetic, nondispersive TEM dielectric. The listed velocity factors and matched-loss numbers are manufacturer/model/frequency dependent and cannot be verified from local primary documentation. | **Qualification + external check required.** | Medium; the formulas guide calculations and the table supplies numerical advice. | State the TEM/homogeneous-dielectric scope next to the velocity-factor rule. Before release, cite or link a current manufacturer data sheet for each representative cable value, or label the table as illustrative estimates rather than facts. |
| T2-5 | [Ch. 16, ideal ground image and elevation lobes, lines 1203–1234](../chapters/16_transmission_lines.tex), propagated in the formula index. | The image-current signs and \(\lvert F\rvert=2\lvert\sin(\beta h\sin\psi)\rvert\) follow for a horizontal electric radiator over an infinite, perfectly conducting plane. The resulting horizon null and vertical-horizon maximum are not literal properties of arbitrary soil, terrain, finite radial systems, or nearby structures. | **Qualification needed.** | Medium; the text’s absolute wording is easy to overapply to installations. | Label this an infinite-PEC, far-field image model in the prose, figure caption, and formula-index description. Follow it with the already appropriate reminder that measured installations differ. |
| T2-6 | [Ch. 17, oscillator/Barkhausen discussion, lines 622–646](../chapters/17_active_circuits.tex). | \(L(j\omega)=-1\) is the linearized marginal-stability (Barkhausen) condition. A physical steady oscillator is a nonlinear limit cycle: start-up requires excess small-signal gain, and amplitude control makes the effective gain settle. It is imprecise to describe the actual nonlinear oscillator simply as poles “settling onto the axis.” | **Qualification needed.** | Medium. | Keep the linear small-signal pole picture, but name it as a start-up/marginal-stability test; then say nonlinear amplitude control establishes the finite-amplitude steady oscillation. |
| T2-7 | [Ch. 17, unity-gain Sallen–Key equation, lines 980–1028](../chapters/17_active_circuits.tex). | KCL for the drawn topology gives denominator \(1+sC_1(R_1+R_2)+s^2R_1R_2C_1C_2\). Thus \(1/Q=\sqrt{C_1/C_2}[\sqrt{R_1/R_2}+\sqrt{R_2/R_1}]\), not the printed \(\sqrt{C_2/C_1}\) factor. The later equal-resistor result \(Q=\tfrac12\sqrt{C_1/C_2}\), component ratio \(C_1=2C_2\), and numerical values are consistent with the corrected expression. | **Correct needed.** | High; the general design equation contradicts its own special case. | Reverse the capacitor ratio in the displayed \(1/Q\) expression. Retain the worked example after checking the corrected formula is used in its explanatory prose. |
| T2-8 | [Ch. 18, FIR/IIR summary, lines 237–242](../chapters/18_sampling_and_dsp.tex). | A stable FIR has a finite impulse response and cannot sustain an unforced oscillation, but a finite sequence of coefficients can produce an oscillatory, “ringing” transient. Exact linear phase additionally needs symmetric (or antisymmetric) coefficients; the preceding derivation correctly supplies the symmetric case. | **Correct needed.** | Low–medium; the summary overstates the FIR distinction. | Replace “cannot ring” with “cannot sustain ringing” or “has finite-duration ringing,” and repeat that exact linear phase is a symmetric-coefficient property. |
| T2-9 | [Ch. 19, compression and IIP3, lines 209–242](../chapters/19_noise_and_dynamic_range.tex) and [formula index IIP3 entry](../appendices/formula_index.tex). | The chapter’s two-tone fundamental gain is \(a_1+\tfrac94a_3A^2\), while the standard \(+9.6\) dB relation uses a **single-tone** \(P_{1\mathrm{dB}}\), for which the coefficient is \(\tfrac34a_3A^2\). If the printed two-tone coefficient is used for the 1-dB compression point, dividing by the stated IIP3 amplitude gives about \(+14.4\) dB instead. | **Correct needed.** | High; it is a quantitative dynamic-range relation and is indexed as a reusable formula. | Explicitly define \(P_{1\mathrm{dB}}\) as the usual single-tone measurement before deriving \(+9.6\) dB, using \(\tfrac34a_3A^2\). Alternatively retain two-tone compression but change the offset and label it accordingly. Update the formula-index wording with the measurement condition. |
| T2-10 | [Ch. 19, phase-noise model, lines 335–362](../chapters/19_noise_and_dynamic_range.tex) and [formula index phase-noise entry](../appendices/formula_index.tex). | The \(1/(Q_L^2\Delta f^2)\) relation is a useful idealized Leeson-region scaling, but phase noise also depends on carrier power, active-device noise, flicker noise, resonator noise, loop architecture, and offset region. The claim that “everything” is pole location is not an adequate physical model. No local primary phase-noise source is present. | **Qualification + external check required.** | Medium; the model is pedagogically helpful but presented as universal. | Call the expression an ideal far-from-flicker-corner resonator/Leeson-type scaling and name omitted dependencies. Verify the chosen form and conditions against an authoritative oscillator-noise source before adding a citation. |
| T2-11 | [Ch. 20, digital-scope and counter limits, lines 97–142](../chapters/20_measurement_and_troubleshooting.tex). | The sampled-alias examples and tracked E4A01/E4A06 pool answers pass. However, sampling rate alone does not determine a real scope’s accurate frequency range: analog front-end bandwidth, sample-clock jitter, acquisition mode, and interpolation matter. Likewise, ±1 count and reference error are not literally the only counter errors; they are the dominant direct-count model terms. | **Qualification needed.** | Medium. | Preserve the pool-answer framing, but say “in the direct-sampling model / among these choices.” Add analog bandwidth and jitter as practical limits; call the counter formula a two-dominant-term estimate. |
| T2-12 | [Ch. 20, VNA text, lines 345–418](../chapters/20_measurement_and_troubleshooting.tex). | The tracked E4B03–E4B05, E4B07, E4B09, and E4B11 statements agree with the local pool extract. A calibrated VNA can indeed characterize input impedance, output impedance, and reflection coefficient when connected/configured at the relevant port. The nearby “one-port sweep” wording could be read as measuring all three ports/quantities simultaneously, which is not intended. | **Qualification needed.** | Low. | Say “at the port under test; repeat/reconfigure for another port” in the one-port paragraph. Retain the pool-motivated high-level statement. |
| T2-13 | [Ch. 24, antenna reflection example, lines 96–115](../chapters/24_worked_examples_and_exam_map.tex). | \(\Gamma=-15/85=-0.1765\), SWR \(=1.43\), return loss \(=15.1\) dB, and reflected power \(=3.11\%\) all re-derive correctly. The phrase that radiation efficiency “cannot be measured from the shack” is too absolute: SWR/reflection alone cannot determine it, but it can be estimated or measured with additional calibrated measurements and known loss models. | **Qualification needed.** | Low. | Change to “cannot be inferred from shack-side SWR/reflection alone.” |
| T2-14 | [Ch. 25, RF effects synthesis, lines 121–134](../chapters/25_anchored_practice.tex), plus the formula index’s \(f_{\mathrm{peak}}\) entry. | This repeats Part 1 finding T8: the text treats a high-\(Q\), lossless-self-resonance approximation \(f_{\mathrm{peak}}\approx f_{\mathrm{SRF}}/\sqrt5\) and \(Q_{\mathrm{eff}}\to0\) at lossless \(f_{\mathrm{SRF}}\) as universal. The retained loss term shifts the exact zero/peak, and real parts may have additional parasitics. | **Cross-audit correction needed.** | Medium; the practice chapter turns the approximation into a memorized rule. | Apply the Part 1 qualification in the source derivation, practice synthesis, and formula index: high-\(Q\), model-dependent estimate; actual component data determine usable behavior. |

## Claims re-derived or checked without a finding

| Coverage | Checks completed | Result and scope |
|---|---|---|
| Chapter 15 | Second-order low-pass form, L-network reactances, transformer ratio, resonator insertion-loss algebra, and quarter-wave/L-network numerical example. | Pass. T2-1 through T2-3 delimit generalizations. |
| Chapter 16 | Lossless telegrapher equations, wave speed and \(Z_0\), reflection coefficient, S-parameter normalization, SWR, low-loss propagation, line-transformer/stub/Wilkinson algebra, and worked \(100\ \Omega\) example. | Pass for the stated lossless/low-loss and matched-reference conditions. T2-4 and T2-5 bound external and idealized physical claims. |
| Chapter 17 | Conduction-angle efficiencies; op-amp gain-bandwidth example; crystal \(f_s\), \(f_p\), and numerical example; PLL type-1 equations and numerical values; mixer/image arithmetic; supply energy/ripple numbers; and Sallen–Key worked values. | Pass except the displayed general Sallen–Key \(Q\) equation (T2-7). Oscillator interpretation needs T2-6. |
| Chapter 18 | Sampling-comb transform; alias positions; quantization SNR; oversampling gain; zero-order-hold droop; DDS frequency; and direct-sampling arithmetic. | Pass under the stated band-limited, full-scale-sine, white/uncorrelated quantization-noise assumptions. FIR summary needs T2-8. |
| Chapter 19 | \(kTB\), \(-174\) dBm/Hz at \(290\) K, Friis formula, MDS examples, IM slopes, DR2/DR3 geometry, reciprocal-mixing power arithmetic, and one-pole/Butterworth noise-bandwidth integrals. | Pass, except the mismatched compression convention in T2-9. Phase-noise breadth needs T2-10. |
| Chapter 20 | Voltmeter/ammeter loading, average-meter form factor, probe compensation and numerical values, ground-lead resonance, reflected-wave masking example, S-parameter definitions, and link-budget arithmetic. | Pass within ideal source/probe/line models. Practical instrument scope needs T2-11 and T2-12. |
| Chapters 21–23 | Pattern power/F-B ratio, polarization mismatch, aperture scaling, AM/SSB/FM bandwidth and power relations, superheterodyne image arithmetic, diode/BJT small-signal relations, common-emitter gain, and ripple estimate. | Pass under stated far-field, ideal polarization, single-tone FM, small-signal, and capacitor-input-supply assumptions. |
| Chapters 24–26 | RLC, reflection, probe, trap, tank-loading, matching, and Butterworth-order worked problems. | Numerical calculations pass. T2-13 and T2-14 propagate needed wording/approximation fixes. |

## Examination-pool verification

The following claims agree with the locally tracked Extra-pool extract:

- Chapter 16’s named array patterns (E9C01–E9C03), folded-dipole approximation (E9C07), antenna matches and Q-section arithmetic (E9E01–E9E09), Wilkinson use (E9E08), and Smith-chart vocabulary/use (E9G01–E9G11).
- Chapter 17’s amplifier, neutralization, switching, PLL, crystal, and DDS exam summaries agree with the corresponding E7B, E7G, and E7H entries.
- Chapter 20’s scope, counter, probe, analyzer, VNA, and S-parameter summaries agree with E4A and E4B, including the short/open/50-ohm calibration standards.
- Chapter 25’s individually quoted E5A/B/C values and answer letters agree with the tracked extract; Chapter 24 and Chapter 26 numerical exercises re-derive correctly.

These are checks against [extra-pool-circuits.md](../references/extra-pool-circuits.md), not independent confirmation of the official pool’s current status. The official pool-cycle statement remains an external-source verification item recorded in Part 1.

## Recommended disposition

Prioritize T2-7 and T2-9: both are internal mathematical inconsistencies with direct design or measurement consequences. Next, bound the ring-down and Bessel claims (T2-2, T2-3), oscillator language (T2-6), FIR summary (T2-8), and practical instrument/antenna claims (T2-4, T2-5, T2-10–T2-13). Reuse Part 1’s self-resonance correction in Chapter 25 and the formula index (T2-14). The remaining core line, active-circuit, DSP, noise-floor, modulation, and worked-example derivations pass within their stated models.

## Implementation disposition

Resolved in this scoped pass:

- **T2-1:** described filter order as pole count and limited the corresponding
  component-count heuristic to independent energy stores in the lumped passive
  realizations used in Chapter 15.
- **T2-2:** restricted the ring-down relationship to one isolated resonant pole pair
  and stated the higher-order limitation.
- **T2-3:** described Bessel group delay as maximally flat near the passband origin,
  not exact linear phase.
- **T2-4:** limited the velocity-factor dielectric shortcut to the stated TEM and
  homogeneous-material assumptions; labeled cable-loss values illustrative and
  directed designs to current, cable-specific data sheets.
- **T2-5:** labeled the ground-image derivation and figure as an infinite-PEC,
  far-field model and stated the finite/lossy-ground and installation limitations.
- **T2-6:** identified Barkhausen as a linearized marginal-stability condition and
  distinguished nonlinear steady oscillation.
- **T2-7:** corrected the Sallen--Key factor to
  \(\sqrt{C_1/C_2}\), consistent with the existing worked example.
- **T2-8:** changed “cannot ring” to “cannot sustain ringing” and made symmetry the
  condition for exact FIR linear phase.
- **T2-9:** defined the standard \(P_{\SI{1}{\decibel}}\) relation as single-tone and
  retained two-tone IIP3, restoring the stated \(+9.6\) dB result.
- **T2-13:** limited the antenna-efficiency statement to what shack-side SWR/reflection
  cannot establish.
- **T2-14:** propagated the high-\(Q\), model-dependent self-resonance wording to
  Chapter 25; the formula index already carries the corresponding high-\(Q\) estimate.
- **T2-10:** limited the Chapter 19 phase-noise relation to a resonator-filtered,
  far-from-flicker-corner Leeson-type model, named its omitted dependencies, aligned
  the Chapter 17 cross-reference, and qualified the formula-index shorthand.
- **T2-11:** labeled the scope-alias and counter expressions as direct-sampling and
  direct-count models, respectively; named the principal practical limits omitted
  from each; and retained the exam-pool answer within its listed-choice framing.
- **T2-12:** limited one-port VNA claims to the calibrated port under test and stated
  that input and output impedances require separate calibrated connections.

No Part 2 audit findings remain open within the Chapters 12--16 scope. The
illustrative cable table remains intentionally uncited; exact values require the
current manufacturer data sheet for the selected cable.
