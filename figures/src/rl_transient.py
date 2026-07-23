"""RL inductor-current transient: rise and decay, normalized, with the
one-time-constant marks (tau = L/R)."""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER

apply_style()

t = np.linspace(0, 5, 400)          # time in units of tau = L/R
rise = 1 - np.exp(-t)
decay = np.exp(-t)

fig, ax = plt.subplots(figsize=(6.2, 3.0))
ax.plot(t, rise, color=GUIDE_BLUE, label=r"rise: $i=\dfrac{E}{R}(1-e^{-Rt/L})$")
ax.plot(t, decay, color=GUIDE_GREEN, label=r"decay: $i=I_0\,e^{-Rt/L}$")
ax.axvline(1, color=GUIDE_AMBER, ls="--", lw=0.9)
ax.plot(1, 1-np.exp(-1), "o", color=GUIDE_BLUE, ms=5, zorder=5)
ax.plot(1, np.exp(-1), "o", color=GUIDE_GREEN, ms=5, zorder=5)
ax.annotate(r"$63.2\%$ at $t=L/R$", xy=(1, 1-np.exp(-1)), xytext=(1.5, 0.80),
            arrowprops=dict(arrowstyle="->", color="0.35", lw=0.8))
ax.annotate(r"$36.8\%$ at $t=L/R$", xy=(1, np.exp(-1)), xytext=(1.5, 0.20),
            arrowprops=dict(arrowstyle="->", color="0.35", lw=0.8))
ax.set_xlabel(r"Time $t/(L/R)$")
ax.set_ylabel(r"Inductor current (normalized)")
ax.set_xlim(0, 5)
ax.set_ylim(0, 1.05)
ax.legend(loc="center right", fontsize=8)

save(fig, "rl_transient")
