# Round 7 generalization: Chapters 12--16

## Scope

This pass applies confirmed Round 7 editing and author-style rules locally to
Chapters 12--16. It preserves derivations, existing technical-audit changes, and
all figure assets. It does not mechanically replace punctuation, redesign figures,
move material, add external sources, or change numerical examples.

## Applied patterns

### Direct openings, subjects, and causal bridges

- **Chapter 12:** Recast the RL motivation and ferrite introduction around the
  model and the physical actor. The common-mode discussion now explicitly connects
  net core flux to the affected current and then to typical interference paths.
- **Chapter 13:** State that the exact bandwidth relation belongs to this series
  circuit before deriving it. The Bode/pole connection, voltage magnification, and
  energy interpretation now identify the causal step before the consequence.
- **Chapter 14:** Name the shared node voltage and two states directly. The
  resonance and duality passages now state the susceptance cancellation or pole
  geometry that causes the result.
- **Chapter 15:** Define order as pole count before relating it to the usual
  passive component realization.
- **Chapter 16:** Replace rhetorical descriptions of \(Z_0\) with the physical
  voltage-to-current ratio and the condition under which a matching resistor absorbs
  a wave.

### Concision and punctuation

Each edited dash was reviewed in context. Where it had been supplying a causal
connection or repeated conclusion, the revision uses a direct sentence, colon, or
explicit connector instead. Dashes retained in unedited text continue to carry a
useful parenthetical relation, conventional range, or compound term. No global
punctuation replacement was performed.

### First-use definitions and bounded claims

- **Chapter 15:** States the difference between filter order (pole count) and the
  common count of independent energy stores in the passive lumped models used here.
- **Chapter 16:** Defines the scope of the velocity-factor shortcut at the point of
  use and defines PEC in the ground-image discussion. The cable values are now
  labelled illustrative estimates rather than specifications.

## Technical-audit qualifications

| Audit ID | Implementation |
|---|---|
| T2-1 | Chapter 15 now describes order as pole count. It limits the component-count rule to the usual independent-store, lumped passive realization and describes asymptotic slope through net pole count. |
| T2-4 | Chapter 16 limits \(VF=1/\sqrt{\varepsilon_r}\) to TEM propagation in a homogeneous, non-magnetic, nondispersive dielectric. It directs design use to the specific cable's current data sheet and labels the local cable-loss values as illustrative. |
| T2-5 | Chapter 16 labels the image result as an infinite-PEC, far-field model in the prose and figure caption. It identifies finite/lossy ground, radial systems, terrain, and nearby structures as limits on direct application. |

## Preservation and verification

- Preserved the pre-existing ferrite caveat, Bessel qualification, ring-down
  qualification, and parallel-RLC explanation already present in the working tree.
- Did not alter figure source files or their layout.
- `./scripts/check.sh` passed: no undefined references, overfull boxes greater than
  20 pt, duplicate labels, orphan labels, dangling references, hard-coded
  cross-references, glossary errors, missing/unused figures, or provenance/grayscale
  audit findings. `git diff --check` also passed.
