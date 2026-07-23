"""Shared matplotlib styling for figures in
"Circuit Theory for the Amateur Extra Exam".

Colors match the book's LaTeX palette (see preamble.tex). Data plots (Bode,
root locus, pole-zero, transient, filter families) are generated here; circuit
schematics live in the LaTeX source as circuitikz.

Regenerate all figures with `make` in the figures/ directory.
"""
import os
import matplotlib as mpl
import matplotlib.pyplot as plt

# Book palette (from preamble.tex)
GUIDE_BLUE = "#244B5A"
GUIDE_GREEN = "#2F5D50"
GUIDE_AMBER = "#7A5C1E"
GUIDE_LINE = "#7B858B"
GUIDE_GRAY = "#F1F3F4"
GUIDE_RED = "#8C2D2D"

# Figures are written to the figures/ directory (parent of src/).
OUTDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def apply_style():
    mpl.rcParams.update({
        "figure.figsize": (6.2, 2.7),
        "figure.dpi": 150,
        "savefig.dpi": 150,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.03,
        "font.family": "serif",
        "font.size": 10,
        "mathtext.fontset": "cm",
        "axes.edgecolor": "#333333",
        "axes.linewidth": 0.6,
        "axes.labelsize": 10,
        "axes.titlesize": 10,
        "axes.grid": True,
        "grid.color": "#CCCCCC",
        "grid.linewidth": 0.4,
        "grid.alpha": 0.8,
        "lines.linewidth": 1.8,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "xtick.direction": "in",
        "ytick.direction": "in",
        "legend.fontsize": 9,
        "legend.frameon": False,
    })


def save(fig, name):
    path = os.path.join(OUTDIR, name + ".pdf")
    fig.savefig(path)
    print("wrote", os.path.relpath(path))
    plt.close(fig)
