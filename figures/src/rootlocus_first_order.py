"""Root locus of a first-order circuit (RC or RL): the single real pole at
-1/tau slides along the negative real axis as the time constant changes. There is
never an imaginary part, so a first-order circuit cannot ring."""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_AMBER

apply_style()

fig, ax = plt.subplots(figsize=(6.0, 1.9))

# pole positions for a few time constants (arbitrary units): pole = -1/tau
poles = [-3.0, -2.0, -1.2, -0.6]
ax.plot(poles, [0]*len(poles), "o", color=GUIDE_BLUE, ms=7, zorder=5)
# arrow showing motion toward the origin as tau increases (e.g. larger R or C)
ax.annotate("", xy=(-0.35, 0), xytext=(-3.4, 0),
            arrowprops=dict(arrowstyle="->", color=GUIDE_AMBER, lw=1.4))
ax.annotate(r"increasing $\tau$ (slower)", xy=(-2.0, 0.16), color=GUIDE_AMBER,
            ha="center", fontsize=9)
ax.annotate(r"faster", xy=(-3.0, -0.22), color="0.4", ha="center", fontsize=9)
ax.annotate(r"$s=-1/\tau$", xy=(-0.6, 0), xytext=(-0.55, 0.18), color=GUIDE_BLUE,
            fontsize=9)

ax.axhline(0, color="0.3", lw=0.8)
ax.axvline(0, color="0.3", lw=0.8)
ax.set_yticks([])
ax.set_xlim(-3.6, 0.5)
ax.set_ylim(-0.5, 0.5)
ax.set_xlabel(r"$\sigma$ (real axis)")
ax.grid(False)

save(fig, "rootlocus_first_order")
