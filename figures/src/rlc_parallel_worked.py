"""Parallel RLC worked example: L = 10 uH, C = 220 pF, R = 18 kOhm.
f0 = 3.39 MHz (same L, C as the series example), Qp = R/(w0 L) ~ 84.

Left:  |Z(f)| of the tank in ohms -- a PEAK at f0 reaching R, the mirror of the
       series circuit's dip. Log-log so the +/-20 dB/decade skirts are straight.
Right: the same information as the impedance phasor locus: parallel R fixes the
       conductance, so it is the ADMITTANCE that traces a vertical line, and Z
       traces a circle through the origin.
"""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_RED

apply_style()

L = 10e-6
C = 220e-12
R = 18e3
w0 = 1.0/np.sqrt(L*C)
f0 = w0/(2*np.pi)
Qp = R/(w0*L)
BW = f0/Qp

fig, (axm, axz) = plt.subplots(1, 2, figsize=(6.8, 3.1))

# ---------- left: |Z(f)| of the tank ----------
f = np.logspace(np.log10(f0) - 1.3, np.log10(f0) + 1.3, 1600)
w = 2*np.pi*f
Y = 1.0/R + 1j*(w*C - 1.0/(w*L))
Z = 1.0/Y
axm.loglog(f/1e6, np.abs(Z), color=GUIDE_BLUE, lw=1.9)
axm.axvline(f0/1e6, color=GUIDE_AMBER, ls=":", lw=1.1)
axm.plot(f0/1e6, R, "o", color=GUIDE_RED, ms=6, zorder=6)
axm.annotate(rf"$f_0$: $|Z|=R={R/1e3:.0f}$ k$\Omega$" "\n"
             rf"(maximum, purely real)",
             xy=(f0/1e6, R), xytext=(0.20, 2.6e3), color=GUIDE_RED, fontsize=7.5,
             ha="left", va="center",
             arrowprops=dict(arrowstyle="->", color=GUIDE_RED, lw=0.9))
# half-power points
axm.axhline(R/np.sqrt(2), color="0.6", ls="--", lw=0.8)
axm.annotate(rf"$-3$ dB: $BW\approx{BW/1e3:.0f}$ kHz",
             xy=(0.20, R/np.sqrt(2)*1.18), color="0.35", fontsize=7.5,
             ha="left", va="bottom")
axm.set_xlabel(r"Frequency (MHz)")
axm.set_ylabel(r"$|Z|$ ($\Omega$)")
axm.set_ylim(2e1, 6e4)
axm.set_title(r"Tank impedance peaks at $f_0$", fontsize=8.5)

# ---------- right: Y(f) and Z(f) loci ----------
fz = np.linspace(0.55*f0, 1.9*f0, 900)
wz = 2*np.pi*fz
Yz = 1.0/R + 1j*(wz*C - 1.0/(wz*L))
Zz = 1.0/Yz
axz.axhline(0, color="0.35", lw=0.7)
axz.axvline(0, color="0.35", lw=0.7)
axz.plot(Zz.real/1e3, Zz.imag/1e3, color=GUIDE_BLUE, lw=2.0)
axz.plot(R/1e3, 0, "o", color=GUIDE_RED, ms=6, zorder=6)
axz.annotate(rf"$f_0$: $Z=R$", xy=(R/1e3, 0), xytext=(11.0, 6.4),
             color=GUIDE_RED, fontsize=7.5, ha="center", va="center",
             arrowprops=dict(arrowstyle="->", color=GUIDE_RED, lw=0.9))
axz.annotate("inductive\n" r"($f<f_0$)", xy=(3.7, 4.6), color=GUIDE_AMBER,
             fontsize=7.5, ha="left", va="center")
axz.annotate("capacitive\n" r"($f>f_0$)", xy=(3.7, -5.2), color=GUIDE_BLUE,
             fontsize=7.5, ha="left", va="center")
axz.annotate(r"$Z(f)$ traces a circle" "\n" r"through the origin",
             xy=(-2.8, 8.4), color="0.35", fontsize=7.5, ha="left", va="center")
axz.set_xlim(-3.0, 21.0)
axz.set_ylim(-10.5, 10.5)
axz.set_xlabel(r"$\Re\{Z\}$ (k$\Omega$)")
axz.set_ylabel(r"$\Im\{Z\}$ (k$\Omega$)")
axz.set_title(r"$Z(f)$ in the complex plane", fontsize=8.5)
axz.grid(False)

fig.tight_layout()
save(fig, "rlc_parallel_worked")
