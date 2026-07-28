"""Root locus of a three-pole amplifier as loop gain increases.

Deliberately the SAME loop as feedback_margins.py and oscillator_loopgain.py:
    L(s) = K / (1 + s/w0)^3
so the three figures are three views of one amplifier. Closed-loop poles are the
roots of 1 + L(s) = 0, i.e. of (1 + s/w0)^3 + K = 0, which has the closed form
    s = w0 * ( (-K)^(1/3) - 1 )
over the three cube roots. The pair crosses the jw axis at K = 8, where
w = sqrt(3) w0 -- exactly the Barkhausen point plotted in oscillator_loopgain.py.
"""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_RED

apply_style()

w0 = 1.0
Ks = np.linspace(0, 26, 700)

# roots of (1+s/w0)^3 = -K
roots = np.array([np.roots([1/w0**3, 3/w0**2, 3/w0, 1 + K]) for K in Ks])

# order the three branches so each is continuous
ordered = np.zeros_like(roots)
ordered[0] = roots[0]
for i in range(1, len(Ks)):
    prev, cur = ordered[i-1], list(roots[i])
    for j in range(3):
        k = min(range(len(cur)), key=lambda m: abs(cur[m] - prev[j]))
        ordered[i, j] = cur.pop(k)

fig, ax = plt.subplots(figsize=(5.6, 4.4))
ax.axhline(0, color="0.35", lw=0.7)
ax.axvline(0, color="0.35", lw=0.7)

for j, c in enumerate([GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER]):
    ax.plot(ordered[:, j].real, ordered[:, j].imag, color=c, lw=1.5)

# open-loop poles: all three at s = -w0 (K = 0)
ax.plot(-w0, 0, "x", color="0.25", ms=12, mew=2.2,
        label=r"open-loop poles ($K=0$): 3 at $-\omega_0$")

# the K = 3 design point used by the margins figure
K_design = 3.0
rd = np.roots([1, 3, 3, 1 + K_design])
ax.plot(rd.real, rd.imag, "s", color=GUIDE_GREEN, ms=6, mew=0,
        label=r"$K=3$ (healthy margins)")

# axis crossing at K = 8, w = sqrt(3) w0
wc = np.sqrt(3)*w0
ax.plot([0, 0], [wc, -wc], "o", mfc="none", mec=GUIDE_RED, ms=11, mew=1.9,
        label=r"$K=8$: poles on the $j\omega$ axis")
ax.annotate("poles cross into the\nright half-plane\n(oscillation)",
            xy=(0, wc), xytext=(-4.1, 2.75), color=GUIDE_RED, fontsize=8,
            ha="left", va="center",
            arrowprops=dict(arrowstyle="->", color=GUIDE_RED, lw=0.9))
ax.annotate(r"increasing $K$", xy=(-0.72, 1.30), color="0.3", fontsize=8,
            ha="right", va="center")

ax.set_xlabel(r"$\sigma$  (units of $\omega_0$)")
ax.set_ylabel(r"$j\omega$  (units of $\omega_0$)")
ax.set_xlim(-4.3, 2.3)
ax.set_ylim(-3.4, 3.4)
ax.set_aspect("equal")
ax.legend(loc="lower left", fontsize=7.5)
ax.grid(False)

save(fig, "opamp_rootlocus")
