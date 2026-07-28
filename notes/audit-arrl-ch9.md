# ARRL Chapter 9 (Antennas & Transmission Lines) — Gap Audit

Audited against `chapters/*.tex` by grep, not by TOC. Chapter 16 is now very complete
on transmission-line theory; almost nothing in ARRL 9.4 (velocity factor, electrical
length, Γ, SWR, return loss, matched-line loss, Smith chart construction and
normalization, constant-SWR circles, wavelength scales, λ/4 invert / λ/2 repeat,
open/short stub signs, the geometric-mean quarter-wave transformer, dBi vs dBd,
468/234) is genuinely missing. The real gaps are in ARRL 9.1–9.3: the **antenna as a
circuit** (loss vs radiation resistance, feed position, loading coils), **phasing as
complex addition**, and **S-parameters**.

---

## HIGH

### 1. The two-element array factor: a pattern is a phasor sum
**ARRL asserts:** presents a picture-book table of patterns for various element
spacings and feed phases — λ/2 in phase gives a broadside figure-8, λ/2 at 180° gives
an endfire figure-8, λ/4 at 90° gives a cardioid — with no analysis, only figures to
memorize. Phasing lines are said to "create the necessary phase differences."

**Our derivation:** two identical elements, spacing \(d\), feed phase difference
\(\phi\). The far-field contributions differ only by a complex exponential, so the
total is the sum of two unit phasors:
\(F(\theta)=1+e^{j(\phi+\beta d\cos\theta)}\), and factoring out the half-angle,
\(|F(\theta)|=2\left|\cos\!\big(\tfrac{\phi+\beta d\cos\theta}{2}\big)\right|\),
with \(\beta=2\pi/\lambda\). Nulls occur where the bracket is an odd multiple of
\(\pi/2\). Then every exam answer is a substitution, not a memory item:
- \(d=\lambda/2,\ \phi=0\): argument \(=\pi\cos\theta\); nulls at \(\theta=0,\pi\)
  (along the element line) → figure-8 **broadside**.
- \(d=\lambda/2,\ \phi=\pi\): argument \(=\pi(1+\cos\theta)/1\); nulls at
  \(\theta=\pi/2\) → figure-8 **endfire**.
- \(d=\lambda/4,\ \phi=\pi/2\): argument \(=\tfrac{\pi}{4}(1+\cos\theta)\); gives
  \(|F|=2\) at \(\theta=\pi\) and \(0\) at \(\theta=0\) → **cardioid**, one null.
- \(d=\lambda/4,\ \phi=0\): argument never reaches \(\pi\), so no null anywhere →
  the "slightly flattened circle," i.e. substantially omnidirectional.

This is pure complex-amplitude addition — the same superposition of two phasors
Ch. 2 introduces — so it is squarely in scope even though the *output* is a pattern.
It also delivers the direction-finding sense antenna (loop + short vertical combined
at 90° gives a cardioid with a single sharp null) for free, and it explains what a
phasing line is for: it sets \(\phi\) electrically instead of by moving \(d\).

**Where:** new section in Ch. 16 following *An Idealized Antenna on the Smith Chart*
(or a short new section at the end of Ch. 2 with the radio application forward-
referenced). Ch. 16 is the better home — it already has \(\beta\) and \(\lambda\).

**Priority: HIGH** — replaces a memorized table of four figures with one formula the
reader can already evaluate, and covers E9C01/02/03, E9E11, E9H08, E9H11.

---

### 2. Feed-point impedance versus feed position
**ARRL asserts:** feed-point impedance is lowest at a dipole's center and rises
toward the ends because current falls while voltage rises; near center it is under
100 Ω, at the ends "several thousand" ohms; the off-center-fed dipole exploits a
150–300 Ω point; the Zepp is fed at a high-impedance end. All stated, never computed.

**Our derivation:** take the standing-wave current on a resonant half-wave dipole,
\(I(z)=I_0\cos\beta z\) with \(z\) measured from center, \(\beta z\) running to
\(\pm\pi/2\) at the ends. Radiated power \(P\) is fixed by the current distribution
and does not depend on where you tap it, so feeding at \(z\) with local current
\(I(z)\) requires \(R(z)=2P/|I(z)|^2\), i.e.
\[
R(z)=\frac{R_{\text{center}}}{\cos^{2}\beta z}.
\]
This single result generates the whole ARRL section: \(z=0\) gives 73 Ω;
\(z=\lambda/8\) (\(\cos^2=1/2\)) gives \(\approx146\ \Omega\), landing in the OCFD's
quoted 150–300 Ω window and explaining the 4:1 transformer that follows it;
\(z\to\lambda/4\) sends \(R\to\infty\), which is why an end-fed half wave (Zepp)
needs a λ/4 line section to invert it (Ch. 16 already derives \(Z_0^2/Z_L\)). It also
explains why the delta and gamma matches work by *moving the tap outward* until the
impedance meets the line — they are tapped transformers, and this is the turns ratio.

**Where:** Ch. 16, new subsection under *An Idealized Antenna on the Smith Chart*
(the constant-power / \(P=I^2R\) argument is Ch. 9's complex-power material).

**Priority: HIGH** — one formula explains five named antennas and three matching
systems (E9C05, E9C07, E9C08, E9C10, E9C12, E9E01, E9E02); it is impedance in
disguise, not pattern geometry.

---

### 3. The folded dipole's 4:1 impedance, by even/odd mode decomposition
**ARRL asserts:** the two wires act as two paralleled dipoles carrying equal current,
so with the same total power and half the current, \(P/I^2\) must be four times
larger: \(4\times73\approx292\ \Omega\). The "two dipoles in parallel with equal
current" step is asserted, and the argument silently mixes parallel-impedance
reasoning with a power argument.

**Our derivation:** decompose the two-conductor structure by superposition into an
**antenna (even) mode**, where both conductors carry equal in-phase current and
radiate, and a **transmission-line (odd) mode**, where they carry equal opposite
currents and radiate nothing. Applying a feed voltage \(V\) excites each mode with
\(V/2\). The odd mode sees two λ/4 shorted stubs in series — and Ch. 16 already
derives that a λ/4 shorted stub presents an open — so the odd mode draws no current
and can be discarded. The even mode is a dipole driven at \(V/2\) but with the feed
current splitting between two conductors, so \(I_{\text{feed}}=I_{\text{dipole}}/2\)
while \(V_{\text{feed}}=2V_{\text{dipole}}\); hence
\(Z_{\text{feed}}=4Z_{\text{dipole}}\). Bonus: the same decomposition explains the
wider SWR bandwidth (the residual stub reactance partially cancels the dipole's).

**Where:** Ch. 16, immediately after proposal 2 — it reuses the stub result from
`sec:stubs` and is the cleanest illustration in the whole chapter that superposition
plus a stub identity solves an antenna problem.

**Priority: HIGH** — turns an asserted factor of 4 into a two-mode superposition
argument built entirely from results the book already has (E9C07, E9C08).

---

### 4. Radiation resistance, loss resistance, and efficiency as a power divider
**ARRL asserts:** the antenna is two series resistances \(R_R\) and \(R_{\text{loss}}\);
total dissipation is \(I^2(R_R+R_{\text{loss}})\); efficiency \(=R_R/R_T\); ohmic
loss "does not matter" until \(R_R\) drops below about 10 Ω; a small magnetic loop
can have \(R_R\ll1\ \Omega\). The efficiency formula is given without deriving why
the split is a resistance ratio.

**Our derivation:** Ch. 16 already models the antenna as a series RLC with
\(R_{\text{rad}}\), but has **no loss resistor and no efficiency anywhere in the
book** (`grep` finds "radiation resistance" only in Ch. 16, and no efficiency
treatment). Add \(R_{\text{loss}}\) in series and the result is Ch. 8's series-divider
argument applied to power: series elements share one current, so
\(P_k=|I|^2R_k\) and
\[
\eta=\frac{P_{\text{rad}}}{P_{\text{in}}}
=\frac{R_{\text{rad}}}{R_{\text{rad}}+R_{\text{loss}}} ,
\]
a resistive divider, with no new physics. Then quantify ARRL's asserted threshold:
with a fixed \(R_{\text{loss}}\approx1\ \Omega\), \(\eta=0.99\) at
\(R_{\text{rad}}=100\ \Omega\), \(0.90\) at 10 Ω, \(0.50\) at 1 Ω, \(0.09\) at 0.1 Ω
— the "below 10 Ω it starts to matter" rule is just the shape of \(x/(x+1)\).
Finally couple it to \(Q\): the same \(R_T\) sets \(Q=\omega_0L/R_T\), so adding loss
resistance *widens* the SWR bandwidth while *lowering* efficiency — the reason a
lossy short antenna can look better on an SWR meter than a good one. That
counterintuitive coupling is the payoff and nothing in the book says it yet.

**Where:** Ch. 16, extending *Modeling the Antenna* / the short-whip `physicalbox`
(which already discusses \(R_{\text{rad}}\) collapsing but stops short of \(\eta\)).

**Priority: HIGH** — a genuine content hole, three pool questions (E9A03, E9A05,
E9A09), and it makes the efficiency-vs-bandwidth tradeoff quantitative.

---

### 5. S-parameters as a change of basis, and \(S_{21}\) as the Bode transfer function
**ARRL asserts:** defines \(a\) and \(b\) waves and ports, states \(S_{11}\) is the
input reflection coefficient (convertible to SWR or return loss) and \(S_{21}\) is
"forward gain," and states that a VNA is calibrated with short/open/50 Ω loads. No
connection is drawn to anything else.

**Our derivation:** the book has **no S-parameter content at all** (`grep` finds
neither "S-param" nor "scattering"), yet it has already done the hard part: Ch. 16
splits \(V\) and \(I\) into forward and reverse waves. Define the wave variables
\(a=(V+Z_0I)/2\sqrt{Z_0}\), \(b=(V-Z_0I)/2\sqrt{Z_0}\) — an invertible linear change
of variables from the \((V,I)\) basis, exactly the kind of change of basis the
state-space chapters use. Then for a one-port of impedance \(Z\),
\(S_{11}=b/a=(Z-Z_0)/(Z+Z_0)=\Gamma\) **identically**, so \(|S_{11}|^2\) is the
reflected power fraction and \(\mathrm{RL}=-20\log_{10}|S_{11}|\) — the return loss
Ch. 16 already defines. And the important one: \(S_{21}\) is the forward transmission
of a two-port terminated in \(Z_0\), i.e. it *is* the transfer function \(G(j\omega)\)
of Ch. 3/4, measured in a matched 50 Ω system. Therefore a VNA's magnitude and phase
sweep is literally a Bode plot, and a filter's \(|S_{21}|\) trace is the Ch. 15
frequency response. That identification is a high-value bridge for this book's whole
thesis and is currently absent. Add the three-load calibration as a small linear
algebra point: the instrument's own error network has three unknown complex terms, so
three known standards (\(\Gamma=-1,\,0,\,+1\) for short, match, open) give three
equations for three unknowns — which is *why* exactly three loads.

**Where:** Ch. 16 (definition, right after *Reflection Coefficient*) plus Ch. 18
*SWR Bridge and Antenna Analyzer* (VNA, four parameters, calibration).

**Priority: HIGH** — fills a total gap, is exam-tested (E4B03, E4B04, E4B05, E4B07,
E4B11), and the \(S_{21}=G(j\omega)\) identity is exactly the controls-to-radio
connection the book exists to make.

---

### 6. Antenna matching systems are Ch. 15's L-network built from Ch. 16's stubs
**ARRL asserts:** describes delta, gamma, hairpin/beta, and stub matches largely as
mechanical recipes. It does note that the hairpin's lumped equivalent "is an L
network," that the gamma rod is a shorted line section shorter than λ/4 and therefore
inductive, and that a series capacitor (or a deliberately short driven element)
cancels that inductance — but never shows why the driven element must be *capacitive*,
nor why these are all the same circuit.

**Our derivation:** the book has the L-network (`15_filters_and_matching.tex`,
`\subsection{The L-Network}`) and has shorted/open stub reactances (`sec:stubs`), but
**never mentions delta, gamma, hairpin, or stub matching** — the connection is simply
missing. Unify them: an L-network matching \(R_{\text{lo}}\) up to \(R_{\text{hi}}\)
needs a shunt reactance across the *low* side and a series reactance of opposite sign;
with \(Q=\sqrt{R_{\text{hi}}/R_{\text{lo}}-1}\) already derived in Ch. 15. Then
- **hairpin/beta:** the hairpin is a shorted stub \(<\lambda/4\), hence
  \(+jZ_0\tan\beta\ell\), supplying the shunt inductance; the L-network therefore
  demands a *series capacitance*, which is why the driven element must be tuned
  slightly short (capacitive). ARRL's assertion "the element must be capacitive"
  becomes a consequence of the network topology.
- **gamma:** the same shunt inductance, but the rod-plus-element pair is the stub;
  the series capacitor is the L-network's other arm explicitly.
- **delta:** not a reactance network at all but a tapped transformer — it works by
  proposal 2's \(R(z)=R_{\text{center}}/\cos^2\beta z\), fanned out until \(R(z)\)
  equals the (high) line impedance.
- **stub match:** a shunt susceptance placed at the point along the line where the
  real part is already correct — which is the Smith-chart procedure Ch. 16 describes,
  now with a named application.

**Where:** Ch. 15 *Impedance Matching* (a subsection identifying the named antenna
matches), cross-referenced from Ch. 16's stub section.

**Priority: HIGH** — six pool questions (E9E01–E9E05, E9E09) with zero new math:
purely the act of connecting two things the book already derives, which is the book's
stated purpose.

---

## MEDIUM

### 7. Ground reflection as an image source
**ARRL asserts:** ground-reflected signals combine with direct radiation, reinforcing
in phase and cancelling out of phase; raising a horizontal antenna lowers the takeoff
angle; above λ/2 height extra lobes appear above the main lobe. Asserted, with
figures.

**Our derivation:** a perfect ground is a mirror: replace it with an **image source**
at depth \(h\) below the surface, phase-reversed for a horizontal antenna. Then this
is proposal 1's two-element formula with \(d=2h\) and \(\phi=\pi\):
\(|F(\psi)|=2|\sin(\beta h\sin\psi)|\) for elevation angle \(\psi\). Everything ARRL
asserts follows: a null at \(\psi=0\) always (a horizontal antenna over ground cannot
radiate along the ground); the first maximum where \(\beta h\sin\psi=\pi/2\), i.e.
\(\sin\psi=\lambda/4h\), so the takeoff angle falls monotonically as \(h\) rises;
and additional maxima appear once \(\beta h>\pi/2\), i.e. \(h>\lambda/4\) — with the
second lobe entering at \(h>\lambda/2\), exactly the height ARRL quotes. A vertical
antenna's image is *not* phase-reversed, giving \(2|\cos(\cdot)|\) and a maximum
along the ground — which is why verticals are the low-angle antennas.

**Where:** Ch. 16, immediately after proposal 1, as a short subsection or
`physicalbox`.

**Priority: MEDIUM** — the derivation is a one-line reuse of proposal 1 and converts
three asserted rules into arithmetic, but it edges nearest the excluded
pattern-geometry territory; include only if proposal 1 lands.

---

### 8. Loading coils: where the required reactance comes from, and the loss budget
**ARRL asserts:** an electrically short whip looks like a small radiation resistance
in series with a large capacitive reactance; base loading needs the least inductance
and the required inductance grows as the coil moves up the whip; center loading is the
best compromise; the coil needs a high reactance-to-resistance ratio; loading narrows
SWR bandwidth; a top capacitive "hat" reduces the needed inductance and so the loss.
Six assertions, no math.

**Our derivation:** Ch. 12 mentions loading coils only in passing and Ch. 16's
`physicalbox` gets the bandwidth half of the story. Complete it. Model the whip above
the coil as an open-ended line section: looking upward from height \(z\), the
reactance to be cancelled is \(X(z)=-Z_0\cot\beta(h-z)\) — Ch. 16's open-stub result.
As \(z\) rises toward the tip, \(\cot\) grows, so the required \(X_L=|X(z)|\)
*increases* — ARRL's asserted rule, derived. A capacitive hat adds \(C_{\text{top}}\)
in parallel at the tip, reducing \(|X|\) and hence \(X_L\). Then the loss budget:
a coil of quality \(Q_c\) contributes \(R_c=X_L/Q_c\) in series, so by proposal 4
\[
\eta=\frac{R_{\text{rad}}(z)}{R_{\text{rad}}(z)+X_L(z)/Q_c+R_{\text{gnd}}} .
\]
Raising the coil increases \(R_{\text{rad}}(z)\) (the current distribution stays high
over more of the whip) but also increases \(X_L(z)\), so \(\eta\) has an interior
maximum — that is exactly the "center loading is the best compromise" claim, and it
is an optimization, not a rule of thumb. Also shows why high \(Q_c\) matters
(it divides the numerator's competitor) and why \(Q=\omega_0L/R_T\) rising means
narrower bandwidth.

**Where:** Ch. 16 short-whip `physicalbox`, expanded to a subsection; or Ch. 12 with
a forward reference.

**Priority: MEDIUM** — six pool questions (E9D03, E9D04, E9D06, E9D07, E9D09, E9D10)
and a genuine tradeoff-with-an-optimum, but it needs proposal 4 first and the line
model of the whip is an approximation worth flagging as such.

---

### 9. Terminated traveling-wave antennas: \(\Gamma_L=0\) is the entire explanation
**ARRL asserts:** an unterminated rhombic or long wire has a second, backward major
lobe from power reflecting off the open ends; adding a terminating resistor absorbs
that power and makes the pattern unidirectional at the cost of about a third of the
input power, "without lowering gain in the desired direction"; a Beverage acts like a
lossy line with earth as one conductor; pennants are terminated in roughly 900 Ω.

**Our derivation:** these are transmission lines, so Ch. 16 applies with no new
theory. An open end is \(Z_L=\infty\), so \(\Gamma_L=+1\): the full reverse wave, and
the backward lobe is that wave radiating. Terminating in \(R_T=Z_0\) makes
\(\Gamma_L=0\) — a unidirectional structure — which also explains why the required
resistor is a few hundred ohms (a single wire over earth has a high \(Z_0\); the
pennant's 900 Ω is its own \(Z_0\), not an arbitrary number). And the "one third
absorbed without losing forward gain" claim is Ch. 16's matched-line-loss result: the
forward wave is attenuated as \(e^{-\alpha x}\) along the way, so whatever survives to
the far end never contributed to the forward lobe anyway. This is the same
"\(R=Z_0\) absorbs a wave perfectly because it presents the ratio the wave already
has" sentence Ch. 16 makes about \(Z_0\), applied to an antenna.

**Where:** Ch. 16, a short `physicalbox` in *Reflection Coefficient* or after
*Standing Waves*.

**Priority: MEDIUM** — short, uses only existing results, and covers E9C04, E9C06,
E9H01, E9H09 while showing the reader that "antenna" and "line" are the same object.

---

### 10. The Wilkinson divider, by even/odd-mode symmetry
**ARRL asserts:** a Wilkinson divider splits transmitter power equally between
in-phase array elements "while preventing changes in the loads from affecting power
flow to the other loads." The isolation property is asserted with no mechanism.

**Our derivation:** absent from the book entirely. Two λ/4 sections of
\(Z_1=\sqrt2\,Z_0\) from a common input to two \(Z_0\) ports, bridged by a resistor
\(R=2Z_0\). Analyze by symmetry/superposition — the same even/odd decomposition as
proposal 3. **Even mode** (both outputs driven alike): no voltage across the bridging
resistor, so it is invisible; each λ/4 section transforms \(Z_0\) to
\(Z_1^2/Z_0=2Z_0\), and the two in parallel give \(Z_0\) at the input — a match,
hence the \(\sqrt2\). **Odd mode** (outputs driven oppositely): the resistor's midpoint
is a virtual ground, each half sees \(R/2=Z_0\), and looking back through the λ/4
section the input is a virtual short, so odd-mode power goes entirely into the
resistor and never reaches the other port. Isolation *is* the odd mode being
resistively absorbed — and it also explains why the divider is lossless for the
intended (even) excitation.

**Where:** Ch. 15 *Impedance Matching* or Ch. 16 after the quarter-wave transformer
(it is two quarter-wave transformers plus symmetry).

**Priority: MEDIUM** — only one pool question (E9E08), but it is one of the best
superposition-plus-quarter-wave-transformer exercises in RF and reuses proposal 3's
even/odd machinery, so its marginal cost is low.

---

## LOW

### 11. Three small closures in Ch. 16 / Ch. 18
**ARRL asserts:** (a) \(VF=1/\sqrt{\varepsilon}\), used numerically for
polyethylene (\(\varepsilon=2.3\to VF=0.66\)); (b) a λ/8 shorted line presents
\(+jZ_0\) and a λ/8 open line \(-jZ_0\); (c) ERP/EIRP = TPO with all system gains and
losses applied, with a dipole reference assumed by default.

**Our derivation / status:** each is a sentence away from something already derived.
(a) Ch. 16 derives \(v_p=1/\sqrt{L'C'}\) and says a dielectric raises \(C'\), but
never closes the loop; since \(C'\propto\varepsilon_r\) and \(L'\) is unchanged for
non-magnetic materials, \(v_p=c/\sqrt{\varepsilon_r}\) **exactly**, and the 0.66 in
the book's own table is then a prediction, not a datum. (b) Ch. 16 gives
\(Z_{\text{in}}^{\text{short}}=jZ_0\tan\beta\ell\); at \(\beta\ell=\pi/4\),
\(\tan=1\), so the λ/8 results are the *only* lengths where the reactance magnitude
equals \(Z_0\) — worth adding to the existing list of special cases, since two pool
questions ask for it. (c) Ch. 18's link-budget section already does exactly this
arithmetic; ERP/EIRP is the same sum truncated at the antenna, with dBd vs dBi
handled by Ch. 16's 2.15 dB. Needs naming, not deriving.

**Where:** (a) Ch. 16 *Wavelength and Velocity Factor*; (b) Ch. 16 *Input Impedance
Along the Line* description list; (c) Ch. 18 *Adding It All Up*.

**Priority: LOW** — high exam yield (E9F01, E9F02, E9F10, E9F11, E9A02, E9A06,
E9A07, E9A13) but essentially zero new mathematics; cheap edits, not new content.

---

### 12. Circular polarization as two phasors 90° apart
**ARRL asserts:** two equal orthogonal linearly polarized waves combined with a 90°
phase difference produce circular polarization; hence two crossed Yagis fed 90° apart
at the same boom position.

**Our derivation:** \(\hat x\cos\omega t+\hat y\cos(\omega t-90^\circ)
=\hat x\cos\omega t+\hat y\sin\omega t\), whose magnitude is constant and whose angle
advances at \(\omega\) — the rotating-phasor picture of Ch. 2, read as a vector in
space rather than in the complex plane. The 90° is not a convention; it is the only
phase that keeps the magnitude constant, and reversing its sign reverses the sense of
rotation. The "same position along the boom" requirement is the condition that no
extra propagation phase be added.

**Where:** Ch. 2 *Why Complex Numbers Appear: Phasors*, as a short example, or
alongside proposal 1.

**Priority: LOW** — a genuine three-line phasor result and it does answer E9D02, but
polarization is field geometry and the book has so far stayed out of it; include only
if it can be framed strictly as the Ch. 2 rotating phasor.

---

## Considered and rejected

**Out of scope (pattern geometry / EM / propagation / operating practice):**
- Reading radiation patterns: beamwidth, the 3 dB definition, front-to-back,
  front-to-rear, front-to-side, major/minor lobes and nulls, E-plane vs H-plane,
  azimuthal vs elevation plots, takeoff angle, counting lobes off a figure. Purely
  graphical pattern interpretation; no circuit content. (E9B01–E9B06.)
- Far field vs near field definition. Field-region EM, not circuits.
- Parabolic dish gain \(\propto D^2f^2\), and "+6 dB when either doubles." The gain
  law needs aperture theory (EM); the dB step itself is \(20\log_{10}2\), already in
  `sec:decibels`. (E9D01.)
- Method of moments / NEC segmentation and the "10 segments per half wavelength"
  rule. Numerical electromagnetics; interesting to this reader professionally, but
  outside the book's stated boundary. (E9B09–E9B11.)
- Ground systems, radials, ground rods, bonding, wide copper straps for lightning
  protection. Explicitly excluded (safety/grounding). The only circuit-theoretic
  content — that a "ground" wire is a λ/4 stub and can be a high impedance — is
  **already in the book**, `18_measurement_and_troubleshooting.tex`, *Ground-Lead
  Inductance* / the RF-ground `physicalbox`. (E9D11, E9D12, E9A10.)
- Soil conductivity and seawater vs rocky ground, terrain, hills, buildings as
  reflectors, HAAT. Propagation, explicitly excluded. (E9A11, E9C11, E9C13 in part,
  E9C14.)
- Direction-finding practice: triangulation, RF attenuation to avoid receiver
  overload, refraction at shorelines, RDF as a figure of merit, electrostatic
  shielding of a loop. Operating practice and pattern statistics. (Note: the *sense
  antenna cardioid*, E9H08/E9H11, is covered free by proposal 1.)
- Named-antenna catalog as such: G5RV, Zepp/EFHW, extended double Zepp, OCFD,
  rhombic and Vee-beam geometry, Beverage siting, pennants/flags, Hamstick,
  screwdriver antennas. Hardware taxonomy. The two pieces with real math have been
  extracted as proposals 2 and 9.
- Foam vs solid polyethylene dielectric: lower loss and higher \(VF\) but lower
  voltage rating. The tradeoff is dielectric breakdown field, a materials fact; the
  loss and \(VF\) halves are already covered in Ch. 16. (E9F08.)
- Loop output voltage \(\propto\) turns \(\times\) area. This is Faraday's law on an
  incident field, not a circuit result; the "acts like a transformer secondary"
  intuition is already served by Ch. 15 *Transformers* and Ch. 8's mutual
  inductance. (E9H10.)

**Already covered — do not re-add:**
- Antenna as a series-RLC one-port, resonance meaning \(X=0\), capacitive below /
  inductive above, \(Q=\omega_0L/R\), \(BW\approx f_0/Q\), and higher \(Q\) meaning
  narrower SWR bandwidth: `16_transmission_lines.tex`, *An Idealized Antenna on the
  Smith Chart* → *Modeling the Antenna*, *Putting Numbers On It*, and the short-whip
  `physicalbox`. (E9A08, E9D08.)
- Antenna \(Q\) as stored energy over energy lost per cycle: derived generically in
  `14_rlc_parallel.tex` (`Q=2\pi\,\text{stored}/\text{lost per cycle}`) and
  `13_rlc_series.tex`; Ch. 16 identifies radiation as the "loss." ARRL's
  energy-based definition of antenna \(Q\) is therefore already the book's.
- dBi vs dBd and the 2.15 dB offset, plus the "gain is directivity, not
  amplification / total radiated power is unchanged" point: Ch. 16 *Gain, and Two
  Reference Antennas* and its `mistakebox`. (E9A01, E9A12, E9B07.)
- Resonant length 468/f and 234/f with the end-effect factor, and the explicit
  warning not to confuse end effect with velocity factor: Ch. 16
  *From Wavelength to Wire Length*.
- Velocity factor, electrical vs physical length, and why physical is shorter:
  Ch. 16 *Wavelength and Velocity Factor* (except the \(1/\sqrt{\varepsilon_r}\)
  closure — see proposal 11). (E9F03, E9F05, E9F06, E9F09.)
- \(\Gamma=(Z_L-Z_0)/(Z_L+Z_0)\), \(\Gamma=0\) only when \(Z_L=Z_0\), SWR from
  \(|\Gamma|\), return loss, and reflected power fraction \(|\Gamma|^2\): Ch. 16
  *Reflection Coefficient* and *Standing Waves, SWR, and Return Loss*. ARRL's
  \(P_{\text{load}}=P_F-P_R\) and \(\rho=\sqrt{P_R/P_F}\) are one line from
  \(|\Gamma|^2\) and not worth a derivation — at most a sentence in Ch. 18.
  (E9E07, E4B06.)
- λ/2 repeats the load, odd multiples of λ/4 invert it, open/short stub reactance
  signs, and a stub as a trap/resonator: Ch. 16 *Input Impedance Along the Line* and
  `sec:stubs`. (E9F04, E9F12, E9F13, E9E03.)
- Quarter-wave ("synchronous") transformer, \(Z_t=\sqrt{Z_0Z_L}\) as a geometric
  mean, the 50-to-100 Ω → 75 Ω example, and its narrowband nature versus a lumped
  L-network: Ch. 16 *Quarter-Wave and Half-Wave Transformers* and Ch. 15
  *Worked Example: Quarter-Wave and L-Network*. (E9E06, E9E10.)
- Smith chart: rectangular-to-circular mapping, the resistance axis as the only
  straight line, constant-resistance circles and constant-reactance arcs,
  normalization to \(Z_0\), constant-SWR circles, half-wavelength periodicity,
  toward-generator/toward-load scales, and its use for stubs and for impedance along
  a line: Ch. 16 *Smith Chart Interpretation* and *From the Model to the Chart*
  (the M\"obius transform is given explicitly). (E9G01–E9G11, E9E03, E9E05 partly.)
- Matched-line loss rising with frequency, the \(\sqrt f\) law with a numerical
  check, why open-wire/ladder line is lower loss (high \(Z_0\) shrinks
  \(R'/2Z_0\)), extra loss on a mismatched line, and SWR masking / "a tuner at the
  transmitter does not lower SWR on the line": Ch. 16 *Real Lines* subsections and
  Ch. 18's `mistakebox`. (E9F07.)
- Antenna analyzer vs SWR bridge (own low-power source, sweeps frequency, its
  display is the Smith locus): Ch. 18 *SWR Bridge and Antenna Analyzer*.
  (E4A07, E4A08, E4A11.)
- Yagi design tradeoffs — optimizing for forward gain costs front-to-back ratio,
  feed-point impedance, and SWR bandwidth. The impedance/bandwidth half is the
  \(Q\)-and-\(R_{\text{rad}}\) story of proposals 4 and 8; the pattern half is out of
  scope. Not worth a separate item. (E9D05.)
