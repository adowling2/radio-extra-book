"""First-order low-pass Bode plot (magnitude and phase), normalized to the
corner frequency, with the -3 dB corner and asymptotes marked."""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER

apply_style()

w = np.logspace(-2, 2, 500)          # normalized frequency w/w_c
mag = 20 * np.log10(1.0 / np.sqrt(1.0 + w**2))
phase = -np.degrees(np.arctan(w))

fig, (axm, axp) = plt.subplots(2, 1, figsize=(6.2, 4.3), sharex=True)

# Magnitude
axm.semilogx(w, mag, color=GUIDE_BLUE, label="exact")
# Asymptotes: 0 dB below corner, -20 dB/decade above
axm.plot([0.01, 1], [0, 0], color=GUIDE_AMBER, ls="--", lw=1.0)
axm.plot([1, 100], [0, -40], color=GUIDE_AMBER, ls="--", lw=1.0,
         label="asymptotes")
axm.axvline(1, color="0.55", ls=":", lw=1.0)
axm.plot(1, -3.0103, "o", color=GUIDE_BLUE, ms=5, zorder=5)
axm.annotate(r"corner $\omega_c$: $-3.01$ dB",
             xy=(1, -3.0103), xytext=(1.7, 4),
             arrowprops=dict(arrowstyle="->", color="0.35", lw=0.8))
axm.set_ylabel("Magnitude (dB)")
axm.set_ylim(-42, 12)
axm.legend(loc="lower left")

# Phase
axp.semilogx(w, phase, color=GUIDE_GREEN)
axp.axvline(1, color="0.55", ls=":", lw=1.0)
axp.plot(1, -45, "o", color=GUIDE_GREEN, ms=5, zorder=5)
axp.annotate(r"$-45^\circ$ at $\omega_c$",
             xy=(1, -45), xytext=(2.2, -20),
             arrowprops=dict(arrowstyle="->", color="0.35", lw=0.8))
axp.set_ylabel("Phase (degrees)")
axp.set_xlabel(r"Normalized frequency $\omega/\omega_c$")
axp.set_ylim(-95, 5)
axp.set_yticks([-90, -45, 0])

save(fig, "bode_first_order_lowpass")
