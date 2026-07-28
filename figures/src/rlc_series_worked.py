"""Specific plots for the series-RLC worked example:
L = 10 uH, C = 220 pF, R = 5 Ohm  ->  f0 = 3.39 MHz, Qs = 42.6, zeta = 0.0117.

Top-left:    Bode magnitude of v_C/u on a real Hz axis -- the Q ~ 42.6 peak.
Bottom-left: phase, sweeping 0 -> -180 deg through -90 deg at f0.
Right:       root locus as R is swept, with the actual R = 5 Ohm pole marked
             hugging the jw axis.
"""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_RED, GUIDE_LINE

apply_style()

L = 10e-6
C = 220e-12
R0 = 5.0
w0 = 1.0/np.sqrt(L*C)
f0 = w0/(2*np.pi)
Q0 = w0*L/R0

fig = plt.figure(figsize=(6.8, 3.5))
gs = fig.add_gridspec(2, 2, width_ratios=[1.2, 1.0], hspace=0.18, wspace=0.36)
axm = fig.add_subplot(gs[0, 0])
axp = fig.add_subplot(gs[1, 0], sharex=axm)
axr = fig.add_subplot(gs[:, 1])

# ---- Bode of V_C/U = w0^2/(s^2 + (w0/Q)s + w0^2) ----
f = np.logspace(np.log10(f0) - 1.6, np.log10(f0) + 1.6, 1400)
s = 1j*2*np.pi*f
G = w0**2/(s**2 + (w0/Q0)*s + w0**2)
axm.semilogx(f/1e6, 20*np.log10(np.abs(G)), color=GUIDE_BLUE, lw=1.8)
axm.axvline(f0/1e6, color=GUIDE_AMBER, ls=":", lw=1.1)
peak = 20*np.log10(Q0)
axm.plot(f0/1e6, peak, "o", color=GUIDE_RED, ms=5, zorder=6)
axm.annotate(rf"peak $\approx Q={Q0:.0f}$" "\n" rf"(${peak:.0f}$ dB) at $f_0$",
             xy=(f0/1e6, peak), xytext=(0.16, 22), color=GUIDE_RED, fontsize=7.5,
             arrowprops=dict(arrowstyle="->", color=GUIDE_RED, lw=0.8))
axm.annotate(r"$-40$ dB/decade", xy=(14, -13), color="0.35", fontsize=7.5,
             ha="left", va="center")
axm.set_ylabel("Mag. (dB)")
axm.set_ylim(-48, 45)
axm.tick_params(labelbottom=False)

axp.semilogx(f/1e6, np.degrees(np.angle(G)), color=GUIDE_GREEN, lw=1.8)
axp.axvline(f0/1e6, color=GUIDE_AMBER, ls=":", lw=1.1)
axp.plot(f0/1e6, -90, "o", color=GUIDE_GREEN, ms=5, zorder=6)
axp.annotate(r"$-90^\circ$ at $f_0$", xy=(f0/1e6, -90), xytext=(0.16, -60),
             color="0.3", fontsize=7.5,
             arrowprops=dict(arrowstyle="->", color="0.4", lw=0.8))
axp.set_ylabel("Phase (deg)")
axp.set_xlabel(r"Frequency (MHz),  $f_0=%.2f$ MHz" % (f0/1e6))
axp.set_ylim(-195, 15)
axp.set_yticks([0, -90, -180])

# ---- root locus as R sweeps 0 -> beyond critical ----
axr.axhline(0, color="0.35", lw=0.7)
axr.axvline(0, color="0.35", lw=0.7)
scale = 1e7  # plot in units of 10^7 /s
th = np.linspace(0, 2*np.pi, 400)
axr.plot(w0*np.cos(th)/scale, w0*np.sin(th)/scale, ls="--", color=GUIDE_LINE, lw=0.9)
Rcrit = 2*np.sqrt(L/C)
Rs = np.linspace(0, Rcrit, 400)
alpha = Rs/(2*L)
wd = np.sqrt(np.maximum(w0**2 - alpha**2, 0))
axr.plot(-alpha/scale, wd/scale, color=GUIDE_BLUE, lw=1.6)
axr.plot(-alpha/scale, -wd/scale, color=GUIDE_BLUE, lw=1.6)
# overdamped branches along the real axis
Ro = np.linspace(Rcrit, 4*Rcrit, 200)
ao = Ro/(2*L)
rad = np.sqrt(ao**2 - w0**2)
axr.plot((-ao + rad)/scale, np.zeros_like(ao), color=GUIDE_GREEN, lw=1.6)
axr.plot((-ao - rad)/scale, np.zeros_like(ao), color=GUIDE_GREEN, lw=1.6)
# the actual design point R = 5 ohm
a0 = R0/(2*L)
wd0 = np.sqrt(w0**2 - a0**2)
axr.plot([-a0/scale, -a0/scale], [wd0/scale, -wd0/scale], "x", color=GUIDE_RED,
         ms=10, mew=2.2, zorder=6)
axr.annotate(rf"$R={R0:g}\,\Omega$  ($Q={Q0:.0f}$)",
             ha="left", va="center",
             xy=(-a0/scale, wd0/scale), xytext=(-3.0, 1.85), color=GUIDE_RED,
             fontsize=7.5,
             arrowprops=dict(arrowstyle="->", color=GUIDE_RED, lw=0.8))
axr.plot(-w0/scale, 0, "o", color=GUIDE_AMBER, ms=5, zorder=6)
axr.annotate(rf"critical: $R={Rcrit:.0f}\,\Omega$", xy=(-w0/scale, 0),
             xytext=(-2.05, -1.55), color=GUIDE_AMBER, fontsize=7.5,
             arrowprops=dict(arrowstyle="->", color=GUIDE_AMBER, lw=0.8))
axr.annotate(r"$|s|=\omega_0$", xy=(1.15, -2.28), color="0.4", fontsize=7.5,
             ha="center")
axr.set_xlim(-3.1, 1.6)
axr.set_ylim(-2.5, 2.5)
axr.set_aspect("equal")
axr.set_xlabel(r"$\sigma$  ($10^7$ s$^{-1}$)")
axr.set_ylabel(r"$j\omega$  ($10^7$ s$^{-1}$)")
axr.grid(False)

save(fig, "rlc_series_worked")
