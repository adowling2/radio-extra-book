# Round 7 Generalization: Chapters 21–26 and Appendices

## Scope

Applied the confirmed Round 7 editing and author-style rules individually to
Chapters 21–26 and the appendices. The pass prioritized direct prose, explicit
mechanisms and conditions, concise sentence structure, and punctuation that states
the logical relation. It did not add claims, sources, figures, or technical
derivations.

## Changes made

- Replaced nonessential rhetorical em dashes with sentences, commas, colons, or
  explicit causal connections in Chapters 21, 24–26 and the units/formula
  appendices.
- Tightened worked-example narration in Chapters 24 and 26 so the equation,
  check, and engineering consequence appear in sequence.
- Made several causal links explicit: coupled-element phasing in a Yagi, equality
  of ring-down calculations from one pole pair, the practical implication of
  narrow-trap poles, and the reason a measurement lead shifts its resonance.
- Preserved model conditions and caveats, including high-\(Q\) qualifications,
  loss placement, matching limits, and asymptotic-filter context.
- Aligned the glossary group-delay definition with the existing chapter condition:
  flat magnitude over the occupied band is also required for waveform fidelity.
- Reviewed Chapters 22 and 23 without forcing edits; their existing prose already
  met the directness and caveat criteria.

## Figure and reference audit

No figure environments or includegraphics commands occur in Chapters 21–26 or the
appendices. Figure redesign was therefore out of scope. Existing local
cross-references and notation were retained; the full checker verifies that no
dangling references were introduced.

## Validation

- git diff --check
- ./scripts/check.sh

Both checks passed after this generalization pass.
