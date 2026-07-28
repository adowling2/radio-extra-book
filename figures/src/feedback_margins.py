"""Gain and phase margin on a loop-gain Bode plot.
Three-pole loop L(s) = K/(1+s/w0)^3 with K chosen to leave healthy margins.
  - gain crossover: |L| = 1 (0 dB)      -> phase margin measured there
  - phase crossover: angle L = -180 deg -> gain margin measured there
For this loop the phase reaches -180 deg at w = sqrt(3) w0, where |L| = K/8.
"""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_RED

apply_style()

w0 = 1.0
K = 3.0                      # < 8, so the loop is stable with real margins
w = np.logspace(-1, 1.3, 900)
L = K/(1 + 1j*w/w0)**3
mag = 20*np.log10(np.abs(L))
phase = np.degrees(np.unwrap(np.angle(L)))

# gain crossover: |L| = 1
i_gc = np.argmin(np.abs(mag))
w_gc, ph_gc = w[i_gc], phase[i_gc]
pm = ph_gc + 180.0                       # phase margin (deg)

# phase crossover: angle = -180 deg  (analytically w = sqrt(3) w0)
w_pc = np.sqrt(3)*w0
mag_pc = 20*np.log10(K/8.0)
gm = -mag_pc                             # gain margin (dB)

fig, (axm, axp) = plt.subplots(2, 1, figsize=(6.3, 4.5), sharex=True)

# ---- magnitude ----
axm.semilogx(w, mag, color=GUIDE_BLUE, lw=1.9)
axm.axhline(0, color="0.6", lw=0.8)
axm.axvline(w_gc, color=GUIDE_GREEN, ls=":", lw=1.1)
axm.axvline(w_pc, color=GUIDE_AMBER, ls=":", lw=1.1)
axm.plot(w_gc, 0, "o", color=GUIDE_GREEN, ms=5, zorder=6)
axm.plot(w_pc, mag_pc, "o", color=GUIDE_AMBER, ms=5, zorder=6)
# gain margin bar
axm.annotate("", xy=(w_pc, 0), xytext=(w_pc, mag_pc),
             arrowprops=dict(arrowstyle="<->", color=GUIDE_RED, lw=1.4))
axm.annotate(rf"gain margin $\approx {gm:.1f}$ dB", xy=(w_pc, mag_pc/2),
             xytext=(w_pc*1.25, mag_pc/2), color=GUIDE_RED, fontsize=8,
             va="center", ha="left")
axm.annotate("gain crossover\n" r"$|L|=1$", xy=(w_gc, 0), xytext=(0.115, 6),
             color=GUIDE_GREEN, fontsize=8,
             arrowprops=dict(arrowstyle="->", color=GUIDE_GREEN, lw=0.8))
axm.set_ylabel("Loop gain (dB)")
axm.set_ylim(-32, 16)

# ---- phase ----
axp.semilogx(w, phase, color=GUIDE_BLUE, lw=1.9)
axp.axhline(-180, color="0.6", lw=0.8)
axp.axvline(w_gc, color=GUIDE_GREEN, ls=":", lw=1.1)
axp.axvline(w_pc, color=GUIDE_AMBER, ls=":", lw=1.1)
axp.plot(w_gc, ph_gc, "o", color=GUIDE_GREEN, ms=5, zorder=6)
axp.plot(w_pc, -180, "o", color=GUIDE_AMBER, ms=5, zorder=6)
# phase margin bar
axp.annotate("", xy=(w_gc, -180), xytext=(w_gc, ph_gc),
             arrowprops=dict(arrowstyle="<->", color=GUIDE_RED, lw=1.4))
axp.annotate(rf"phase margin $\approx {pm:.0f}^\circ$",
             xy=(w_gc, (ph_gc-180)/2), xytext=(w_gc*0.82, (ph_gc-180)/2),
             color=GUIDE_RED, fontsize=8, va="center", ha="right")
axp.annotate("phase crossover\n" r"$\angle L=-180^\circ$", xy=(w_pc, -180),
             xytext=(w_pc*1.15, -105), color=GUIDE_AMBER, fontsize=8,
             arrowprops=dict(arrowstyle="->", color=GUIDE_AMBER, lw=0.8))
axp.set_ylabel("Phase (deg)")
axp.set_xlabel(r"Normalized frequency $\omega/\omega_0$")
axp.set_ylim(-290, 10)
axp.set_yticks([0, -90, -180, -270])

fig.tight_layout()
save(fig, "feedback_margins")
