"""Central figure style, validation, and provenance for the textbook.

The book adapts ``scientific_figures_tables.md`` from the Dowling Lab writing
resources to a single-column, serif textbook. Every computed figure imports
this module: it supplies the colour-blind-safe palette, print dimensions,
legend-overlap check, and a provenance sidecar. Circuit schematics remain inline
``circuitikz`` diagrams rather than generated data figures.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import subprocess
import sys
import warnings

import matplotlib as mpl
import matplotlib.pyplot as plt
from cycler import cycler

# Okabe--Ito colours. Existing names keep the figure scripts simple.
PALETTE = ["#0072B2", "#E69F00", "#009E73", "#D55E00", "#CC79A7", "#56B4E9"]
GUIDE_BLUE, GUIDE_AMBER, GUIDE_GREEN, GUIDE_RED = PALETTE[:4]
GUIDE_LINE = "#6C757D"
GUIDE_GRAY = "#F1F3F4"

# Sized for the book's 6.8-inch text block. Taller and near-square panels are
# allowed where their subject needs them; both dimensions are checked on save.
BOOK_WIDE = (6.2, 2.7)
MAX_WIDTH = 6.8
MAX_HEIGHT = 5.4
OUTDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PROVENANCE_DIR = os.path.join(OUTDIR, "provenance")
_APPLIED = False


def apply_style(force=False):
    """Apply the book-wide figure style once per Python process."""
    global _APPLIED
    if _APPLIED and not force:
        return
    mpl.rcParams.update({
        "figure.figsize": BOOK_WIDE,
        "figure.dpi": 300,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.04,
        "font.family": "serif",
        "font.size": 10,
        "mathtext.fontset": "cm",
        "axes.edgecolor": "#333333",
        "axes.linewidth": 0.6,
        "axes.labelsize": 10,
        "axes.titlesize": 10,
        "axes.grid": True,
        "axes.prop_cycle": cycler(color=PALETTE),
        "grid.color": "#CCCCCC",
        "grid.linewidth": 0.4,
        "grid.alpha": 0.8,
        "lines.linewidth": 1.8,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "xtick.direction": "in",
        "ytick.direction": "in",
        "xtick.top": True,
        "ytick.right": True,
        "legend.fontsize": 9,
        "legend.frameon": False,
    })
    _APPLIED = True


def _git_state():
    try:
        def run(*args):
            return subprocess.run(
                ["git", "-C", OUTDIR, *args], capture_output=True, text=True,
                timeout=10, check=False,
            ).stdout.strip()
        return {"git_commit": run("rev-parse", "HEAD"),
                "git_dirty": bool(run("status", "--porcelain"))}
    except OSError:
        return {}


def _check_size(fig):
    width, height = fig.get_size_inches()
    if width > MAX_WIDTH or height > MAX_HEIGHT:
        warnings.warn(
            f"figure is {width:.2f} by {height:.2f} in; it exceeds the textbook "
            f"limit of {MAX_WIDTH} by {MAX_HEIGHT} in at final printed size",
            stacklevel=3,
        )


def _check_legends(fig, margin=2.0):
    """Warn when a legend hides data or is wider than its axes."""
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    for ax in fig.get_axes():
        legend = ax.get_legend()
        if legend is None:
            continue
        box = legend.get_window_extent(renderer).padded(-margin)
        covered = 0
        for line in ax.get_lines():
            points = line.get_xydata()
            if len(points):
                points = ax.transData.transform(points)
                covered += int(((points[:, 0] >= box.x0) & (points[:, 0] <= box.x1)
                                & (points[:, 1] >= box.y0) & (points[:, 1] <= box.y1)).sum())
        if covered:
            warnings.warn(
                f"legend covers {covered} plotted data point(s); move it outside "
                "the axes, open space, or label series directly",
                stacklevel=3,
            )
        if legend.get_window_extent(renderer).width > ax.get_window_extent(renderer).width + margin:
            warnings.warn("legend is wider than its axes", stacklevel=3)


def _write_provenance(fig, name):
    os.makedirs(PROVENANCE_DIR, exist_ok=True)
    script = os.path.abspath(sys.argv[0]) if sys.argv and os.path.isfile(sys.argv[0]) else None
    record = {
        "figure": f"{name}.pdf",
        "script": os.path.relpath(script, OUTDIR) if script else None,
        "sources": ["Analytical model encoded in the generating script"],
        "size_inches": [round(float(x), 3) for x in fig.get_size_inches()],
        "created": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
        "python": sys.version.split()[0],
        "matplotlib": mpl.__version__,
    }
    record.update(_git_state())
    with open(os.path.join(PROVENANCE_DIR, f"{name}.json"), "w", encoding="utf-8") as handle:
        json.dump(record, handle, indent=2)
        handle.write("\n")


def save(fig, name):
    """Validate, save a vector PDF, and record reproducible provenance."""
    _check_size(fig)
    _check_legends(fig)
    path = os.path.join(OUTDIR, name + ".pdf")
    fig.savefig(path, dpi=1200)
    _write_provenance(fig, name)
    print("wrote", os.path.relpath(path))
    plt.close(fig)
