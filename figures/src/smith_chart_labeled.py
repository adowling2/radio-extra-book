"""A labeled Smith chart, drawn from the Mobius map Gamma = (z-1)/(z+1) rather than
traced, in the conventional orientation with infinity on the right (matching NCVEC
Diagram E9-3). Every feature the pool asks to name is labeled: the resistance axis as
the only straight line, the outer circle as the reactance axis, the prime center, the
two families of circles and arcs, a constant-SWR circle, and the wavelength scale.
See sec:smith."""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_RED

apply_style()

fig, ax = plt.subplots(figsize=(6.1, 5.3))

# ---- constant-resistance circles: centre r/(1+r), radius 1/(1+r) ----
for r in (0.0, 0.2, 0.5, 1.0, 2.0, 5.0):
    c, rad = r/(1+r), 1/(1+r)
    th = np.linspace(0, 2*np.pi, 600)
    ax.plot(c + rad*np.cos(th), rad*np.sin(th),
            color="0.62", lw=0.7, zorder=2)

# ---- constant-reactance arcs: centre (1, 1/x), radius |1/x|, clipped to the disk ----
for x in (0.2, 0.5, 1.0, 2.0, 5.0):
    for sgn in (+1, -1):
        c, rad = (1.0, sgn/x), 1/x
        th = np.linspace(0, 2*np.pi, 3000)
        X = c[0] + rad*np.cos(th)
        Y = c[1] + rad*np.sin(th)
        inside = X**2 + Y**2 <= 1.0
        X, Y = X[inside], Y[inside]
        ax.plot(X, Y, color=GUIDE_GREEN, lw=0.7, alpha=0.85, zorder=2)

# ---- the two features that are single objects, drawn boldly ----
th = np.linspace(0, 2*np.pi, 800)
ax.plot(np.cos(th), np.sin(th), color=GUIDE_GREEN, lw=2.0, zorder=4)   # reactance axis
ax.plot([-1, 1], [0, 0], color=GUIDE_BLUE, lw=2.0, zorder=4)          # resistance axis
ax.plot([0], [0], "o", color=GUIDE_AMBER, ms=7, zorder=6)             # prime center

# ---- one constant-SWR circle (the third family) ----
swr = 3.0
gam = (swr-1)/(swr+1)
ax.plot(gam*np.cos(th), gam*np.sin(th), color=GUIDE_RED, lw=1.5, ls="--", zorder=5)

# ---- labels ----
ax.annotate("resistance axis\n(the only straight line)", xy=(-0.80, 0.0),
            xytext=(-1.86, -1.24), color=GUIDE_BLUE, fontsize=8.5, ha="left",
            arrowprops=dict(arrowstyle="->", color=GUIDE_BLUE, lw=0.9))
ax.annotate("reactance axis\n(the outer circle, where\nevery arc terminates)",
            xy=(np.cos(np.radians(128)), np.sin(np.radians(128))),
            xytext=(-1.34, 1.02), color=GUIDE_GREEN, fontsize=8.5, ha="left",
            arrowprops=dict(arrowstyle="->", color=GUIDE_GREEN, lw=0.9))
ax.annotate("prime center: $z=1$,\n$\\Gamma=0$, the match", xy=(0, 0),
            xytext=(0.34, -0.80), color=GUIDE_AMBER, fontsize=8.5, ha="left",
            arrowprops=dict(arrowstyle="->", color=GUIDE_AMBER, lw=0.9))
ax.annotate(f"constant-SWR circle,\nhere {swr:g}:1 — the third family,\nadded when matching",
            xy=(gam*np.cos(np.radians(206)), gam*np.sin(np.radians(206))),
            xytext=(-1.86, -0.78), color=GUIDE_RED, fontsize=8.5, ha="left",
            arrowprops=dict(arrowstyle="->", color=GUIDE_RED, lw=0.9))
ax.annotate("constant-resistance\ncircles", xy=(0.72, 0.30), xytext=(1.06, 0.66),
            color="0.35", fontsize=8.5, ha="left",
            arrowprops=dict(arrowstyle="->", color="0.5", lw=0.9))
ax.annotate("constant-reactance\narcs", xy=(0.28, 0.62), xytext=(0.72, 1.08),
            color=GUIDE_GREEN, fontsize=8.5, ha="left",
            arrowprops=dict(arrowstyle="->", color=GUIDE_GREEN, lw=0.9))
ax.annotate(r"$z\to\infty$", xy=(1.06, -0.17), color=GUIDE_BLUE, fontsize=9,
            ha="left")
ax.annotate(r"$z=0$", xy=(-1.06, 0.12), color=GUIDE_BLUE, fontsize=9, ha="right")

# wavelength scale: half a turn is a quarter wave
for frac, lab in ((0.0, r"$0\lambda$"), (0.125, r"$0.125\lambda$"),
                  (0.25, r"$0.25\lambda$"), (0.375, r"$0.375\lambda$")):
    a = np.pi - 4*np.pi*frac          # one full turn = lambda/2
    ax.plot([1.02*np.cos(a)], [1.02*np.sin(a)], marker=(2, 0, np.degrees(a)),
            ms=7, color="0.45")
    ax.annotate(lab, xy=(1.15*np.cos(a), 1.15*np.sin(a)), color="0.40",
                fontsize=7.2, ha="center", va="center")
ax.annotate("wavelength scale: one full turn is $\\lambda/2$ of line,\n"
            "so a half turn inverts the impedance",
            xy=(0.10, -1.50), color="0.35", fontsize=8, ha="center")

ax.set_xlim(-2.02, 1.58)
ax.set_ylim(-1.70, 1.36)
ax.set_aspect("equal")
ax.axis("off")
save(fig, "smith_chart_labeled")
