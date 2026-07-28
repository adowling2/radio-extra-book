"""Proportional feedback on a first-order system.
Left: the single closed-loop pole -wa(1+A0*beta) slides left along the real axis
      as beta grows -- a one-branch locus that never leaves the real axis.
Right: the closed-loop step response gets faster and lower (gain traded for
      bandwidth), since DC gain = A0/(1+A0*beta) and tau = 1/(wa(1+A0*beta)).
"""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_LINE

apply_style()

A0 = 10.0
wa = 1.0
betas = [0.0, 0.1, 0.3, 0.9]
colors = [GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_LINE]

fig, (axp, axs) = plt.subplots(1, 2, figsize=(6.6, 2.9))

# ---- left: pole locations on the real axis ----
axp.axhline(0, color="0.35", lw=0.7)
axp.axvline(0, color="0.35", lw=0.7)
for b, c in zip(betas, colors):
    p = -wa*(1 + A0*b)
    axp.plot(p, 0, "x", color=c, ms=11, mew=2.2,
             label=rf"$\beta={b:g}$")
# arrow showing direction of travel
axp.annotate("", xy=(-9.4, 0.42), xytext=(-1.4, 0.42),
             arrowprops=dict(arrowstyle="-|>", color="0.4", lw=1.2))
axp.annotate(r"increasing $\beta$ (faster)", xy=(-5.4, 0.55), color="0.35",
             fontsize=8, ha="center")
axp.set_xlim(-11.5, 1.6)
axp.set_ylim(-1.0, 1.0)
axp.set_xlabel(r"$\sigma$ (real)")
axp.set_ylabel(r"$j\omega$ (imag)")
axp.set_yticks([-1, 0, 1])
axp.legend(loc="lower left", fontsize=7.5)
axp.grid(False)

# ---- right: closed-loop step responses ----
t = np.linspace(0, 6, 500)
for b, c in zip(betas, colors):
    dc = A0/(1 + A0*b)
    tau = 1.0/(wa*(1 + A0*b))
    axs.plot(t, dc*(1 - np.exp(-t/tau)), color=c, lw=1.7,
             label=rf"$\beta={b:g}$")
axs.set_xlabel(r"time $\omega_a t$")
axs.set_ylabel("step response")
axs.set_xlim(0, 6)
axs.set_ylim(0, A0*1.05)
axs.legend(loc="center right", fontsize=7.5)

fig.tight_layout()
save(fig, "feedback_first_order")
