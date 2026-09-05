# Round 7 Generalization — Chapters 17–20

## Scope

This pass applies the confirmed Round 7 editing rules individually to Chapters 17–20:
make the mechanism explicit, use direct subjects and verbs, retain the model boundary
beside the claim, and replace a rhetorical em dash only where a sentence break or
semicolon makes the relationship clearer. It is not a bulk punctuation rewrite. No
figures were redesigned and no derivation, numerical result, or external citation was
added.

## Changes by category

### Direct causal exposition and concision

- **Chapter 17:** Recast the root-locus/margin connection as two views of the same
  parameter sweep, and described a PLL directly as a phase-controlled servo.
- **Chapter 18:** Replaced three rhetorical conclusions with short causal statements:
  sampling changes the multiplier, filter order narrows the transition band, and
  oversampling can improve in-band performance without adding converter bits.
- **Chapter 19:** Replaced broad claims about oscillator poles with a direct
  carrier-plus-skirts explanation and a scoped model statement.
- **Chapter 20:** Rewrote the scope-instrument and VNA introductions so the measured
  quantity, model, and port are the grammatical subjects.

### Punctuation and repetition

- Replaced selected rhetorical em-dash joins in Chapters 17–18 with periods or
  semicolons where they joined independent explanatory claims.
- Retained technical dashes, ranges, mathematical signs, and useful parenthetical
  interruptions. The pass did not globally replace em dashes.
- Removed repeated or promotional framing where the following mechanism already
  supplied the reason.

### Definitions, scope, and technical qualifications

- **T2-10, Chapters 17 and 19:** Labeled the \(1/(Q_L^2\Delta f^2)\) relationship as
  an idealized, resonator-filtered, far-from-flicker-corner Leeson-type scaling.
  The prose now holds carrier power and relevant noise sources fixed for that model and
  names carrier power, device/resonator noise, flicker noise, and loop architecture as
  dependencies of a real phase-noise spectrum. The formula-index shorthand was not
  changed because it is outside the assigned Chapters 17–20 scope.
- **T2-11, Chapter 20:** Defined the alias examples as a direct-sampling model and
  the counter equation as a two-dominant-term direct-count estimate. The text now
  names analog front-end bandwidth, jitter, acquisition mode, interpolation, trigger
  noise, input conditioning, reciprocal-counting architecture, and reference aging as
  practical limits that do not invalidate the pedagogical derivations.
- **T2-12, Chapter 20:** Stated that a one-port VNA sweep measures the calibrated port
  under test. Input and output impedance require separate calibrated connections and
  repeated measurements.

### Equations, prose, and figures

- Kept existing equations and numerical examples unchanged.
- Used prose to state the assumption or measurement geometry needed to interpret the
  existing equations. Existing figures retain topology and response-shape work; no
  duplicate diagrams were added.

## Verification

- The whitespace check passed.
- The full repository checker passed: 229 pages, 26 chapters, 36 figures, and all
  reference, label, glossary, inclusion, and figure-audit checks passed.

## Remaining boundary

The Phase 5 scope did not cover the formula index. Its compact phase-noise entry should
be reviewed when appendix work is in scope so it carries the same Leeson-type boundary
as Chapter 19.
