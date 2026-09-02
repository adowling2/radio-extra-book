# Figure standard

This figure set follows the adapted Dowling Lab scientific-figure standard in
`claude-for-researchers/resources/practices/scientific_figures_tables.md`.
The adaptation preserves the textbook's serif type and page-width layouts; it
does not import journal-column typography blindly.

- Every plotted PDF answers one stated teaching question and has a same-named
  source script in `src/`; circuit schematics are inline `circuitikz` diagrams.
- `src/_style.py` is the only place that sets the palette, typography, grid,
  print limits, legend-overlap check, and PDF export settings. It uses the
  colour-blind-safe Okabe--Ito palette.
- `make` regenerates every PDF and records a sidecar in `provenance/`; the
  generated `manifest.json` maps each final figure to its script, model source,
  dimensions, Python environment, and git state.
- `make audit` also renders greyscale previews to the ignored `audit/` folder.
  Inspect those previews at printed size after any visual change.

The figures are analytical teaching models, not research results: their values
come directly from the equations stated in the corresponding script and caption.
There is therefore no separate results-data file to preserve. The provenance
record names that explicit exception rather than pretending that one exists.

Regenerated PDFs contain creation metadata and can differ byte-for-byte even
when their plotted content is unchanged. Review the rendered output rather than
using a raw PDF checksum as a scientific comparison.
