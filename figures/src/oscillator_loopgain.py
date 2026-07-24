"""Barkhausen condition on a loop-gain Bode plot. For a three-identical-pole loop
L(s)=K/(1+s/w0)^3, the phase reaches -180 deg at w=sqrt(3) w0. Choosing K=8 makes
|L|=1 (0 dB) exactly there: the loop gain is unity with 180 deg of lag, so
L=-1 and the closed-loop poles sit on the jw axis -- steady oscillation."""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER

apply_style()

w0 = 1.0
K = 8.0                      # gives |L|=1 at the -180 deg frequency
w = np.logspace(-1, 1.3, 700)
L = K/(1 + 1j*w/w0)**3
mag = 20*np.log10(np.abs(L))
phase = np.degrees(np.angle(L))
phase = np.unwrap(np.radians(phase))
phase = np.degrees(phase)

w_osc = np.sqrt(3)*w0        # phase = -180 deg here

fig, (axm, axp) = plt.subplots(2, 1, figsize=(6.2, 4.4), sharex=True)

axm.semilogx(w, mag, color=GUIDE_BLUE, lw=1.9)
axm.axhline(0, color="0.6", lw=0.7)
axm.axvline(w_osc, color=GUIDE_AMBER, ls=":", lw=1.1)
axm.plot(w_osc, 0, "o", color=GUIDE_BLUE, ms=5, zorder=6)
axm.annotate(r"$|L|=1$ (0 dB)", xy=(w_osc, 0), xytext=(0.12, -6),
             color="0.3", fontsize=8,
             arrowprops=dict(arrowstyle="->", color="0.4", lw=0.8))
axm.set_ylabel("Loop gain (dB)")
axm.set_ylim(-30, 22)

axp.semilogx(w, phase, color=GUIDE_GREEN, lw=1.9)
axp.axhline(-180, color="0.6", lw=0.7)
axp.axvline(w_osc, color=GUIDE_AMBER, ls=":", lw=1.1)
axp.plot(w_osc, -180, "o", color=GUIDE_GREEN, ms=5, zorder=6)
axp.annotate(r"$\angle L=-180^\circ$ at $\omega_{\mathrm{osc}}=\sqrt{3}\,\omega_0$",
             xy=(w_osc, -180), xytext=(0.12, -120),
             color="0.3", fontsize=8,
             arrowprops=dict(arrowstyle="->", color="0.4", lw=0.8))
axp.set_ylabel("Phase (deg)")
axp.set_xlabel(r"Normalized frequency $\omega/\omega_0$")
axp.set_ylim(-290, 10)
axp.set_yticks([0, -90, -180, -270])

save(fig, "oscillator_loopgain")
