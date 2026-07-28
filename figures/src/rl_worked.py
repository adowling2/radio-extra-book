"""Specific plots for the RL worked example: L = 10 uH, R = 50 Ohm,
so tau = L/R = 200 ns, f_c = 796 kHz, pole at -5e6 1/s.

Left panel:  Bode of the output-across-R low-pass on a real Hz axis, marking the
             796 kHz corner and the 14 MHz operating point from the text.
Right panel: root locus as R is swept -- the pole -R/L slides LEFT as R grows,
             the mirror of the RC case.
"""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_RED

apply_style()

L = 10e-6
R0 = 50.0
tau0 = L/R0
fc0 = 1.0/(2*np.pi*tau0)

fig = plt.figure(figsize=(6.7, 3.4))
gs = fig.add_gridspec(2, 2, width_ratios=[1.25, 1.0], hspace=0.18, wspace=0.34)
axm = fig.add_subplot(gs[0, 0])
axp = fig.add_subplot(gs[1, 0], sharex=axm)
axr = fig.add_subplot(gs[:, 1])

# ---- Bode of v_R/u (low-pass, unity DC gain) ----
f = np.logspace(4, 8, 800)
G = 1.0/(1 + 1j*2*np.pi*f*tau0)
axm.semilogx(f, 20*np.log10(np.abs(G)), color=GUIDE_BLUE, lw=1.9)
axm.axvline(fc0, color=GUIDE_AMBER, ls=":", lw=1.1)
axm.plot(fc0, -3.0103, "o", color=GUIDE_BLUE, ms=5, zorder=6)
axm.annotate(rf"$f_c={fc0/1e3:.0f}$ kHz", xy=(fc0, -3.0103),
             xytext=(2.4e4, -16), color="0.3", fontsize=7.5,
             arrowprops=dict(arrowstyle="->", color="0.4", lw=0.8))
# 14 MHz operating point
f_op = 14e6
G_op = 1.0/(1 + 1j*2*np.pi*f_op*tau0)
axm.plot(f_op, 20*np.log10(np.abs(G_op)), "o", color=GUIDE_RED, ms=5, zorder=6)
axm.annotate(r"14 MHz:" "\n" rf"${20*np.log10(np.abs(G_op)):.0f}$ dB",
             xy=(f_op, 20*np.log10(np.abs(G_op))), xytext=(1.5e6, -33),
             color=GUIDE_RED, fontsize=7.5,
             arrowprops=dict(arrowstyle="->", color=GUIDE_RED, lw=0.8))
axm.set_ylabel("Mag. (dB)")
axm.set_ylim(-45, 8)
axm.tick_params(labelbottom=False)

axp.semilogx(f, np.degrees(np.angle(G)), color=GUIDE_GREEN, lw=1.9)
axp.axvline(fc0, color=GUIDE_AMBER, ls=":", lw=1.1)
axp.plot(fc0, -45, "o", color=GUIDE_GREEN, ms=5, zorder=6)
axp.annotate(r"$-45^\circ$", xy=(fc0, -45), xytext=(2.4e4, -30),
             color="0.3", fontsize=7.5,
             arrowprops=dict(arrowstyle="->", color="0.4", lw=0.8))
axp.set_ylabel("Phase (deg)")
axp.set_xlabel("Frequency (Hz)")
axp.set_ylim(-99, 9)
axp.set_yticks([0, -45, -90])

# ---- root locus: sweep R (pole = -R/L) ----
axr.axhline(0, color="0.35", lw=0.7)
axr.axvline(0, color="0.35", lw=0.7)
Rs = np.array([25.0, 50.0, 100.0])
poles = -Rs/L
cols = [GUIDE_BLUE, GUIDE_RED, GUIDE_GREEN]
for Rv, p, c in zip(Rs, poles, cols):
    axr.plot(p/1e6, 0, "x", color=c, ms=10, mew=2.1)
    axr.annotate(rf"{Rv:g} $\Omega$", xy=(p/1e6, 0),
                 xytext=(p/1e6, 0.16 if Rv != 50.0 else -0.22),
                 color=c, fontsize=7, ha="center",
                 va="bottom" if Rv != 50.0 else "top")
axr.annotate("", xy=(-9.6, -0.42), xytext=(-1.6, -0.42),
             arrowprops=dict(arrowstyle="-|>", color="0.45", lw=1.2))
axr.annotate(r"increasing $R$ (faster)", xy=(-5.6, -0.53), color="0.35",
             fontsize=7.5, ha="center", va="top")
axr.annotate(r"$s=-R/L$", xy=(-7.0, 0.62), color="0.3", fontsize=8, ha="center")
axr.set_xlim(-11.5, 2.2)
axr.set_ylim(-0.85, 0.85)
axr.set_xlabel(r"$\sigma$  ($10^6$ s$^{-1}$)")
axr.set_ylabel(r"$j\omega$")
axr.set_yticks([0])
axr.grid(False)

save(fig, "rl_worked")
