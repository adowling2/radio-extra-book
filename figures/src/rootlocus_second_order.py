"""Root locus of a canonical second-order system s^2 + 2*zeta*w0*s + w0^2 as the
damping zeta sweeps 0 -> infinity (the RLC-vs-R story, generically): poles start
on the jw axis, arc along the |s|=w0 circle, meet at -w0 (critical), then split
along the negative real axis (overdamped)."""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_RED

apply_style()

w0 = 1.0
zetas = np.linspace(0, 3.0, 600)
upper, lower = [], []
for z in zetas:
    r = np.roots([1, 2*z*w0, w0**2])
    r = sorted(r, key=lambda x: x.imag)
    lower.append(r[0]); upper.append(r[-1])
upper = np.array(upper); lower = np.array(lower)

fig, ax = plt.subplots(figsize=(4.9, 4.4))
th = np.linspace(0, 2*np.pi, 400)
ax.plot(w0*np.cos(th), w0*np.sin(th), color="0.7", ls="--", lw=0.9)
ax.plot(upper.real, upper.imag, color=GUIDE_BLUE, lw=1.6)
ax.plot(lower.real, lower.imag, color=GUIDE_BLUE, lw=1.6)

# key marks
ax.plot([0, 0], [w0, -w0], "o", color=GUIDE_RED, ms=6, zorder=6)
ax.annotate(r"$\zeta=0$", xy=(0, w0), xytext=(0.06, w0-0.05), color=GUIDE_RED)
ax.plot(-w0, 0, "o", color=GUIDE_AMBER, ms=6, zorder=6)
ax.annotate("critical\n" r"$\zeta=1$", xy=(-w0, 0), xytext=(-w0-0.02, 0.18),
            color=GUIDE_AMBER, ha="center", fontsize=8)
# overdamped arrows along real axis
ax.annotate("", xy=(-2.4, 0), xytext=(-1.05, 0),
            arrowprops=dict(arrowstyle="->", color=GUIDE_GREEN, lw=1.4))
ax.annotate("", xy=(-0.42, 0), xytext=(-0.95, 0),
            arrowprops=dict(arrowstyle="->", color=GUIDE_GREEN, lw=1.4))
ax.annotate("overdamped", xy=(-1.9, 0.12), color=GUIDE_GREEN, fontsize=8)
ax.annotate("increasing\n" r"$\zeta$ (e.g. $R$)", xy=(-0.7, 0.75),
            color="0.35", fontsize=8, ha="center")

ax.axhline(0, color="0.3", lw=0.7)
ax.axvline(0, color="0.3", lw=0.7)
ax.set_xlabel(r"$\sigma$ (real)")
ax.set_ylabel(r"$j\omega$ (imag)")
ax.set_xlim(-2.6, 0.5)
ax.set_ylim(-1.25, 1.25)
ax.set_aspect("equal")

save(fig, "rootlocus_second_order")
