"""Proportional feedback on a second-order system.
Closed-loop denominator: s^2 + 2*zeta*w0*s + w0^2*(1+A0*beta), so
  w_cl = w0*sqrt(1+A0*beta),  zeta_cl = zeta/sqrt(1+A0*beta).
Left: the pole pair rises vertically -- real part pinned at -zeta*w0 while the
      imaginary part grows, so it approaches (but never crosses) the jw axis.
Right: the step response develops overshoot and ringing as zeta_cl falls.
"""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_LINE

apply_style()

w0 = 1.0
zeta = 0.6
A0 = 1.0
betas = [0.0, 1.0, 4.0, 9.0]
colors = [GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_LINE]

fig, (axp, axs) = plt.subplots(1, 2, figsize=(6.6, 3.0))

# ---- left: closed-loop pole pair ----
axp.axhline(0, color="0.35", lw=0.7)
axp.axvline(0, color="0.35", lw=0.7)
sigma = -zeta*w0                      # real part is independent of beta
for b, c in zip(betas, colors):
    wcl = w0*np.sqrt(1 + A0*b)
    zcl = zeta/np.sqrt(1 + A0*b)
    wd = wcl*np.sqrt(max(1 - zcl**2, 0.0))
    axp.plot([sigma, sigma], [wd, -wd], "x", color=c, ms=10, mew=2.1,
             label=rf"$\beta={b:g}$")
# vertical dashed line the poles ride
axp.axvline(sigma, color="0.6", ls="--", lw=0.9)
axp.annotate(r"$\sigma=-\zeta\omega_0$ fixed", xy=(sigma, 2.75),
             xytext=(sigma-0.05, 2.85), color="0.35", fontsize=7.5, ha="right")
axp.annotate("", xy=(sigma, 2.55), xytext=(sigma, 0.9),
             arrowprops=dict(arrowstyle="-|>", color="0.4", lw=1.2))
axp.annotate(r"increasing $\beta$", xy=(sigma+0.08, 1.7), color="0.35",
             fontsize=7.5, ha="left")
axp.set_xlim(-1.5, 0.6)
axp.set_ylim(-3.2, 3.2)
axp.set_xlabel(r"$\sigma$ (real)")
axp.set_ylabel(r"$j\omega$ (imag)")
axp.legend(loc="lower left", fontsize=7)
axp.grid(False)

# ---- right: closed-loop step responses (normalized to final value) ----
t = np.linspace(0, 14, 900)
for b, c in zip(betas, colors):
    wcl = w0*np.sqrt(1 + A0*b)
    zcl = zeta/np.sqrt(1 + A0*b)
    wd = wcl*np.sqrt(1 - zcl**2)
    y = 1 - np.exp(-zcl*wcl*t)*(np.cos(wd*t) + (zcl*wcl/wd)*np.sin(wd*t))
    axs.plot(t, y, color=c, lw=1.6, label=rf"$\zeta_{{cl}}={zcl:.2f}$")
axs.axhline(1.0, color="0.6", ls=":", lw=0.8)
axs.set_xlabel(r"time $\omega_0 t$")
axs.set_ylabel("step response (normalized)")
axs.set_xlim(0, 14)
axs.set_ylim(0, 1.85)
axs.legend(loc="upper right", fontsize=7)

fig.tight_layout()
save(fig, "feedback_second_order")
