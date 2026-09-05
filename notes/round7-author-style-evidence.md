# Round 7 Author-Style Evidence

## Scope

This is the evidence record for the Round 7 author-style guide. It uses only
papers in `Group Papers` for which the first page demonstrates that Alexander
W. Dowling is either the first author or a corresponding author. The
`claude-for-researchers` and `CDSE_hybrid_modeling_project` materials informed
the method and the categories to inspect; they are not treated as independent
evidence for the rules below.

The paper corpus supports strong inferences about argument architecture,
technical precision, and evidence handling. It supports weaker inferences about
punctuation and individual word choices because venue conventions, collaborators,
and publisher copyediting affect those features.

## Curated source set and role evidence

| ID | Paper | Role demonstrated on the first page | Why it is in the set |
|---|---|---|---|
| S1 | Dowling, Vetukuri, and Biegler (2012), *Large-Scale Optimization Strategies for Pressure Swing Adsorption Cycle Synthesis* | **First author**: author line begins “Alexander W. Dowling.” | Early, first-author methods paper; strong signal for technical exposition. 15 pp. |
| S2 | Dowling, Kumar, and Zavala (2017), *A multi-scale optimization framework for electricity market participation* | **First author**: author line begins “Alexander W. Dowling.” | First-author systems paper; strong signal for reader orientation across scales. 18 pp. |
| S3 | Dowling and Zavala (2018), *Economic opportunities for industrial systems from frequency regulation markets* | **First author**: author line begins “Alexander W. Dowling.” | First-author applied paper; strong signal for quantitative interpretation and bounded conclusions. 11 pp. |
| S4 | Dowling, Zheng, and Zavala (2018), *A Decomposition Algorithm for Simultaneous Scheduling and Control of CSP Systems* | **First author**: author line begins “Alexander W. Dowling.” | First-author optimization paper; strong signal for problem framing, research questions, and results-to-decision prose. 10 pp. |
| S5 | Wang et al. (2023), *When physics-informed data analytics outperforms black-box machine learning* | **Corresponding author**: `Alexander W. Dowling a,*` on the author line. | Later collaborative paper; useful for editorial framing and comparative claims. 17 pp. |
| S6 | Wang et al. (2024), *Measure this, not that: Optimizing the cost and model-based information content of measurements* | **Corresponding author**: `Alexander W. Dowling a,*` on the author line. | Later collaborative methods paper; useful for readable definitions and conclusion structure. 15 pp. |
| S7 | Carlozo, Wang, and Dowling (2025), *Bayesian Optimization Methods for Nonlinear Model Calibration* | **Corresponding author**: `Alexander W. Dowling*` on the author line. | Later collaborative benchmark paper; especially useful for conditional recommendations and quantitative comparisons. 21 pp. |
| S8 | Jones and Dowling (2026), *BITS for GAPS: Bayesian Information-Theoretic Sampling for Hierarchical GAussian Process Surrogates* | **Corresponding author**: `Alexander W. Dowling*` on the author line. | Recent concise methods paper; useful for caveats, scope boundaries, and controlled use of contrasts. 17 pp. |

Papers with Dowling in the middle of the author list, papers without a visible
corresponding-author mark, supporting information, slides, and archived
duplicates were excluded. First-author sources carry more weight for sentence
habits; corresponding-author sources carry more weight for editorial choices,
framing, claims, and presentation.

## Source-specific observations

### S1 — PSA cycle synthesis (2012)

- The introduction moves from an engineering need to the process setting, then
  treats prior work constructively before naming a specific limitation and the
  proposed formulation.
- Technical detail is introduced in stages: physical system, optimization task,
  variables/assumptions, then computational strategy. The reader is given a
  roadmap before the mathematical development becomes dense.
- Equations and symbols are embedded in grammatical prose, and the conclusion
  ties the algorithm back to a concrete problem class and computational tradeoff.

### S2 — Multi-scale electricity-market framework (2017)

- The opening defines the physical and market context before using the framework
  to reason across timescales. Definitions carry units and operational meaning,
  rather than relying on disciplinary shorthand.
- The conclusion reports what the data establish, identifies the boundary of the
  study, and presents future work as a response to a named limitation rather
  than as generic speculation.
- Figures and tables are used to orient the reader to hierarchy, time scale, and
  quantitative scale before the prose asks for a conclusion.

### S3 — Frequency-regulation opportunities (2018)

- Introductory paragraphs supply a concrete system, operational timescales, and
  numerical context before the literature review expands the scope.
- Results paragraphs compare a baseline with the alternative, give a magnitude,
  and explain why the difference arises from model assumptions or control
  capability.
- The conclusion names method, purpose, and practical limitation; it does not
  make a universal recommendation beyond the analyzed systems.

### S4 — CSP scheduling and control (2018)

- The problem statement identifies the source of difficulty before it states the
  proposed framework. It turns the motivation into a small, explicit set of
  research questions and follows with a section roadmap.
- The conclusion restates the method through its physical and decision-making
  consequences, including numerical result ranges, then gives a bounded future
  direction.
- The prose uses contrast words only when they establish a real baseline,
  limitation, or consequence.

### S5 — Physics-informed additive manufacturing (2023)

- The abstract makes a sharp comparison between physics-informed and black-box
  models, names the experimental budget, and describes the practical task rather
  than asserting importance without evidence.
- The conclusion recaps the workflow in operational order: available data,
  model candidates, selection, experimental design, then predictive result.
- The paper distinguishes the demonstrated case from wider intended
  applicability, though the phrase-level style remains collaborative and
  coauthor-influenced.

### S6 — Measurement optimization (2024)

- The introduction defines the problem in readers’ terms—what measurements are
  chosen, why resources matter, and what quantities models need—before the
  optimization formulation.
- The conclusion organizes contributions as formulation, implementation,
  scalability, then case-study observations. It reports model size, constraints,
  iteration count, and wall time where those details establish practical scope.
- The results preserve inconvenient findings: relaxed formulations can lose the
  ability to reveal identifiability issues at small budgets.

### S7 — Bayesian optimization for calibration (2025)

- The abstract compares methods on named benchmarks with success rates and
  states an explicit conditional recommendation.
- The conclusion is organized as conditional recommendations rather than a
  single winner. Each recommendation names the model regime, an alternative,
  and a quantitative basis.
- Caveats remain visible: suitability depends on computational cost,
  stochasticity, and multimodality. A method is not described as universally
  superior.

### S8 — BITS for GAPS (2026)

- The abstract defines the method in contrast to standard approaches, then
  connects the statistical construction to an engineering case study and
  downstream decision.
- The conclusion distinguishes the central methodological contribution from the
  illustrative numerical case. It explicitly limits what the case establishes
  and names computational scaling limitations.
- Definitions pair a term with its role in the model, and transitions such as
  contrast and consequence clarify the argument instead of decorating it.

## Cross-source findings

1. **Claim → evidence → interpretation → boundary → consequence recurs.** It is
   clearest in S3, S4, S6, and S7, and appears in the framing of S1, S2, S5,
   and S8.
2. **Quantification is argumentative, not ornamental.** S3, S4, S6, and S7
   pair magnitudes with comparison conditions; S1 does the same for model and
   computational tradeoffs.
3. **Definitions are local and operational.** S1, S2, S6, and S8 define a
   component, variable, or statistical construct when it begins doing work in
   the argument.
4. **Caveats survive the conclusion.** S2, S3, S6, S7, and S8 identify model,
   data, computational, or application limits rather than leaving only a
   success narrative.
5. **Punctuation is subordinate to logic.** The corpus does not justify a
   rigid punctuation rule: publisher conventions vary. It does support using
   a contrast, consequence, parenthetical, or sentence boundary to make the
   relationship between clauses explicit.

## Limitations

- This is a curated eight-paper sample, not an authorship-attribution study.
- First-page role markers establish first/corresponding authorship, not the
  precise author of every sentence; the corresponding-author papers are
  necessarily collaborative.
- PDF extraction is reliable enough for prose and structural inspection but can
  scramble multi-column reading order around equations, tables, and captions.
- The sources are research papers. Their rhetorical conventions must be adapted,
  not transplanted, into a licensing-exam textbook.
