# General (Element 3) Question Pool — Circuit-Theory / Electronics Inventory

Source: `references/HamExam.org General Question Pool.pdf` (HamExam.org export, pool id `19-General`),
extracted with `pdftotext -layout`. Extraction was clean: all 423 question stems and all four
choices parsed for every question. No garbled sections.

## 0. Pool metadata and coverage counts

**Cycle dates: the export does not state them.** The PDF contains no "valid/effective" date text
anywhere (only the browser print timestamp 7/27/26 in the page header and the URL
`hamexam.org/view_pool/19-General`). Do not cite a date range from this file; it must be confirmed
against the NCVEC release. Flagging this explicitly rather than guessing.

**Total questions in the export: 423 unique IDs**, in 35 groups:

| Subelement | Groups | Questions |
|---|---|---|
| G0 Electrical and RF Safety | G0A, G0B | 25 |
| G1 Commission's Rules | G1A–G1E | 52 |
| G2 Operating Procedures | G2A–G2E | 60 |
| G3 Radio Wave Propagation | G3A–G3C | 37 |
| G4 Amateur Radio Practices | G4A–G4E | 60 |
| G5 Electrical Principles | G5A, G5B, G5C | 40 |
| G6 Circuit Components | G6A, G6B | 23 |
| G7 Practical Circuits | G7A, G7B, G7C | 38 |
| G8 Signals and Emissions | G8A, G8B, G8C | 42 |
| G9 Antennas and Feed Lines | G9A–G9D | 46 |

**Three ID gaps confirmed absent from this export** (verified with both `-layout` and raw
extraction): **G6B09, G8C01, G9C06**. Group counts are G6B = 11 (B01–B08, B10–B12), G8C = 15
(C02–C16), G9C = 11 (C01–C05, C07–C12). Either HamExam dropped them or the underlying pool
withdrew them — worth a cross-check, since the official pool is usually quoted with a round
count.

**Only one figure in the whole pool: Figure G7-1** (schematic-symbol identification), used by
G7A09–G7A13. There is no Ohm's-law nomograph figure and no circuit-diagram figure like the
Extra pool's E7 figures.

**Circuit-relevant classification: 236 of 423 (56%) relevant; 187 not relevant.**

| Bucket | Relevant / total |
|---|---|
| G5 Electrical Principles | 40 / 40 (all) |
| G6 Circuit Components | 23 / 23 (all) |
| G7 Practical Circuits | 38 / 38 (all) |
| G4 Amateur Radio Practices | 53 / 60 |
| G8 Signals and Emissions | 31 / 42 (G8A, G8B all; G8C mostly protocol trivia) |
| G9 Antennas and Feed Lines | 42 / 46 |
| G0 (circuit questions in disguise) | 8 / 25 |
| G1 (one PEP-definition question) | 1 / 52 |
| G1 rest, G2, G3, G0 rest | 0 |

---

## 1. Per-group tables

### G5 — Electrical Principles (40 questions, all relevant)

| Group | # | Concepts / formulas actually tested |
|---|---|---|
| G5A Reactance, inductance, capacitance, resistance, impedance | 12 | Definition of reactance as AC opposition; X measured in ohms, symbol X; X_L = 2πfL rises with f, X_C = 1/(2πfC) falls with f (both explicitly "frequency, not amplitude"); impedance Z = V/I; admittance Y = 1/Z as the inverse of impedance; series resonance when X_L = X_C → reactances cancel → **minimum** impedance; impedance-matching devices (transformer, pi-network, transmission-line section) |
| G5B Ohm's law, power calculations, decibels, RMS/PEP | 14 | P = V²/R (400 V, 800 Ω → 200 W); P = VI (12 V, 0.2 A → 2.4 W); P = I²R (7 mA, 1250 Ω → 61 mW); parallel branch currents sum (KCL); dB = 10 log(P₂/P₁): 3 dB = factor 2, −1 dB = 20.6% power loss; RMS defined as the AC value giving the same resistive dissipation as equal DC; V_pp = 2√2 V_rms (120 V rms → 339.4 V pp); V_rms = V_pk/√2 (17 V pk → 12 V); PEP from V_pp across a resistive load: P = (V_pp/(2√2))²/R (200 V pp / 50 Ω → 100 W; 500 V pp / 50 Ω → 625 W); V_rms = √(PR) (1200 W, 50 Ω → 245 V); PEP/average = 1.00 for an unmodulated carrier (1060 W avg → 1060 W PEP) |
| G5C Resistors, capacitors, inductors in series/parallel; transformers; sinusoids | 14 | Transformer action by **mutual inductance**; turns ratio V_s/V_p = N_s/N_p (500:1500 turns, 120 V → 360 V); a step-down transformer driven backwards steps up by the same ratio; primary of a step-up carries higher current so it needs larger wire (V·I conservation, I ∝ 1/N); impedance transformation ratio = (turns ratio)², so turns ratio = √(Z₁/Z₂) (600 Ω ↔ 50 Ω → 3.5:1); parallel resistors 1/R_t = Σ1/R_i (10‖20‖50 = 5.9 Ω; 100‖200 = 67 Ω); capacitors add in parallel (5 nF + 5 nF + 750 pF = 10.75 nF) and combine reciprocally in series (three 100 µF → 33.3 µF; 20 µF series 50 µF → 14.3 µF); inductors add in series (20 + 50 = 70 mH) and combine reciprocally in parallel (three 10 mH → 3.3 mH); qualitative: add C in parallel to raise capacitance, add L in series to raise inductance |

### G6 — Circuit Components (23 questions, all relevant)

| Group | # | Concepts / formulas actually tested |
|---|---|---|
| G6A Resistors, capacitors, inductors, diodes, transistors, tubes, batteries | 12 | Lead-acid 12 V minimum discharge 10.5 V; low internal battery resistance → high discharge current (source-resistance model); diode forward threshold: Ge ≈ 0.3 V, Si ≈ 0.7 V; electrolytic capacitors = high C per volume; low-voltage ceramics = low cost (poor tolerance/stability); wire-wound resistors have series inductance → unusable at RF; BJT as switch operates at **saturation and cutoff** (not the active region); MOSFET gate insulated from the channel by a thin oxide (vs. JFET's reverse-biased junction); inductor **self-resonant frequency** — above SRF the parasitic winding capacitance dominates and the part looks capacitive; vacuum tube: control grid modulates cathode-to-plate electron flow; screen grid reduces grid-to-plate capacitance (i.e. Miller feedback capacitance) |
| G6B Analog and digital ICs, connectors, ferrites, LEDs | 11 | Ferrite **mix** composition sets frequency performance; MMIC = monolithic microwave IC; CMOS vs TTL — low power consumption; op-amp IC is an **analog** device; ferrite bead/core suppresses common-mode current by inserting series impedance in that current's path; ferrite toroid advantages (large L, tailorable mix, contained field); LED is forward biased when emitting; connector frequency limits: BNC low-SWR to ~500 MHz, Type N weather-resistant to 10 GHz, SMA threaded to several GHz, RCA phono for LF/DC. (Note: G6B09 absent from this export.) |

### G7 — Practical Circuits (38 questions, all relevant)

| Group | # | Concepts / formulas actually tested |
|---|---|---|
| G7A Power supplies; schematic symbols | 13 | Bleeder resistor discharges filter capacitors (RC discharge / safety); filter network is L and C; full-wave center-tapped rectifier = 2 diodes + center-tapped transformer; half-wave: 1 diode, conducts 180° of the cycle; full-wave conducts 360°; unfiltered full-wave output = DC pulses at **twice** the line frequency (ripple frequency); switchmode vs linear — high switching frequency shrinks the magnetics and filter components; Figure G7-1 symbol ID: FET, Zener diode, NPN BJT, solid-core (iron-core) transformer, tapped inductor |
| G7B Amplifiers, oscillators, digital circuitry | 11 | Neutralization cancels internal feedback to stop self-oscillation; conduction-angle/efficiency ladder — Class A conducts 100% of the cycle and has the lowest efficiency, Class C the highest; amplifier efficiency η = P_RF,out / P_DC,in; **linear** amplifier preserves the input waveform, so Class C is only usable for constant-envelope modes (FM/CW), not SSB or AM; sine-wave oscillator = amplifier + frequency-selective filter in a feedback loop (Barkhausen); LC oscillator frequency set by the tank L and C; digital: two-input AND truth table, 3-bit counter has 2³ = 8 states, shift register as a clocked delay chain |
| G7C Receivers and transmitters; filters; SDR | 14 | Sideband selection by filtering the balanced-modulator output; balanced modulator suppresses the carrier and outputs DSB; impedance-matching transformer at a transmitter output presents the design load to the PA and line; product detector (mixing with a BFO/carrier) recovers SSB; DDS gives a variable output frequency with crystal-referenced stability; DSP filters give arbitrary bandwidth and shape; **filter parameter vocabulary**: insertion loss (in-band attenuation), ultimate rejection (out-of-band floor), cutoff frequency = the half-power (−3 dB) point of a low-pass response, bandwidth of a band-pass filter measured between the upper and lower half-power frequencies; receiver sensitivity depends on input-stage gain, noise figure, and detection bandwidth; SDR I/Q: the two signals are in quadrature (90° apart), I/Q lets any modulation be synthesized in software, and filtering/detection/modulation are all done in software |

### G4 — Amateur Radio Practices (53 of 60 relevant)

| Group | # rel / # | Concepts / formulas actually tested |
|---|---|---|
| G4A Station operation and setup | 10 / 13 | Notch filter (narrow rejection of an in-passband carrier); noise blanker gates receiver gain during a noise pulse; noise-reduction (DSP) processing artifacts/distortion; vacuum-tube PA TUNE control dips plate current at resonance (tank resonance = minimum plate current), LOAD/COUPLING adjusted for maximum power output at the specified plate current (impedance matching to the tube); ALC prevents excessive drive, and must be defeated for AFSK because the audio-level path would distort the FSK; antenna tuner increases power transfer into the line by matching; receive attenuator prevents front-end overload on strong signals; opposite-sideband CW reception (spectral placement of interferers). *Not counted: G4A10 electronic keyer, G4A12 dual VFO, G4A09 amplifier keying sequencing.* |
| G4B Test equipment | 13 / 13 | Oscilloscope architecture — horizontal and vertical channel amplifiers; scope shows waveform/time-domain detail a DVM cannot, so it is the instrument for CW keying waveform and RF envelope (transmitter output connected to the vertical input); voltmeters need high input impedance to avoid loading the circuit under test (loading error); DMM vs analog meter — better precision/accuracy vs. better for reading trends/peaking a slowly varying value; **two-tone test**: two non-harmonically-related audio tones, used to measure transmitter linearity / intermodulation distortion; directional wattmeter measures forward and reflected power (hence SWR); antenna analyzer needs a load/antenna connected, measures feed-point impedance and SWR vs. frequency, and is corrupted by strong nearby signals |
| G4C Interference and its suppression | 9 / 12 | Bypass capacitors and ferrite chokes on audio leads; broadband interference from arcing (a wideband impulse source); RFI symptoms as a diagnostic (SSB = distorted speech, CW = on/off hum); high RF voltages at current/voltage maxima → RF burns; **resonant ground connection** — a ground lead that is an appreciable fraction of a wavelength presents high impedance/high RF voltage; ferrite common-mode choke on a cable; ground loops and single-point (star) grounding; bonding all equipment enclosures to a common point |
| G4D Speech processors, S meters, sideband occupancy | 11 / 11 | Speech processor = audio compression, raises **average** power / talk power without raising PEP; overdriven processor → distortion and excessive bandwidth (splatter); S meter measures received signal strength; 1 S unit ≈ 6 dB; S8 → S9 requires a 4× power increase; "20 dB over S9" = 100× the power of S9; occupied-spectrum arithmetic: a 3 kHz LSB signal on a displayed carrier of 7.178 MHz occupies 7.175–7.178 MHz, a 3 kHz USB signal on 14.347 MHz occupies 14.347–14.350 MHz; band-edge clearance therefore = at least the signal bandwidth (3 kHz) |
| G4E Mobile and portable stations; solar power | 10 / 11 | Capacitance hat adds top capacitance to electrically shorten/resonate a short whip; corona ball reduces losses from corona discharge at the high-voltage tip; DC wiring — fuse both leads directly at the battery, and a 100 W transceiver draws too much current for an accessory socket (I = P/(V·η), voltage drop in undersized wiring); shortened mobile antennas have **narrower bandwidth** (higher loaded Q, lower radiation resistance); alternator/ignition conducted noise; solar: cells in **series** to build panel voltage, silicon photovoltaic open-circuit voltage ≈ 0.5 V per cell, series blocking diode stops reverse night-time discharge, LiFePO₄ needs a proper charge controller |

### G8 — Signals and Emissions (31 of 42 relevant)

| Group | # rel / # | Concepts / formulas actually tested |
|---|---|---|
| G8A Carriers and modulation | 14 / 14 | AM = varying instantaneous power/amplitude; modulation envelope traced by the peaks; overmodulation and "flat-topping" (clipping from excessive drive) → excessive bandwidth and distortion; FM = varying instantaneous frequency, PM = varying phase angle, reactance modulator on an oscillator/amplifier stage produces PM; direct binary FSK by digitally pulling an oscillator; SSB has the narrowest phone bandwidth; QPSK = 0/90/180/270° phase states carrying dibits, QPSK31 has ≈ the same bandwidth as BPSK31 but adds error correction; FT8 = 8-tone FSK; **link budget** = TX power + antenna gains − system losses (all in dB, summed at the receiver) and **link margin** = received power − minimum required receiver signal level |
| G8B Frequency mixing, multiplication, bandwidths | 13 / 13 | Mixer produces the sum and difference of LO and RF (heterodyning); the LO is the tuned port that maps RF to a fixed IF; **image response** at 2×IF away from the desired signal; frequency multiplier stages generate a harmonic of a lower-frequency oscillator; intermodulation from two signals in a **non-linear** circuit, and odd-order products (2F1−F2, 3F1−2F2, …) fall closest to the originals; **FM bandwidth by Carson's rule**: BW = 2(Δf + f_m) → 2(5 + 3) = 16 kHz; deviation scales with the multiplication ratio: a 12.21 MHz oscillator multiplied to 146.52 MHz (×12) needs 5 kHz/12 = 416.7 Hz deviation; duty cycle vs. average power rating (thermal); matching receiver bandwidth to signal bandwidth maximizes SNR (noise power ∝ bandwidth); symbol rate ∝ required bandwidth |
| G8C Digital modes | 4 / 15 | Relevant: FSK's two frequencies are named **mark and space** (G8C11); waterfall display axes — frequency horizontal, time vertical, amplitude as intensity, i.e. a spectrogram (G8C14); FT8 signal reports are SNR in dB referenced to a 2.5 kHz noise bandwidth (G8C15); narrowband modes decodable below the noise floor / negative SNR (G8C07). The other 11 (G8C02–06, C08–C10, C12, C13, C16 — WSPR, packet framing, Baudot, ARQ/NAK, PSK31 Varicode, FEC, mesh, digital-voice mode names) are protocol/mode trivia, not circuit theory. G8C01 absent from this export. |

### G9 — Antennas and Feed Lines (42 of 46 relevant)

| Group | # rel / # | Concepts / formulas actually tested |
|---|---|---|
| G9A Transmission lines | 11 / 11 | Characteristic impedance Z₀ of a parallel-conductor line set by conductor spacing and conductor radius (geometry only, not length or frequency); window/ladder line Z₀ ≈ 450 Ω; reflection caused by a mismatch between Z₀ and the load (antenna feed-point) impedance; standing waves eliminated only by matching the load to Z₀ — line length cannot fix it; SWR from a resistive mismatch, SWR = Z₀/Z_L or Z_L/Z₀ whichever > 1 (200 Ω on 50 Ω → 4:1; 10 Ω on 50 Ω → 5:1); a tuner at the transmitter end does **not** change the SWR on the line itself; coax attenuation increases with frequency; feed-line loss quoted in dB per 100 feet; high SWR increases loss on a lossy line (extra I²R and V²/R from the circulating standing wave); line loss makes SWR measured at the input read **lower** than the true SWR at the load |
| G9B Basic antennas | 12 / 12 | Half-wave dipole free-space pattern = figure-eight broadside to the wire; feed-point impedance vs. height above ground (drops as height falls to λ/10) and vs. feed position (rises steadily toward the ends — current node/voltage node reasoning); azimuthal pattern of a low horizontal dipole becomes nearly omnidirectional at high elevation angles; quarter-wave ground-plane vertical — omnidirectional in azimuth, feed impedance raised to ~50 Ω by sloping the radials downward, ground-mounted radials on or just under the surface; horizontal polarization → lower ground loss; a random wire fed directly puts RF current on the station equipment (no return/counterpoise); **length formulas**: half-wave dipole ℓ(ft) = 468/f(MHz) (14.250 MHz → 33 ft; 3.550 MHz → 132 ft), quarter-wave monopole ℓ(ft) = 234/f(MHz) (28.5 MHz → 8 ft) |
| G9C Directional antennas | 11 / 11 | Yagi driven element ≈ λ/2, reflector longer, director shorter (reactive loading sets the phasing); larger-diameter elements → wider bandwidth (lower element Q); boom length and added directors increase gain; element spacing/length trade gain vs. front-to-back vs. SWR bandwidth; front-to-back ratio = main-lobe power ÷ power 180° opposite; main lobe = direction of maximum field strength; **dBi = dBd + 2.15** (dipole reference gain); stacking two identical Yagis λ/2 apart gives ≈ 3 dB (array-factor doubling of aperture); matching networks — beta/hairpin match is a shorted transmission-line stub at the feed point (a shunt inductance cancelling capacitive feed reactance), gamma match works with the driven element bonded to the boom. (G9C06 absent from this export.) |
| G9D Special antennas | 8 / 12 | End-fed half-wave has a **very high** feed-point impedance (current node at the end); antenna traps = parallel-resonant LC that electrically isolates a section for multiband operation; multiband antennas have poor harmonic rejection (they are resonant at harmonic-related lengths); vertical stacking narrows the elevation lobe; log-periodic — element length and spacing scale logarithmically along the boom, giving very wide bandwidth; "screwdriver" mobile antenna varies base **loading inductance** to retune; electrically small loop (< λ/10 circumference) has nulls broadside to the loop plane. *Not counted: G9D01 NVIS height, G9D03 halo direction, G9D09 Beverage use, G9D12 inverted-V naming.* |

### G0 — circuit questions in disguise (8 of 25)

| Group | # rel / # | Concepts actually tested |
|---|---|---|
| G0A RF safety | 4 / 12 | RF exposure determined by power density (and frequency and duty cycle) — G0A02; **time averaging** of exposure over the MPE averaging period — G0A04; modulation duty cycle: a lower duty cycle permits a higher peak power for the same average exposure — G0A07; field strength measured with a calibrated field-strength meter with a calibrated antenna — G0A09 |
| G0B AC power and safety | 4 / 13 | In a 4-conductor 240 VAC circuit only the two **hot** conductors are fused (neutral/ground never interrupted) — G0B01; NEC wire ampacity: 20 A breaker requires ≥ AWG 12 — G0B02; AWG 14 wiring takes a 15 A fuse/breaker — G0B03; GFCI trips on an imbalance between the current in the hot and neutral conductors (i.e. KCL: current returning by an unintended path) — G0B05 |

### G1 — one relevant question

G1C11: FCC maximum power is specified as **PEP output at the transmitter's antenna terminals** —
the definitional anchor for all the G5B PEP arithmetic.

---

## 2. Flat deduplicated concept list

This is the checklist. Each entry is one distinct technical idea plus every question ID that
tests it.

### A. DC circuits, Ohm's law, power

1. **Ohm's law V = IR** (implicit throughout; used explicitly in the power forms below) — G5B03, G5B04, G5B05, G5B12
2. **P = VI** — G5B04
3. **P = V²/R** — G5B03, G5B12
4. **P = I²R** — G5B05
5. **V_rms = √(PR)** (rearranged power law) — G5B12
6. **Resistors in parallel, 1/R_t = Σ1/R_i**; two-resistor product-over-sum — G5C03, G5C04
7. **Kirchhoff's current law / branch currents in parallel sum to the total** — G5B02; also the physical basis of GFCI operation — G0B05
8. **Series/parallel network reduction habit** (which combination rule for which element) — G5C13, G5C14
9. **Source internal resistance limits deliverable current** (battery model) — G6A02
10. **Wire ampacity / current-carrying capacity and fuse coordination** — G0B02, G0B03, G4E03, G4E04
11. **Voltage drop in undersized DC wiring; fuse both leads at the source** — G4E03, G4E04
12. **Cells in series to add voltage** (solar panel construction) — G4E08
13. **Photovoltaic cell open-circuit voltage ≈ 0.5 V (silicon)** — G4E09
14. **Battery discharge floor for lead-acid (10.5 V on a 12 V battery)** — G6A01
15. **Blocking/series diode to prevent reverse current** — G4E10
16. **Charge control required for LiFePO₄ chemistry** — G4E11

### B. AC waveforms, RMS, PEP

17. **RMS defined as the equivalent-heating value** — G5B07
18. **Sine-wave conversions: V_rms = V_pk/√2, V_pp = 2V_pk = 2√2·V_rms** — G5B08, G5B09
19. **PEP from peak-to-peak voltage across a resistive load, P = (V_pp/2√2)²/R** — G5B06, G5B14
20. **PEP = average power for an unmodulated (constant-envelope) carrier; ratio 1.00** — G5B11, G5B13
21. **PEP is defined at the transmitter's antenna terminals** — G1C11
22. **Average vs. peak power, and duty cycle as the average/peak link** — G8B08, G0A07, G0A04
23. **Envelope of a modulated waveform (peak locus)** — G8A11, G4B04

### C. Decibels and logarithmic ratios

24. **dB = 10 log(P₂/P₁); 3 dB = 2× power** — G5B01
25. **1 dB loss = 20.6% of the power** — G5B10
26. **dB accounting in a cascade: link budget = TX power + gains − losses** — G8A13
27. **Link margin = received level − required level, in dB** — G8A14
28. **S units: 1 S unit ≈ 6 dB; S8→S9 needs 4× power; "20 dB over S9" = 100×** — G4D05, G4D06, G4D07
29. **dBi vs dBd: dBi = dBd + 2.15** — G9C04
30. **Feed-line loss expressed in dB per 100 ft** — G9A06
31. **Array stacking gain ≈ 3 dB for two identical antennas** — G9C09
32. **SNR expressed in dB referenced to a stated noise bandwidth (2.5 kHz)** — G8C15
33. **Noise power ∝ bandwidth, so matched bandwidth maximizes SNR** — G8B09, G8C07

### D. Reactance, impedance, resonance

34. **Reactance = AC opposition from L or C; units of ohms; symbol X** — G5A02, G5A03, G5A04, G5A09, G5A11
35. **X_L = 2πfL, increases with frequency (frequency, not amplitude)** — G5A05
36. **X_C = 1/(2πfC), decreases with frequency** — G5A06
37. **Impedance Z = V/I** — G5A08
38. **Admittance Y = 1/Z as the reciprocal of impedance** — G5A07
39. **Series resonance: X_L = X_C, reactances cancel, impedance is minimum** — G5A01, G5A12
40. **Parallel resonance as a high-impedance tank** — G7B09 (LC oscillator tank), G9D04 (antenna trap), G4A04 (plate-current dip at tank resonance)
41. **Self-resonant frequency of a real inductor; above SRF the part is capacitive** — G6A11
42. **Parasitic inductance of wire-wound resistors makes them unusable at RF** — G6A06
43. **Stray/interelectrode capacitance as a feedback path; screen grid and neutralization as cures** — G6A12, G7B01
44. **Resonant ground lead: a lead a significant fraction of λ presents high impedance and high RF voltage** — G4C06, G4C05
45. **Series impedance inserted by a ferrite choke to suppress common-mode current** — G6B10, G6B05, G4C08, G4C01
46. **Ferrite mix/composition selects the useful frequency range** — G6B01, G6B05
47. **Loaded Q ↔ bandwidth: a shortened (loaded) antenna has narrower bandwidth; a larger-diameter Yagi element has wider bandwidth** — G4E06, G9C01
48. **Loading inductance / capacitance hat / corona ball to resonate a short antenna** — G4E01, G4E02, G9D08

### E. Series/parallel L and C

49. **Capacitors in parallel add** — G5C08, G5C13
50. **Capacitors in series combine reciprocally** — G5C09, G5C12, G5C13
51. **Inductors in series add** — G5C11, G5C14
52. **Inductors in parallel combine reciprocally** — G5C10, G5C14
53. **Unit handling across nF/pF/µF/mH** — G5C08, G5C09, G5C10, G5C11, G5C12

### F. Transformers, coupling, and impedance matching

54. **Mutual inductance is the coupling mechanism** — G5C01; mutual coupling in Yagi parasitic elements — G9C03
55. **Voltage turns ratio V_s/V_p = N_s/N_p, and it is reciprocal (a step-down run backwards steps up)** — G5C06, G5C02
56. **Current ratio is inverse to the turns ratio, so winding wire gauge follows current** — G5C05
57. **Impedance transforms as the square of the turns ratio; turns ratio = √(Z₁/Z₂)** — G5C07
58. **Impedance matching for maximum power transfer; devices that do it (transformer, pi-network, transmission-line section, tuner, stub)** — G5A10, G7C03, G4A06, G9C11, G9C12, G9D08
59. **Iron/solid-core vs air-core transformer symbols and toroidal cores** — G7A12, G6B05
60. **PA output-network tuning as a two-degree-of-freedom match: TUNE sets resonance (plate-current dip), LOAD sets the transformation ratio** — G4A04, G4A08

### G. Transmission lines

61. **Z₀ of a parallel-conductor line set by conductor spacing and radius only** — G9A01
62. **Common Z₀ values (450 Ω window line; 50 Ω/75 Ω coax)** — G9A03, G6B04
63. **Reflection arises from Z_L ≠ Z₀** — G9A04, G9A07
64. **SWR from a purely resistive mismatch = max(Z_L/Z₀, Z₀/Z_L)** — G9A09, G9A10
65. **A matching network at the input does not change the SWR on the line behind it** — G9A08
66. **High SWR increases loss on a lossy line** — G9A02
67. **Line loss masks SWR: measured input SWR reads lower than at the load** — G9A11
68. **Coax attenuation rises with frequency** — G9A05
69. **Shorted stub as a reactance (beta/hairpin match)** — G9C11
70. **Standing-wave voltage/current maxima → RF burns and hot spots** — G4C05, G4C11
71. **Connector frequency limits and low-SWR usable range** — G6B04, G6B07, G6B11, G6B12

### H. Filters and frequency response

72. **Half-power (−3 dB) point defines cutoff for a low-pass filter** — G7C12
73. **Band-pass bandwidth measured between upper and lower half-power frequencies** — G7C14
74. **Insertion loss = attenuation inside the passband** — G7C07
75. **Ultimate rejection = maximum out-of-band attenuation** — G7C13
76. **Notch filter = narrow-band rejection inside the passband** — G4A01
77. **Sideband selection by filtering** — G7C01
78. **Power-supply filter as an LC low-pass (ripple attenuation)** — G7A02
79. **DSP filters give arbitrary bandwidth and shape** — G7C06
80. **Bypass capacitors / decoupling on audio leads** — G4C01

### I. Diodes, transistors, tubes, and components

81. **Diode forward threshold: Si ≈ 0.7 V, Ge ≈ 0.3 V** — G6A05, G6A03
82. **LED forward biased to emit** — G6B08
83. **Zener diode symbol and voltage-reference role** — G7A10
84. **BJT (NPN) symbol; switching operation at saturation and cutoff** — G7A11, G6A07
85. **FET symbol; MOSFET insulated gate vs JFET junction gate** — G7A09, G6A09
86. **Vacuum tube: control grid regulates cathode-to-plate current; screen grid reduces C_gp** — G6A10, G6A12
87. **Capacitor types and trade-offs: electrolytic (C per volume), low-voltage ceramic (cheap)** — G6A04, G6A08
88. **Tapped inductor symbol** — G7A13
89. **IC families: op-amp is analog, CMOS is low power vs TTL, MMIC for microwave** — G6B06, G6B03, G6B02

### J. Power supplies

90. **Half-wave rectifier: one diode, 180° conduction** — G7A03 (contrast), G7A04, G7A05
91. **Full-wave center-tapped rectifier: two diodes + center tap, 360° conduction** — G7A03, G7A06
92. **Ripple frequency of a full-wave rectifier is twice the input frequency; output is a pulse train** — G7A07, G7A04
93. **Bleeder resistor discharges the filter capacitors (RC time constant)** — G7A01
94. **Switchmode vs linear: high switching frequency shrinks reactive components** — G7A08

### K. Amplifiers and oscillators

95. **Conduction angle and class: Class A = 100% conduction** — G7B04
96. **Efficiency ordering; Class C highest** — G7B02
97. **Efficiency η = P_RF,out / P_DC,in** — G7B08
98. **Linearity: a linear amplifier preserves the waveform; Class C only for constant-envelope modes** — G7B10, G7B11
99. **Neutralization to cancel internal feedback and stop self-oscillation** — G7B01
100. **Oscillator = amplifier + frequency-selective feedback (loop gain / Barkhausen)** — G7B07
101. **LC tank sets oscillator frequency** — G7B09
102. **ALC as a feedback loop limiting drive; must be bypassed for AFSK** — G4A05, G4A11
103. **Speech processing / audio compression raises average power without raising PEP; overdrive causes distortion and splatter** — G4D01, G4D02, G4D03, G8A10, G8A08
104. **Front-end overload and the receive attenuator; input gain and noise figure set sensitivity** — G4A13, G7C08
105. **Noise blanker gates gain during an impulse; noise reduction (DSP) distorts** — G4A03, G4A07

### L. Mixing, modulation, and spectra

106. **Mixing/heterodyning produces sum and difference frequencies** — G8B03, G8B11
107. **LO is the tuned port that translates RF to a fixed IF** — G8B01
108. **Image response at 2×IF from the desired signal** — G8B02
109. **Frequency multiplier generates a harmonic of a lower-frequency source** — G8B04
110. **Intermodulation in a non-linear circuit; odd-order products (2F1−F2, 3F1−2F2) land closest** — G8B12, G8B05, G8B13
111. **Balanced modulator suppresses the carrier and produces DSB** — G7C02
112. **Product detector recovers SSB by mixing with a reinserted carrier** — G7C04
113. **AM varies instantaneous amplitude/power; PM varies phase; FM varies instantaneous frequency; a reactance modulator gives PM** — G8A05, G8A02, G8A03, G8A04
114. **Carson's rule BW = 2(Δf + f_m)** — G8B06
115. **Deviation scales with the frequency-multiplication ratio** — G8B07
116. **SSB is the narrowest phone emission; occupied bandwidth of the modes** — G8A07
117. **Occupied-spectrum arithmetic for LSB/USB relative to the displayed carrier, and the resulting band-edge clearance** — G4D08, G4D09, G4D10, G4D11
118. **Symbol rate ∝ required bandwidth** — G8B10
119. **Digital modulation constellations: QPSK 0/90/180/270° dibits; QPSK31; FSK mark/space; 8-FSK (FT8); direct FSK by digitally pulling an oscillator** — G8A12, G8A06, G8C11, G8A09, G8A01
120. **I/Q quadrature (90°) representation; any modulation synthesizable in software; software filtering/detection/modulation** — G7C09, G7C10, G7C11
121. **DDS: variable frequency with crystal reference stability** — G7C05
122. **Spectrogram / waterfall axes; overmodulation visible as sidebands beside the signal** — G8C14, G8C13

### M. Digital logic

123. **Two-input AND truth table** — G7B03
124. **N-bit counter has 2^N states** — G7B05
125. **Shift register as a clocked delay/serial chain** — G7B06

### N. Test instrumentation and measurement

126. **Oscilloscope architecture (horizontal and vertical channel amplifiers); time-domain vs. DVM** — G4B01, G4B02
127. **Scope for CW keying waveform and RF envelope (signal into the vertical input)** — G4B03, G4B04
128. **Voltmeter input impedance and circuit loading error** — G4B05
129. **DMM vs analog meter trade-off (precision vs. trend/peaking readability)** — G4B06, G4B09
130. **Two-tone test: two non-harmonically-related tones measure transmitter linearity/IMD** — G4B07, G4B08
131. **Directional wattmeter: forward and reflected power** — G4B10
132. **Antenna analyzer: needs a load, measures feed-point impedance and SWR vs frequency, corrupted by nearby transmitters** — G4B11, G4B12, G4B13
133. **Calibrated field-strength meter with calibrated antenna** — G0A09
134. **Power density as the RF-exposure quantity; time averaging; duty-cycle trade** — G0A02, G0A04, G0A07

### O. Grounding, bonding, and interference mechanisms

135. **Ground loops: multiple return paths cause hum; single-point/star grounding** — G4C09, G4C10, G4C12
136. **Common-mode vs differential-mode current on a cable** — G6B10, G4C08
137. **Arcing as a broadband impulse noise source** — G4C02
138. **Demodulation of RF in audio gear: SSB → distorted speech, CW → keyed hum** — G4C03, G4C04
139. **Conducted vehicle noise (alternator/ignition)** — G4E07
140. **Hot conductors fused, neutral and ground never interrupted** — G0B01
141. **GFCI detects hot/neutral current imbalance** — G0B05

### P. Antennas as circuits

142. **Radiation pattern of a half-wave dipole (figure-eight broadside)** — G9B04
143. **Feed-point impedance vs. height above ground** — G9B07, and pattern vs. height — G9B05
144. **Feed-point impedance vs. feed position (current maximum at center, voltage maximum at the ends)** — G9B08; very high Z for an end-fed half wave — G9D02
145. **Quarter-wave ground-plane vertical: azimuthally omnidirectional; radial slope sets feed Z; radial placement** — G9B03, G9B02, G9B06
146. **Half-wave dipole length ℓ(ft) = 468/f(MHz)** — G9B10, G9B11
147. **Quarter-wave monopole length ℓ(ft) = 234/f(MHz)** — G9B12
148. **Counterpoise/return requirement — a random wire fed directly puts RF on the equipment** — G9B01
149. **Ground loss and polarization** — G9B09
150. **Yagi element lengths and reactive tuning (driven ≈ λ/2, reflector longer, director shorter)** — G9C02, G9C03
151. **Gain vs. boom length and number of directors; element spacing trades gain / F-B / SWR bandwidth** — G9C05, G9C10
152. **Front-to-back ratio and main lobe definitions** — G9C07, G9C08
153. **Vertical stacking narrows the elevation lobe (array factor)** — G9D05, G9C09
154. **Log-periodic scaling (log-spaced element lengths) → very wide bandwidth** — G9D06, G9D07
155. **Antenna traps as parallel-resonant isolators for multiband operation; multiband antennas have poor harmonic rejection** — G9D04, G9D11
156. **Electrically small loop (< λ/10 circumference) has nulls broadside to the loop plane** — G9D10
157. **Schematic-symbol literacy generally (Figure G7-1)** — G7A09, G7A10, G7A11, G7A12, G7A13

---

## 3. Excluded (187 questions)

Fully excluded: all of G1 except G1C11 (51), all of G2 (60), all of G3 (37), G0A minus 4 (8),
G0B minus 4 (9), plus the partial-group remainders: G4A ×3, G4C ×3, G4E ×1, G8C ×11, G9D ×4.
These are licensing rules, band/frequency privileges, operating procedure and etiquette,
emergency communications, ionospheric propagation, tower climbing and electrical-code safety
practice, and digital-protocol/mode naming trivia — none of which the book is responsible for.
