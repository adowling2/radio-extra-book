# Round 7 figure and diagram audit

## Scope and method

This is a visual and structural audit, not a redraw. It covers all 36 generated
PDF figures and all 22 inline `tikzpicture`/`circuitikz` figures in the current
227-page `main.pdf` (built 2026-09-04). The generated figures were rendered at
200 dpi with Poppler in colour and greyscale and inspected at their authored
physical dimensions. Inline diagrams were inspected in the rendered book at
180 dpi, at their final page scale. Source, caption, label, input/output, and
unit checks used the corresponding TeX source and `main.aux`.

Severity is deliberately conservative:

| Severity | Meaning |
|---|---|
| P1 | Clipping, ambiguity, or a defect that prevents reliable use. Fix before release. |
| P2 | A meaningful print/accessibility/readability issue. Repair in this round. |
| P3 | A worthwhile polish item; apply if the figure is otherwise being touched. |
| Pass | No actionable defect found in this pass. |

For the generated set, `figures/manifest.json` lists exactly 36 PDFs, each has a
same-named source script and provenance sidecar, and no plotted PDF is missing
from or extra to that set. The provenance records consistently identify the
source as an analytical model encoded in the script. Inline circuit diagrams
are intentionally excluded from that manifest by `figures/Makefile`; their
source of truth is the stated TeX figure environment.

## Generated PDF figures

| Figure | Severity | Evidence and proposed remediation |
|---|---|---|
| `array_patterns.pdf` / Fig. 16.4 | P3 | Colour, greyscale, and caption agree. The cardioid panel carries two leaders into a small region and its lower annotation is close to the panel edge. Keep the content, but shorten/reposition the beamwidth note when next editing so both callouts have more breathing room. |
| `bode_first_order_highpass.pdf` / Fig. 11.3 | Pass | Exact/asymptote distinction survives greyscale because the asymptote is dashed; corner leaders are clear and do not hide data. |
| `bode_first_order_lowpass.pdf` / Fig. 4.1 | Pass | Exact/asymptote distinction survives greyscale because the asymptote is dashed; no clipping or caption mismatch found. |
| `bode_second_order.pdf` / Fig. 4.2 | Resolved P2 | Four response curves were solid and differentiated only by hue. The regenerated plot now uses solid, dashed, dash-dot, and dotted styles, verified in the 200-dpi greyscale render. |
| `conduction_angle.pdf` / Fig. 17.1 | Resolved P2 | The three waveforms were colour-led. The regenerated plot now pairs solid/dashed/dotted waveforms with explicit neutral labels; its DC guides remain consistently dashed and the result is readable in greyscale. |
| `crystal_impedance.pdf` / Fig. 17.7 | Resolved P2 | The parallel-resonance annotation was pressed against the top boundary, and lower amber labels were weak in greyscale. The annotation now sits inside clear upper-right plot space; the inductive/range text is neutral dark while the range bracket remains coloured. Both colour and greyscale renders pass. |
| `feedback_first_order.pdf` / Fig. 5.1 | Resolved P2 | Both panels encoded beta values with colour only. The pole panel now directly labels every beta and the step panel uses and directly labels four line styles. The prior legend-data overlap warning is eliminated. |
| `feedback_margins.pdf` / Fig. 5.4 | P3 | Geometry and labels make both margins understandable in greyscale. The two crossover colours become similar, however; retain the existing dotted vertical guides but add labelled `omega_gc`/`omega_pc` guide styles or distinct dash patterns if revising. |
| `feedback_second_order.pdf` / Fig. 5.2 | Resolved P2 | The four pole-pair/response cases were solid colour encodings. The pole panel now directly labels beta values and the response panel uses four distinct line styles, verified in greyscale. |
| `filter_families.pdf` / Fig. 15.2 | Resolved P2 | This was the strongest greyscale failure. Butterworth, Chebyshev, elliptic, and Bessel curves now use four distinct line styles, carried through the legend and verified in greyscale. |
| `ground_image_lobes.pdf` / Fig. 16.5 | Resolved P2 | The overlapping height traces formerly relied on colour. Both panels now use matched solid/dashed/dotted styles, and the legend carries that encoding. |
| `halfpower_edges.pdf` / Fig. 13.2 | P3 | The two panels support the caption well. At final size, the upper formula/note on the compact right panel has little margin from the top border. Nudge the formula slightly down or increase the right panel's top margin when editing. |
| `line_attenuation.pdf` / Fig. 16.1 | Resolved P2 | The right-panel RG-58 and RG-213 series formerly used identical solid lines and circular markers. RG-58 is now solid/circular and RG-213 dashed/square; the distinction remains clear in greyscale. |
| `line_worked.pdf` / Fig. 16.7 | Pass | Leaders terminate unambiguously, text is readable, the caption matches both panels, and the monochrome rendering is clear. |
| `nyquist_margins.pdf` / Fig. 5.3 | P3 | No ambiguous arrow endpoint or clipping found. It is annotation-dense, and the coloured gain/phase/frequency leaders collapse toward similar greys; add dash styles or dark neutral text with coloured marks only if the figure is revised. |
| `opamp_gbw_bode.pdf` / Fig. 17.4 | P3 | The common diagonal is clear and labels do not hide the teaching point. Closed-loop curves are solid colour encodings and merge near the unity-gain point; direct labels or line styles would make a greyscale reproduction more robust. |
| `opamp_rootlocus.pdf` / Fig. 17.5 | Pass | Marker shapes and legend make the operating points distinguishable without colour; leader is clear and does not cross a datum. |
| `oscillator_loopgain.pdf` / Fig. 17.6 | Pass | Single-curve figure; crossover guides, leaders, labels, units, and caption all agree and survive greyscale. |
| `phasor_unit_circle.pdf` / Fig. 2.1 | P3 | The content is readable in greyscale, but the rectangular/polar component labels use colour as a grouping device. Retain the colours but consider matching dash patterns for the dotted projections if the diagram is revised. |
| `poles_second_order.pdf` / Fig. 4.3 | Resolved P2 | Four damping-ratio point sets had identical circular markers and colour-only legend keys. The regenerated figure uses circle, square, diamond, and triangle markers mirrored in the legend, verified in greyscale. |
| `poles_zeros_notch.pdf` / Fig. 4.4 | Pass | Pole/zero marker shape provides redundant encoding; labels and the caption make the intended distinction clear in greyscale. |
| `probe_compensation.pdf` / Fig. 20.2 | P3 | Step-response curves and pole/zero rows remain interpretable because the rows are directly named, but the three cases are colour-led and the far-right row labels sit close to the axes edge. Add line styles for the left panel and move right labels slightly inward if revising. |
| `rc_transient.pdf` / Fig. 11.2 | Pass | Solid/dashed response styling provides grayscale redundancy; labels and leaders are clear. |
| `rc_worked.pdf` / Fig. 11.5 | Pass | Units, points, arrows, and caption fit are clear; the closely spaced high-resistance poles retain legibility at the printed size. |
| `rl_transient.pdf` / Fig. 12.2 | P3 | The two curves are solid and encode rise/decay chiefly by colour, though direction and labels make the distinction recoverable. Match the RC counterpart with a dashed decay curve for consistent monochrome pedagogy. |
| `rl_worked.pdf` / Fig. 12.3 | Pass | Units, marked operating point, root-locus labels, and caption match; no collision detected. |
| `rlc_parallel_worked.pdf` / Fig. 14.2 | P3 | Both panels are readable and caption-consistent. The orange/blue inductive/capacitive labels become weakly differentiated in greyscale; use dark text plus leader/position as the primary grouping if editing. |
| `rlc_series_phasor.pdf` / Fig. 13.5 | P3 | No clipping or ambiguous endpoint. Coloured explanatory labels in both panels become similar in greyscale; a neutral-text treatment with coloured geometry would improve reproduction. |
| `rlc_series_worked.pdf` / Fig. 13.4 | Pass | Marker shape plus position distinguishes the design/critical points; captions, units, and leaders are clear. |
| `rootlocus_first_order.pdf` / Fig. 11.4 | Pass | Direction arrow, points, axis, formula, and caption communicate the single-pole motion without depending on colour. |
| `rootlocus_second_order.pdf` / Fig. 4.5 | P3 | The locus is clear, but critical/undamped/overdamped labels use colour as their main grouping signal. Direct labels already supply a fallback; no urgent change. |
| `s21_is_bode.pdf` / Fig. 20.3 | P3 | The inset, bandwidth arrows, slope labels, and caption fit the teaching question. The magnitude panel is deliberately dense, and its amber annotations become pale in greyscale; darken those annotations or use neutral text if it is revised. |
| `smith_chart_antenna.pdf` / Fig. 16.3 | P3 | Leaders land clearly, but multiple leaders cross Smith-grid lines and the high/low frequency labels compete with the grid. Use small white label backplates or shorten the leaders if next revising; do not remove the useful sweep annotations. |
| `smith_chart_labeled.pdf` / Fig. 16.2 | P2 | The chart succeeds as a comprehensive reference, but it is at the limit of annotation density: several long leaders cross grid lines and the lower-left/right explanatory blocks compete with chart features. In greyscale the coloured semantic groups disappear. Divide the explanation into two panels or retain the chart and move the wavelength-scale/axis explanations into a small keyed companion diagram. If kept single-panel, use numbered callouts with a compact key and route leaders around the chart perimeter. |
| `step_first_order.pdf` / Fig. 3.2 | Pass | Single response, markers, guides, labels, and caption remain clear in monochrome. |
| `step_second_order.pdf` / Fig. 3.3 | Resolved P2 | Four solid response curves crossed and converged under a colour-only legend. The regenerated figure uses four line styles, preserved in the legend and clear in greyscale. |

## Inline TikZ and circuitikz figures

The inline set has no external provenance requirement. Its source/caption fit was
checked in `chapters/*.tex`; every circuit reviewed names or makes visually
unambiguous its input, output, and relevant element values. All are inherently
greyscale-safe because they render in neutral ink, with the limited blue used only
as a secondary label colour in Figures 15.3 and 17.8.

| Figure | Severity | Evidence and proposed remediation |
|---|---|---|
| Fig. 3.1 `fig:blocks` | Pass | Cascade, summing, and feedback diagrams have adequate spacing; arrows and signs are unambiguous at final page size. |
| Fig. 8.1 `fig:divider` | Pass | Input, output, polarity, and resistor labels are clear; caption states the relationship shown. |
| Fig. 8.2 `fig:thevenin` | Pass | The paired one-port diagrams and equivalence sign are visually balanced and readable. |
| Fig. 9.1 `fig:series-z` | Pass | Source, current direction, output polarity, and component labels are clear. |
| Fig. 9.2 `fig:rlc-parallel-z` | Pass | Branches, output node voltage, and ground reference are clear; no label collisions. |
| Fig. 9.3 `fig:rc-parallel-ex` | P3 | The `R = 100 ohm` and `X_C = 100 ohm` labels are tightly placed on one line in a small one-port. Separate them slightly or put the equality in the caption when editing. |
| Fig. 9.4 `fig:series-rl-ex` | Pass | Values, terminal markers, and the stated (Z=R+\jj\omega L) relationship are readable. |
| Fig. 11.1 `fig:rc-schematic` | Pass | Input/output and capacitor-voltage polarity agree with the caption; no collision at printed size. |
| Fig. 12.1 `fig:rl-schematic` | Pass | Current, output polarity, and resistor-voltage relation are clear. |
| Fig. 13.1 `fig:rlc-schematic` | Pass | Source, current, capacitor output, and state-defining labels are clear. |
| Fig. 13.3 `fig:rlc-rootlocus` | Pass | Inline root locus has clear arrow directions and labelled critical point; the light dashed circle remains readable. |
| Fig. 14.1 `fig:rlcpar-schematic` | Pass | Current-source input, node-voltage output, inductor-current arrow, and ground reference are clear. |
| Fig. 15.1 `fig:butterworth-poles` | Pass | Compact pole diagram is legible at final scale and caption gives the required interpretation. |
| Fig. 15.3 `fig:lnetwork` | P3 | The blue `input`/`output` labels are useful, but `X_series` sits close to the inductor label/coil. Move that label a little above the coil and make port direction visible without relying solely on colour. |
| Fig. 15.4 `fig:pit-network` | Pass | Pi and T variants are cleanly separated, labels are readable, and no wires/labels cross ambiguously. |
| Fig. 15.5 `fig:transformer` | Pass | Winding, polarity, and turns labels are readable; no caption/diagram conflict. |
| Fig. 16.6 `fig:antenna-model` | Pass | Series-RLC model and feed terminals are legible at the top-of-page placement; labels are not clipped. |
| Fig. 17.2 `fig:opamp-inv` | Pass | Virtual-ground symbol, feedback path, input/output, and resistor labels are clear. |
| Fig. 17.3 `fig:feedback-loop` | Pass | Summing signs and feedback direction are visually unambiguous. |
| Fig. 17.8 `fig:pll` | P3 | The blue functional labels improve grouping, but the `phase detector` label sits close to the summing node/line at printed size. Nudge it up/left and ensure the block names remain clear in greyscale. |
| Fig. 17.9 `fig:sallenkey` | Pass | Circuit is spacious and readable; the buffer wiring and component labels do not collide. |
| Fig. 20.1 `fig:probe-schematic` | Pass | Input/probe/scope/output grouping is explicit, component labels are legible, and the caption matches the topology. |

## Implementation status (2026-09-05)

Implemented and regenerated: `bode_second_order`, `conduction_angle`,
`crystal_impedance`, `feedback_first_order`, `feedback_second_order`,
`filter_families`, `ground_image_lobes`, `line_attenuation`,
`poles_second_order`, and `step_second_order`. Their ten PDFs, provenance
sidecars, and the figure manifest were regenerated. Colour and 200-dpi
greyscale PNGs were visually inspected; the new styles/markers remain distinct,
leaders do not acquire crossings, and no clipping was introduced.

Deferred: the P2 structural simplification of `smith_chart_labeled` (explicitly
out of scope for this implementation pass); all P3 refinements; and final
book-page inspection, which should occur after the manuscript's next full build.

## Limitations

This inspection catches rendered collisions, clipping, weak contrast, leader routing, caption-to-picture fit, and source-manifest alignment. It does not substitute for a screen-reader accessibility review of untagged PDFs, a colour-contrast measurement under every printer profile, or a technical validation of the mathematical models; those belong to the technical-claim audit.
