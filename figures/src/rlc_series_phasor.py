"""Impedance of the series-RLC worked example expressed as a phasor.
L = 10 uH, C = 220 pF, R = 5 Ohm, f0 = 3.39 MHz.

Left:  the net impedance at f = 1.1 f0 drawn as a phasor -- rectangular form
       Z = R + jX read off the axes, polar form |Z| and theta read off the arrow.
Right: the locus of Z(f) through resonance: a VERTICAL line (R is constant, only
       the reactance changes) that crosses the real axis at Z = R.
"""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_RED

apply_style()

L = 10e-6
C = 220e-12
R = 5.0
f0 = 1.0/(2*np.pi*np.sqrt(L*C))

# a frequency a little above resonance -> small net inductive reactance
f1 = 1.10*f0
w1 = 2*np.pi*f1
XL = w1*L
XC = 1.0/(w1*C)
X = XL - XC
Zmag = np.hypot(R, X)
Zang = np.degrees(np.arctan2(X, R))

fig, (axv, axs) = plt.subplots(1, 2, figsize=(6.7, 3.2))

# ---------- left: Z as a phasor ----------
axv.axhline(0, color="0.35", lw=0.7)
axv.axvline(0, color="0.35", lw=0.7)
axv.annotate("", xy=(R, X), xytext=(0, 0),
             arrowprops=dict(arrowstyle="-|>", color=GUIDE_RED, lw=2.4))
# rectangular projections
axv.plot([R, R], [0, X], ls=":", color=GUIDE_GREEN, lw=1.1)
axv.plot([0, R], [X, X], ls=":", color=GUIDE_GREEN, lw=1.1)
axv.plot(R, X, "o", color=GUIDE_RED, ms=5, zorder=6)
# angle arc
arc = np.linspace(0, np.radians(Zang), 60)
rr = 11.0
axv.plot(rr*np.cos(arc), rr*np.sin(arc), color=GUIDE_AMBER, lw=1.1)
axv.annotate(rf"$\theta={Zang:.0f}^\circ$", xy=(13.5, 5.5), color=GUIDE_AMBER,
             fontsize=8, ha="left", va="center")
axv.annotate(rf"$|Z|={Zmag:.0f}\,\Omega$", xy=(-3.0, X*0.62),
             color=GUIDE_RED, fontsize=8.5, ha="right", va="center")
axv.annotate(rf"$R={R:g}\,\Omega$", xy=(R, -1.6), color=GUIDE_GREEN, fontsize=8,
             ha="center", va="top")
axv.annotate(rf"$X={X:.0f}\,\Omega$", xy=(R+1.8, X+2.6), color=GUIDE_GREEN,
             fontsize=8, ha="left", va="bottom")
axv.annotate(rf"$X_L={XL:.0f}$, $X_C={XC:.0f}$" "\n"
             rf"$X=X_L-X_C={X:.0f}\,\Omega$",
             xy=(24, 14), color="0.3", fontsize=7.5, ha="left", va="center")
axv.set_xlim(-22, 62)
axv.set_ylim(-9, 53)
axv.set_xlabel(r"resistance ($\Omega$)")
axv.set_ylabel(r"reactance ($\Omega$)")
axv.set_title(r"$Z$ as a phasor at $f=1.1f_0$", fontsize=8.5)
axv.grid(False)

# ---------- right: Z(f) locus through resonance ----------
f = np.linspace(0.50*f0, 2.00*f0, 900)
w = 2*np.pi*f
Z = R + 1j*(w*L - 1.0/(w*C))
axs.axhline(0, color="0.35", lw=0.7)
axs.axvline(0, color="0.35", lw=0.7)
axs.plot(Z.real, Z.imag, color=GUIDE_BLUE, lw=2.2)
axs.plot(R, 0, "o", color=GUIDE_RED, ms=6, zorder=6)
axs.annotate(rf"$f_0$: $Z=R={R:g}\,\Omega$" "\n" r"($|Z|$ at its minimum)",
             xy=(R, 0), xytext=(22, -95), color=GUIDE_RED, fontsize=7.5,
             ha="left", va="center",
             arrowprops=dict(arrowstyle="->", color=GUIDE_RED, lw=0.9))
axs.annotate("inductive\n" r"($f>f_0$)", xy=(16, 250), color=GUIDE_BLUE,
             fontsize=7.5, ha="left", va="center")
axs.annotate("capacitive\n" r"($f<f_0$)", xy=(16, -270), color=GUIDE_AMBER,
             fontsize=7.5, ha="left", va="center")
axs.annotate(r"$R$ is constant, so the" "\n" r"locus is a vertical line",
             xy=(-54, 190), color="0.35", fontsize=7.5, ha="left", va="center")
axs.set_xlim(-58, 80)
axs.set_ylim(-390, 390)
axs.set_xlabel(r"resistance ($\Omega$)")
axs.set_ylabel(r"reactance ($\Omega$)")
axs.set_title(r"$Z(f)$ sweeping through resonance", fontsize=8.5)
axs.grid(False)

fig.tight_layout()
save(fig, "rlc_series_phasor")
