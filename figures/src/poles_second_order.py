"""Second-order pole locations in the s-plane for several damping ratios,
showing the poles lie on a circle of radius omega_0 and that cos(theta)=zeta."""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_RED

apply_style()

w0 = 1.0
zetas = [0.0, 0.25, 0.5, 0.85]
colors = [GUIDE_RED, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER]

fig, ax = plt.subplots(figsize=(4.8, 4.4))

# circle of radius omega_0 (left half only relevant, draw full dashed)
th = np.linspace(0, 2*np.pi, 400)
ax.plot(w0*np.cos(th), w0*np.sin(th), color="0.65", ls="--", lw=0.9)

for zeta, c in zip(zetas, colors):
    sigma = -zeta*w0
    wd = w0*np.sqrt(max(0.0, 1-zeta**2))
    ax.plot([sigma, sigma], [wd, -wd], "o", color=c, ms=6, zorder=5,
            label=rf"$\zeta={zeta}$")
    if zeta == 0.5:
        # damping angle from negative real axis
        ax.plot([0, sigma], [0, wd], color="0.4", lw=0.8)
        ax.annotate(r"$\theta$", xy=(sigma*0.35, wd*0.35),
                    xytext=(sigma*0.35 - 0.16, wd*0.35 + 0.02))

ax.axhline(0, color="0.3", lw=0.7)
ax.axvline(0, color="0.3", lw=0.7)
ax.annotate(r"$|s|=\omega_0$", xy=(-0.34, 1.04), color="0.45")
ax.annotate(r"$\cos\theta=\zeta$", xy=(-1.45, 0.12), color="0.3")
ax.set_xlabel(r"$\sigma$ (real)")
ax.set_ylabel(r"$j\omega$ (imag)")
ax.set_xlim(-1.55, 0.4)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect("equal")
ax.legend(loc="lower left", fontsize=8)

save(fig, "poles_second_order")
