# Round 7 Author Style Guide

## Purpose and authority

This guide describes the authorial register inferred for Round 7 from the
curated Group Papers evidence in
[round7-author-style-evidence.md](round7-author-style-evidence.md). It is a
working standard for textbook revision, not a phrase bank and not permission to
alter a technical claim. When rules conflict, use this order:

1. Technical accuracy and honest scope.
2. A reader’s ability to follow the physical or mathematical idea.
3. The chapter’s teaching purpose and the author’s explicit markup.
4. This style guide.
5. Local elegance.

The style-analysis procedure and the existing Dowling-oriented guides in
`claude-for-researchers` and `CDSE_hybrid_modeling_project` informed the
structure of this file. Only the evidence-record sources establish the rules.

## Source basis and confidence

The evidence set comprises four first-author papers (S1–S4) and four
corresponding-author papers (S5–S8), all listed with role evidence in the
companion evidence file. First-author papers dominate the evidence for sentence
and exposition habits; corresponding-author papers reinforce choices of scope,
claim, comparison, and presentation.

- **High confidence:** argument structure, paragraph architecture, reader
  orientation, local definitions, quantitative specificity, explicit comparison,
  and preservation of caveats.
- **Moderate confidence:** sentence rhythm, punctuation preference, exact
  transition vocabulary, and individual word choices.
- **Low confidence / do not infer:** publisher typography, treatment of dashes
  in all genres, and the authorship of any particular collaborative sentence.

## Core register

Write as a technically confident instructor: direct, systematic, concrete, and
bounded by evidence. State the point early; explain why it follows; then make
the practical consequence visible. Favor clear causal structure over a smooth
but vague narrative. Credit an existing method or model for what it accomplishes
before explaining the limitation relevant to the present problem.

## Rules for prose

### 1. Give each paragraph one job — high confidence

Open a paragraph with the point the reader should carry forward. Follow with
the derivation, observation, comparison, or example that establishes it. Close
by interpreting the result, stating a boundary, or setting up the next idea.
Split paragraphs that require two unrelated pieces of evidence.

**Textbook adaptation:** A paragraph may first pose a learner’s question, but
the first explanatory sentence should still reveal the answer or governing
principle. Do not postpone the point until the end of a long setup.

### 2. Use a visible causal or comparative chain — high confidence

When an outcome depends on a condition, name both the condition and the reason.
When comparing alternatives, name the baseline, quantity, and regime before
stating which one changes. Use connective words such as *however*, *in
contrast*, *therefore*, *thus*, *specifically*, and *for example* only when
they accurately label a limitation, comparison, consequence, narrowing, or
illustration.

**Textbook adaptation:** Replace unsupported “this is important” language with
the circuit behavior, measurement consequence, operating constraint, or exam
decision that makes it important.

### 3. Prefer concrete subjects and active verbs — high confidence

Use the circuit, component, signal, equation, measurement, or reader action as
the subject. Prefer verbs such as *sets*, *limits*, *stores*, *opposes*,
*shows*, *compare*, *derive*, and *calculate* to nominalized abstractions. Use
“we” when it accurately describes the book’s instructional action (“We next
derive …”); use the component as subject when the physical behavior matters.

Do not use *read* as a generic substitute for *understand* or *interpret*. Reserve
it for literal reading, instrument readings, or a conventional operation such as
reading a value from a plot.

Do not force active voice where an impersonal construction is clearer or where
the result, rather than the actor, is the real subject.

### 4. Define terms, symbols, and assumptions at first use — high confidence

Define a term in the sentence where it first becomes necessary. Give symbols a
verbal meaning, units where relevant, and a stable role. Introduce equations
before displaying them; write about them as grammatical parts of the surrounding
sentence. Do not begin a prose sentence with a bare mathematical symbol.

**Textbook adaptation:** Pair the formal definition with the physical picture
when the latter prevents a predictable misconception. One crisp sentence plus a
diagram is better than a paragraph of repeated definition.

### 5. Let figures, equations, and prose share the explanatory work — high confidence

Use each visual to answer a specific teaching question. The caption identifies
what is shown and how to read it; the prose tells the reader what the visual
establishes and why. Introduce an equation as a model of a named relationship,
then interpret its terms, limiting cases, and consequence. Do not make the
caption or a displayed equation carry the entire argument.

### 6. Quantify whenever the quantity proves the point — high confidence

Replace unqualified comparative adjectives with a named reference and, when
available, a number, range, ratio, units, or limiting condition. Keep only
numbers that move the explanation forward; do not turn instructional prose into
a data dump.

**Textbook adaptation:** In a worked example, state why a value is chosen and
what order of magnitude or sign the reader should expect before calculating.

### 7. State caveats precisely and keep them — high confidence

Use direct language for what a derivation or example establishes. Use *can*,
*may*, *suggests*, or a condition when the statement depends on an assumption,
frequency range, approximation, component nonideality, or untested scope. Name
the boundary rather than adding habitual hedges.

Do not trade a caveat for a cleaner sentence. A concise scope condition is part
of the teaching.

### 8. Use moderate-length, varied sentences — moderate confidence

Favor one primary idea per sentence, usually with a clear subject–verb–object
spine. Use a longer sentence only to express a necessary technical relationship;
follow dense derivation with a short orienting sentence when useful. Split a
sentence that stacks definition, mechanism, exception, and consequence without
a clear hierarchy.

### 9. Make punctuation clarify the relationship — moderate confidence

Choose punctuation for logic, not emphasis. Use a semicolon only between closely
related independent clauses; use a colon to introduce a true explanation,
consequence, or list; use a sentence break when the reader benefits from a pause.
Avoid using an em dash as a generic substitute for a relation that should be
stated more directly. Retain a dash where it is the conventional and clearest
form, including compound modifiers and mathematical ranges.

The author’s annotated-book edits are stronger evidence than the paper corpus
for this final dash preference; apply the local editing-style guide when the two
records are more specific.

### 10. Conclude a section with what the reader can now infer — high confidence

End a substantial section by synthesizing the mechanism, comparison, or result
and its engineering consequence. Do not merely repeat headings or preview the
next section. A bounded note about an assumption or a natural next step is
useful when it prevents overgeneralization.

## Editing tactics

Use these in the following order; stop when the sentence is accurate and easy to
follow.

1. **Recover the point.** Identify the one claim, relationship, or action the
   passage needs to convey.
2. **Name the actor and condition.** Replace vague “this,” “it,” or “there are”
   constructions when the referent matters.
3. **Make evidence local.** Move the figure reference, equation interpretation,
   unit, baseline, or assumption beside the statement it supports.
4. **Cut repeated setup.** Delete a sentence only when the remaining text still
   defines every needed term and preserves the technical boundary.
5. **Resolve overloaded punctuation.** Use a semicolon, colon, or sentence split
   only if it improves the relationship between ideas.
6. **Read for the learner’s next question.** Add a physical interpretation,
   limiting case, visual, or open question when algebra alone leaves the central
   relationship hidden.

## Textbook-specific adaptation

Research articles persuade specialists that a contribution is supported. This
book must teach a reader how a circuit behaves and how to reason through an exam
question. Preserve the authorial logic but change its function:

| Research-paper habit | Textbook adaptation |
|---|---|
| “In this work, we develop …” | State the chapter’s learning objective or the circuit question being answered. |
| Comparison of methods | Compare circuit models, operating regimes, or solution paths, with the condition that selects each. |
| Quantitative benchmark | Use units, signs, ratios, limiting cases, or a compact numerical example to test intuition. |
| Methodological caveat | State the approximation, idealization, or operating condition before a reader may misuse the rule. |
| Figure as evidence | Use a figure to make topology, current/voltage direction, phase relation, or changing state visible. |
| Conclusion/recommendation | Leave the reader with a rule of reasoning and its boundary, not a claim of novelty. |

## Drift signals

Revise or flag prose that shows one of these patterns:

- A generic opening that announces importance without naming a physical,
  engineering, or exam consequence.
- A result stated without its condition, model assumption, baseline, units, or
  supporting derivation/figure.
- A paragraph that opens with background but hides its point until the end.
- Vague comparative words—*better*, *significant*, *efficient*, *accurate*,
  *obvious*, *very*—without a defined measure or context.
- A long multi-clause sentence that combines definition, mechanism, exception,
  and conclusion.
- A string of formulaic transitions, mirrored paragraph lengths, or automatic
  three-item lists that flatten the argument.
- An equation displayed without introduction, punctuation, term interpretation,
  or physical meaning.
- A figure referred to only as decoration, or a caption that substitutes for the
  explanation the body text should supply.
- A caveat removed because it weakens the prose, or a pedagogical simplification
  presented as an unrestricted physical law.
- An em dash used where an explicit relationship or a clean sentence boundary
  would read more clearly.

## Paragraph acceptance test

A textbook paragraph passes if a technically prepared reader can identify its
main point in the opening, follow the mechanism or derivation with every term
defined locally, see the relevant condition or comparison, and leave with a
bounded physical or problem-solving consequence. It should be direct without
overclaiming, concise without deleting the assumption that makes it true, and
free of punctuation used as a substitute for logic.

## Limits of use

This guide does not authorize new technical claims, changed numerical values,
new citations, or a global mechanical rewrite. It should be applied locally,
with the annotated comment log taking precedence. If applying a style rule would
change the scope or truth of a statement, retain the source text and record an
open question instead.
