"""The phasor picture, two panels:
(left) a complex constant X shown in polar (r, theta) and rectangular (a+jb) form
       on the complex plane;
(right) multiplying by e^{j w t} rotates the phasor at rate w, and its real-axis
       projection traces the sinusoid x(t) = sqrt(2) Re{X e^{j w t}}.
"""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_LINE

apply_style()

r = 1.15                       # |X|
phi = np.radians(35.0)         # angle of X
a, b = r*np.cos(phi), r*np.sin(phi)

fig = plt.figure(figsize=(6.7, 3.1))
gs = fig.add_gridspec(1, 2, width_ratios=[1.0, 1.35], wspace=0.32)
axA = fig.add_subplot(gs[0])
axB = fig.add_subplot(gs[1])

# ---- Panel A: complex plane, polar <-> rectangular ----
axA.set_aspect("equal")
axA.axhline(0, color="0.35", lw=0.7)
axA.axvline(0, color="0.35", lw=0.7)
th = np.linspace(0, 2*np.pi, 400)
axA.plot(r*np.cos(th), r*np.sin(th), ls="--", color=GUIDE_LINE, lw=0.9)
# phasor arrow
axA.annotate("", xy=(a, b), xytext=(0, 0),
             arrowprops=dict(arrowstyle="-|>", color=GUIDE_BLUE, lw=2.0))
# rectangular projections
axA.plot([a, a], [0, b], ls=":", color=GUIDE_GREEN, lw=1.1)
axA.plot([0, a], [b, b], ls=":", color=GUIDE_GREEN, lw=1.1)
# angle arc
arc = np.linspace(0, phi, 40)
axA.plot(0.34*np.cos(arc), 0.34*np.sin(arc), color=GUIDE_AMBER, lw=1.1)
axA.annotate(r"$\phi$", xy=(0.40, 0.12), color=GUIDE_AMBER, fontsize=10)
axA.annotate(r"$r=|X|$", xy=(0.48*a-0.20, 0.48*b+0.17), color=GUIDE_BLUE,
             fontsize=9, rotation=np.degrees(phi), ha="center", va="center")
axA.annotate(r"$a=|X|\cos\phi$", xy=(a, 0), xytext=(a-0.05, -0.22),
             color=GUIDE_GREEN, fontsize=8, ha="center")
axA.annotate(r"$b=|X|\sin\phi$", xy=(0, b), xytext=(-0.16, b),
             color=GUIDE_GREEN, fontsize=8, ha="right", va="center")
axA.plot(a, b, "o", color=GUIDE_BLUE, ms=4, zorder=6)
axA.set_xlim(-1.4, 1.5)
axA.set_ylim(-1.4, 1.5)
axA.set_xlabel("real")
axA.set_ylabel("imaginary")
axA.set_title(r"$X=|X|\angle\phi=a+\mathrm{j}b$", fontsize=9)
axA.grid(False)

# ---- Panel B: rotation -> sinusoid ----
wt = np.linspace(0, 2*2*np.pi, 500)
x = np.sqrt(2)*r*np.cos(wt + phi)
axB.plot(wt, x, color=GUIDE_BLUE, lw=1.8)
amp = np.sqrt(2)*r
axB.axhline(amp, ls="--", color=GUIDE_LINE, lw=0.8)
axB.axhline(-amp, ls="--", color=GUIDE_LINE, lw=0.8)
axB.annotate(r"$\sqrt{2}\,|X|$", xy=(2*2*np.pi, amp), xytext=(-4, 4),
             textcoords="offset points", color="0.35", fontsize=8, ha="right")
# phase marker: peak occurs at wt = -phi (i.e. first peak left of 0), mark shift
axB.plot(0, np.sqrt(2)*r*np.cos(phi), "o", color=GUIDE_GREEN, ms=5, zorder=6)
axB.annotate(r"$x(0)=\sqrt{2}|X|\cos\phi$",
             xy=(0, np.sqrt(2)*r*np.cos(phi)), xytext=(0.62, 1.93),
             color=GUIDE_GREEN, fontsize=8, ha="left", va="center",
             arrowprops=dict(arrowstyle="->", color="0.4", lw=0.8))
# rotation annotation
axB.annotate(r"$\times\,e^{\mathrm{j}\omega t}$ rotates at $\omega$: one turn per period $T$",
             xy=(np.pi*2, -1.90), color=GUIDE_AMBER, fontsize=8, ha="center",
             va="center")
axB.set_xlim(0, 2*2*np.pi)
axB.set_ylim(-2.15, 2.15)
axB.set_xticks([0, 2*np.pi, 4*np.pi])
axB.set_xticklabels(["0", r"$T$", r"$2T$"])
axB.set_xlabel(r"time $t$")
axB.set_ylabel(r"$x(t)=\sqrt{2}\,\Re\{X e^{\mathrm{j}\omega t}\}$", fontsize=9)

save(fig, "phasor_unit_circle")
