"""First-order step response, normalized, marking one time constant (63.2%)
and the 5-tau settling region."""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_AMBER

apply_style()

t = np.linspace(0, 6, 400)          # time in units of tau
y = 1 - np.exp(-t)

fig, ax = plt.subplots(figsize=(6.2, 2.9))
ax.plot(t, y, color=GUIDE_BLUE)
ax.axhline(1.0, color="0.55", ls=":", lw=1.0)
# one time constant
ax.plot(1, 1 - np.exp(-1), "o", color=GUIDE_AMBER, ms=5, zorder=5)
ax.annotate(r"$t=\tau$: $63.2\%$",
            xy=(1, 1 - np.exp(-1)), xytext=(1.4, 0.42),
            arrowprops=dict(arrowstyle="->", color="0.35", lw=0.8))
ax.axvline(1, color=GUIDE_AMBER, ls="--", lw=0.9)
# 5 tau settling
ax.axvline(5, color="0.55", ls="--", lw=0.9)
ax.annotate(r"$5\tau$: settled", xy=(5, 0.2), xytext=(4.0, 0.12))
ax.set_xlabel(r"Time $t/\tau$")
ax.set_ylabel(r"$y(t)/y(\infty)$")
ax.set_ylim(0, 1.08)
ax.set_xlim(0, 6)

save(fig, "step_first_order")
