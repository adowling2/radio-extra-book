"""Pole-zero plot of a notch (band-stop) response: a lightly damped complex pole
pair just inside the left half-plane, and a pair of transmission zeros on the
jw axis at the rejection frequency. Illustrates that poles set the resonance and
zeros set the rejection."""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_RED

apply_style()

w0 = 1.0
alpha = 0.18

fig, ax = plt.subplots(figsize=(4.9, 4.4))
# axes
ax.axhline(0, color="0.3", lw=0.7)
ax.axvline(0, color="0.3", lw=0.7)

# poles (x) just left of the axis
ax.plot([-alpha, -alpha], [w0, -w0], "x", color=GUIDE_BLUE, ms=11, mew=2.2,
        label="poles (natural modes)")
# zeros (o) on the jw axis at the rejection frequency
ax.plot([0, 0], [w0, -w0], "o", mfc="none", mec=GUIDE_RED, ms=11, mew=2.0,
        label="zeros (rejection)")

ax.annotate(r"$+j\omega_0$", xy=(0, w0), xytext=(0.08, w0+0.05), color=GUIDE_RED)
ax.annotate("pole pair\n" r"($-\alpha\pm j\omega_d$)", xy=(-alpha, w0),
            xytext=(-1.15, w0-0.02), color=GUIDE_BLUE, fontsize=8, va="center")

ax.set_xlabel(r"$\sigma$ (real)")
ax.set_ylabel(r"$j\omega$ (imag)")
ax.set_xlim(-1.4, 0.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect("equal")
ax.legend(loc="lower left", fontsize=8)

save(fig, "poles_zeros_notch")
