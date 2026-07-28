"""Specific plots for the RC worked example: R = 4.7 kOhm, C = 100 nF,
so tau = 470 us, f_c = 339 Hz, pole at -2130 1/s.

Left panel:  Bode magnitude/phase of the low-pass on a real Hz axis, with the
             339 Hz corner marked.
Right panel: root locus in real units -- the single pole -1/(RC) as R is swept,
             showing that changing R only slides the pole along the real axis.
"""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_RED

apply_style()

R0 = 4.7e3
C = 100e-9
tau0 = R0*C
fc0 = 1.0/(2*np.pi*tau0)

fig = plt.figure(figsize=(6.7, 3.4))
gs = fig.add_gridspec(2, 2, width_ratios=[1.25, 1.0], hspace=0.18, wspace=0.34)
axm = fig.add_subplot(gs[0, 0])
axp = fig.add_subplot(gs[1, 0], sharex=axm)
axr = fig.add_subplot(gs[:, 1])

# ---- Bode of the specific low-pass ----
f = np.logspace(0, 5, 800)
G = 1.0/(1 + 1j*2*np.pi*f*tau0)
axm.semilogx(f, 20*np.log10(np.abs(G)), color=GUIDE_BLUE, lw=1.9)
axm.axvline(fc0, color=GUIDE_AMBER, ls=":", lw=1.1)
axm.plot(fc0, -3.0103, "o", color=GUIDE_BLUE, ms=5, zorder=6)
axm.annotate(rf"$f_c={fc0:.0f}$ Hz, $-3$ dB", xy=(fc0, -3.0103),
             xytext=(1.25, -27), color="0.3", fontsize=7.5, ha="left", va="center",
             arrowprops=dict(arrowstyle="->", color="0.4", lw=0.8))
axm.set_ylabel("Mag. (dB)")
axm.set_ylim(-45, 8)
axm.tick_params(labelbottom=False)

axp.semilogx(f, np.degrees(np.angle(G)), color=GUIDE_GREEN, lw=1.9)
axp.axvline(fc0, color=GUIDE_AMBER, ls=":", lw=1.1)
axp.plot(fc0, -45, "o", color=GUIDE_GREEN, ms=5, zorder=6)
axp.annotate(r"$-45^\circ$", xy=(fc0, -45), xytext=(1.4e3, -26),
             color="0.3", fontsize=7.5,
             arrowprops=dict(arrowstyle="->", color="0.4", lw=0.8))
axp.set_ylabel("Phase (deg)")
axp.set_xlabel("Frequency (Hz)")
axp.set_ylim(-99, 9)
axp.set_yticks([0, -45, -90])

# ---- root locus in real units: sweep R ----
axr.axhline(0, color="0.35", lw=0.7)
axr.axvline(0, color="0.35", lw=0.7)
Rs = np.array([1.0e3, 2.2e3, 4.7e3, 10.0e3])
poles = -1.0/(Rs*C)
cols = [GUIDE_GREEN, GUIDE_GREEN, GUIDE_RED, GUIDE_BLUE]
for Rv, p, c in zip(Rs, poles, cols):
    axr.plot(p/1e3, 0, "x", color=c, ms=10, mew=2.1)
    lab = rf"{Rv/1e3:g} k$\Omega$"
    axr.annotate(lab, xy=(p/1e3, 0), xytext=(p/1e3, 0.16 if Rv != 4.7e3 else -0.22),
                 color=c, fontsize=7, ha="center",
                 va="bottom" if Rv != 4.7e3 else "top")
axr.annotate("", xy=(-0.9, -0.42), xytext=(-9.6, -0.42),
             arrowprops=dict(arrowstyle="-|>", color="0.45", lw=1.2))
axr.annotate(r"increasing $R$ (slower)", xy=(-5.2, -0.53), color="0.35",
             fontsize=7.5, ha="center", va="top")
axr.annotate(r"$s=-1/RC$", xy=(-7.5, 0.62), color="0.3", fontsize=8, ha="center")
axr.set_xlim(-11.5, 2.2)
axr.set_ylim(-0.85, 0.85)
axr.set_xlabel(r"$\sigma$  ($10^3$ s$^{-1}$)")
axr.set_ylabel(r"$j\omega$")
axr.set_yticks([0])
axr.grid(False)

save(fig, "rc_worked")
