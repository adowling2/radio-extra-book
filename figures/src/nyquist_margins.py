"""Nyquist plot of the same three-pole loop as feedback_margins.py, showing that
gain margin and phase margin are the radial and angular components of one
clearance from the point -1.

  L(s) = K/(1+s/w0)^3, K = 3  (the healthy-margin case)

Deliberately omits the encirclement criterion: the book's loops are all
open-loop stable, so only the distance to -1 matters. Negative frequencies (the
mirror image about the real axis) are omitted too -- they add clutter without
adding anything the argument needs.
"""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_RED, GUIDE_LINE

apply_style()

w0 = 1.0
K = 3.0
w = np.logspace(-2, 2.5, 4000)
L = K / (1 + 1j * w / w0) ** 3

# gain crossover: |L| = 1 -> phase margin is the angle left to the -180 axis
i_gc = np.argmin(np.abs(np.abs(L) - 1.0))
L_gc = L[i_gc]
ang_gc = np.angle(L_gc)                     # negative, about -138 deg
pm = np.degrees(ang_gc) + 180.0

# phase crossover: angle L = -180 deg, analytically w = sqrt(3) w0, |L| = K/8
x_pc = -K / 8.0
gm_db = -20 * np.log10(K / 8.0)

fig, ax = plt.subplots(figsize=(6.3, 4.15))

# unit circle: where |L| = 1
th = np.linspace(0, 2 * np.pi, 400)
ax.plot(np.cos(th), np.sin(th), color=GUIDE_LINE, ls="--", lw=0.9, zorder=2)
ax.annotate(r"$|L|=1$", xy=(-0.72, 0.70), color=GUIDE_LINE, fontsize=8)

ax.axhline(0, color="0.65", lw=0.7, zorder=1)
ax.axvline(0, color="0.65", lw=0.7, zorder=1)

# the locus
ax.plot(L.real, L.imag, color=GUIDE_BLUE, lw=1.9, zorder=4)
k = 1150
ax.annotate("", xy=(L.real[k + 70], L.imag[k + 70]), xytext=(L.real[k], L.imag[k]),
            arrowprops=dict(arrowstyle="-|>", color=GUIDE_BLUE, lw=1.5))

# the critical point
ax.plot(-1, 0, "x", color=GUIDE_RED, ms=9, mew=2.2, zorder=7)
ax.annotate(r"$-1$", xy=(-1, 0), xytext=(-1.18, 0.22), color=GUIDE_RED,
            fontsize=10, ha="right", va="bottom")

# --- gain margin: the radial shortfall along the negative real axis ---
ax.plot(x_pc, 0, "o", color=GUIDE_AMBER, ms=5.5, zorder=7)
ax.annotate("", xy=(-1, 0), xytext=(x_pc, 0),
            arrowprops=dict(arrowstyle="<->", color=GUIDE_AMBER, lw=1.5))

# --- phase margin: the angle still to go, measured on the unit circle ---
arc = np.linspace(np.pi, ang_gc + 2 * np.pi, 240)
ax.plot(np.cos(arc), np.sin(arc), color=GUIDE_GREEN, lw=2.4, zorder=5)
ax.plot(L_gc.real, L_gc.imag, "o", color=GUIDE_GREEN, ms=5.5, zorder=7)
ax.plot([0, L_gc.real], [0, L_gc.imag], color=GUIDE_GREEN, lw=0.8, ls=":", zorder=3)

# annotations parked in the empty right-hand half
ax.annotate(rf"gain margin: locus stops at ${x_pc:.3f}$," "\n"
            rf"so gain may rise ${1/(K/8):.2f}\times$ = {gm_db:.1f} dB",
            xy=((x_pc - 1) / 2, 0), xytext=(0.60, 1.02),
            color=GUIDE_AMBER, fontsize=8, ha="left", va="center",
            arrowprops=dict(arrowstyle="->", color=GUIDE_AMBER, lw=0.8,
                            connectionstyle="arc3,rad=0.25"))
ax.annotate(rf"phase margin: ${pm:.0f}^\circ$ of arc" "\n"
            r"still to reach $-180^\circ$",
            xy=(np.cos(-2.75), np.sin(-2.75)), xytext=(0.60, -1.30),
            color=GUIDE_GREEN, fontsize=8, ha="left", va="center",
            arrowprops=dict(arrowstyle="->", color=GUIDE_GREEN, lw=0.8,
                            connectionstyle="arc3,rad=-0.2"))
ax.annotate(r"increasing $\omega$", xy=(L.real[k], L.imag[k]),
            xytext=(-1.00, -1.42), color=GUIDE_BLUE, fontsize=8, ha="left",
            arrowprops=dict(arrowstyle="->", color=GUIDE_BLUE, lw=0.8))
ax.annotate(r"$\omega\to0$: $L\to K$", xy=(K, 0), xytext=(2.10, 0.42),
            color=GUIDE_BLUE, fontsize=8, ha="center",
            arrowprops=dict(arrowstyle="->", color=GUIDE_BLUE, lw=0.8))

ax.set_xlabel(r"$\Re\{L(\mathrm{j}\omega)\}$")
ax.set_ylabel(r"$\Im\{L(\mathrm{j}\omega)\}$")
ax.set_xlim(-1.65, 3.45)
ax.set_ylim(-1.72, 1.60)
ax.set_aspect("equal")
ax.grid(False)

fig.tight_layout()
save(fig, "nyquist_margins")
