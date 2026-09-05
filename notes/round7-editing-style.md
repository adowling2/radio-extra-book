# Round 7 editing style inferred from the annotated manuscript

## Scope

This guide captures recurring preferences visible in the September 2026 markup.
It describes editing behavior, not a license to apply changes mechanically. The
comment log remains the source of authorial intent; examples refer to its `R7-*`
IDs. Rules marked **confirmed** recur across unrelated pages. Rules marked
**local** should not be generalized without a comparable context.

## Confirmed rules

### 1. Let the mechanism do the explaining

Prefer a stated physical, mathematical, or visual reason over a label, slogan, or
unexplained consequence. The author repeatedly asks where a result comes from,
why it holds, and how an equation maps to a circuit or plot (`R7-008`, `R7-020`,
`R7-021`, `R7-023`, `R7-031`, `R7-041`, `R7-053`).

Apply this when a reader must accept a new rule or interpretation. Do not expand
routine algebra already derived nearby; the desired outcome is a short causal
bridge, not a second derivation.

### 2. Remove throat-clearing and repeated conclusions

Delete phrases that announce, restate, or rhetorically celebrate what the nearby
equation/paragraph has already shown. Markup deletes “A word on sources,”
“whole reason phasors earn their keep,” duplicated RMS/heating explanation,
“Nothing here is electrical,” and “thread tying … together” (`R7-005`,
`R7-010`, `R7-012`, `R7-028`, `R7-038`, `R7-062`).

Apply this when deletion leaves the subject, verb, and technical claim intact.
Do not cut boundary conditions, a first definition, or an exam-relevance link
that supplies information a reader cannot otherwise infer.

### 3. Use direct, concrete verbs and subjects

Prefer `explains`, `considers`, `focuses on`, or a named circuit/model over vague
verbs such as “builds,” “takes up,” or impersonal rhetoric (`R7-013`, `R7-019`,
`R7-029`). State who or what changes: a pole moves, a loop samples, a circuit
stores energy, a figure shows a relation.

This is not a ban on technical shorthand. Retain established terms when they are
defined and more exact than a conversational substitute.

Avoid using \emph{read} as a generic verb for explanation or inference. Use
\emph{understand} when the point is conceptual and \emph{interpret} when relating a
model, plot, or equation to physical meaning. Retain \emph{read} for a literal
document, an instrument indication, or a conventional plot-reading operation where
it is the precise word.

### 4. Define terms at the moment they acquire explanatory work

Do not use a term as if it already explains something. Examples request clearer
meaning for “read the right-hand form,” DC gain, “lag,” and the relation of
\(Q\), \(\zeta\), poles, and energy storage (`R7-008`, `R7-018`, `R7-031`,
`R7-034`, `R7-035`).

Apply this at true first use or at the first point where a reader must reason
with the term. Avoid re-defining standard notation in every later chapter.

### 5. Keep prose, equations, and figures in one argument

When a figure carries a claim, name the relevant panel, curve, point, parameter,
and equation in the prose. Conversely, do not make a figure repeat an unlabeled
paragraph. The author asks for explicit figure references, panel labels, visible
parameters, and explanations of plotted geometry (`R7-015`, `R7-016`, `R7-022`,
`R7-026`, `R7-032`, `R7-033`, `R7-037`, `R7-058`).

Apply it particularly to Bode, root-locus, Nyquist, and transient plots. A label
should answer one question; it should not crowd the visual with every fact from
the text.

### 6. Use diagrams where spatial or causal structure is hidden in prose

The markup repeatedly asks for a block diagram, circuit diagram, pole-placement
picture, or a figure for the stability argument (`R7-016`, `R7-029`, `R7-031`,
`R7-042`, `R7-057`). Before adding one, write the teaching question in one
sentence: what relation cannot be seen from the equation/prose alone?

Do not add a diagram merely as decoration or as a duplicate of a well-labelled
existing equation.

### 7. Put an idea where the reader needs it

Move material that is technically sound but poorly motivated in its current
location. The author asks to connect the generic material to Part III, defer
filter-specific or delay material, and simplify Nyquist coverage toward later
uses (`R7-015`, `R7-036`, `R7-043`, `R7-044`, `R7-055`).

Apply only after checking cross-references and first-use definitions. A move must
improve exposition order, not simply shorten a chapter.

### 8. Treat technical questions as audits, not stylistic edits

Questions about whether a classification, response, stability statement, or
power convention is correct require a derivation or authoritative check before
changing prose (`R7-007`, `R7-025`, `R7-034`, `R7-052`, `R7-054`).

Never rewrite to silence the question. Preserve the original statement until the
underlying model, units, signs, and assumptions have been checked.

## Punctuation and concision

The markup favors sentences whose logical relation is explicit enough to stand
without a rhetorical interruption. During the global concision pass, review each
em dash individually: retain it for a genuinely parenthetical interruption;
otherwise prefer a period, semicolon, colon, or direct sentence structure. This
is an author-provided round-level preference, reinforced by the repeated deletion
of parenthetical/rhetorical extensions in `R7-012`, `R7-028`, `R7-038`, and
`R7-062`.

Never run a global punctuation replacement. Mathematical ranges, compound terms,
and genuinely useful appositives are outside this rule.

## Local rules that should not be generalized yet

- Use the author’s requested word “predictable” in the true-RMS-meter passage
  (`R7-009`); it is not necessarily a global lexical preference.
- Simplify the full Nyquist-criterion discussion only in the Chapter 5 context
  (`R7-036`); it is not a general directive to omit mathematical background.
- Moving Chapter 6 filter/delay content needs the explicit structural decision in
  `notes/round7-open-questions.md` rather than an automatic application of the
  “move material” rule (`R7-043`, `R7-044`).

## Drift signals for the remainder of the book

Pause for manual review when prose contains any of the following:

- a conclusion introduced without the equation, limiting case, or physical model
  that earns it;
- a “this/it/they” whose referent is a diagram, curve, or previous paragraph;
- a figure caption that names a result but not its visual evidence;
- a dense margin of unlabelled curves, arrows, or parameters;
- a paragraph that repeats an immediately preceding equation in different words;
- a term such as `lag`, `DC gain`, `Q`, or `pole` doing explanatory work before
  its local meaning has been established.
