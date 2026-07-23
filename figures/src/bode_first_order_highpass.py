"""First-order high-pass Bode plot (magnitude and phase), normalized to the
corner frequency -- the RC response taken across the resistor."""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER

apply_style()

w = np.logspace(-2, 2, 500)          # normalized frequency w/w_c
H = (1j*w) / (1 + 1j*w)
mag = 20*np.log10(np.abs(H))
phase = np.degrees(np.angle(H))

fig, (axm, axp) = plt.subplots(2, 1, figsize=(6.2, 4.3), sharex=True)

axm.semilogx(w, mag, color=GUIDE_BLUE, label="exact")
axm.plot([0.01, 1], [-40, 0], color=GUIDE_AMBER, ls="--", lw=1.0,
         label="asymptotes")
axm.plot([1, 100], [0, 0], color=GUIDE_AMBER, ls="--", lw=1.0)
axm.axvline(1, color="0.55", ls=":", lw=1.0)
axm.plot(1, -3.0103, "o", color=GUIDE_BLUE, ms=5, zorder=5)
axm.annotate(r"corner $\omega_c$: $-3.01$ dB", xy=(1, -3.0103), xytext=(0.02, 4),
             arrowprops=dict(arrowstyle="->", color="0.35", lw=0.8))
axm.set_ylabel("Magnitude (dB)")
axm.set_ylim(-42, 12)
axm.legend(loc="lower right")

axp.semilogx(w, phase, color=GUIDE_GREEN)
axp.axvline(1, color="0.55", ls=":", lw=1.0)
axp.plot(1, 45, "o", color=GUIDE_GREEN, ms=5, zorder=5)
axp.annotate(r"$+45^\circ$ at $\omega_c$", xy=(1, 45), xytext=(1.8, 20),
             arrowprops=dict(arrowstyle="->", color="0.35", lw=0.8))
axp.set_ylabel("Phase (degrees)")
axp.set_xlabel(r"Normalized frequency $\omega/\omega_c$")
axp.set_ylim(-5, 95)
axp.set_yticks([0, 45, 90])

save(fig, "bode_first_order_highpass")
