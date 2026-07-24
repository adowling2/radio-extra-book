"""Root locus of a three-pole amplifier as loop gain increases. With one pole a
loop only gets faster; with three, two of the closed-loop poles curve toward and
cross the jw axis -- the onset of ringing and then oscillation. Open-loop
L(s)=K/((s+1)(s+2)(s+3)); closed-loop poles are the roots of the characteristic
polynomial s^3+6s^2+11s+(6+K)=0 as K sweeps up."""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_LINE, GUIDE_RED

apply_style()

Ks = np.linspace(0, 140, 600)
roots = np.array([np.roots([1, 6, 11, 6 + K]) for K in Ks])  # shape (N,3)

# order roots per step to draw continuous branches
ordered = np.zeros_like(roots)
ordered[0] = roots[0]
for i in range(1, len(Ks)):
    prev = ordered[i-1]
    cur = list(roots[i])
    for j in range(3):
        # pick the closest remaining root to prev[j]
        k = min(range(len(cur)), key=lambda m: abs(cur[m] - prev[j]))
        ordered[i, j] = cur.pop(k)

fig, ax = plt.subplots(figsize=(5.4, 4.4))
ax.axhline(0, color="0.35", lw=0.7)
ax.axvline(0, color="0.35", lw=0.7)

colors = [GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER]
for j in range(3):
    ax.plot(ordered[:, j].real, ordered[:, j].imag, color=colors[j], lw=1.4)

# open-loop poles (K=0)
ax.plot([-1, -2, -3], [0, 0, 0], "x", color="0.25", ms=10, mew=2.0,
        label="open-loop poles ($K=0$)")

# crossing point: K=60, omega=sqrt(11)
wc = np.sqrt(11)
ax.plot([0, 0], [wc, -wc], "o", mfc="none", mec=GUIDE_RED, ms=10, mew=1.8,
        label=r"axis crossing ($K{=}60$)")
ax.annotate("poles cross into\nright half-plane\n(oscillation)",
            xy=(0, wc), xytext=(0.55, 2.6), color=GUIDE_RED, fontsize=8,
            arrowprops=dict(arrowstyle="->", color=GUIDE_RED, lw=0.9))
ax.annotate("increasing loop gain $K$", xy=(-1.4, 1.6), color="0.3", fontsize=8)

ax.set_xlabel(r"$\sigma$ (real)")
ax.set_ylabel(r"$j\omega$ (imag)")
ax.set_xlim(-4.5, 1.4)
ax.set_ylim(-4.2, 4.2)
ax.set_aspect("equal")
ax.legend(loc="lower left", fontsize=8)
ax.grid(False)

save(fig, "opamp_rootlocus")
