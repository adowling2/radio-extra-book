"""A quartz crystal's two resonances, and the narrow window between them where a
crystal oscillator actually operates. Top: |Z| falls to R at the series resonance and
rises to megohms at the parallel one. Bottom: the reactance, which is INDUCTIVE only
between the two -- the shaded window. Component values are sec:crystal's worked
example. See sec:crystal."""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_RED

apply_style()

# sec:crystal's worked example: fs placed at exactly 10 MHz
Cm, C0, R = 15e-15, 5e-12, 15.0
fs = 10.0e6
Lm = 1/((2*np.pi*fs)**2*Cm)
fp = fs*np.sqrt(1 + Cm/C0)
gap_ppm = (fp/fs - 1)*1e6

f = np.linspace(fs - 6e3, fs + 26e3, 400000)
w = 2*np.pi*f
Zm = R + 1j*(w*Lm - 1/(w*Cm))          # motional arm
Z = 1/(1/Zm + 1j*w*C0)                 # shunted by the holder capacitance
khz = (f - fs)/1e3                     # x axis: kHz above the series resonance
ks, kp = 0.0, (fp - fs)/1e3

fig, (axm, axx) = plt.subplots(2, 1, figsize=(6.3, 4.0), sharex=True,
                               gridspec_kw={"height_ratios": [1.25, 1]})

for ax in (axm, axx):
    ax.axvspan(ks, kp, color=GUIDE_AMBER, alpha=0.13, zorder=0)

# ---------------- magnitude ----------------
axm.semilogy(khz, np.abs(Z), color=GUIDE_BLUE, zorder=4)
axm.plot([ks], [R], "o", color=GUIDE_GREEN, ms=5, zorder=6)
axm.plot([kp], [np.abs(Z)[np.argmax(np.abs(Z))]], "o", color=GUIDE_RED, ms=5, zorder=6)
axm.annotate(rf"$f_s={fs/1e6:.3f}$ MHz" "\n" rf"$|Z|\approx R={R:.0f}\ \Omega$",
             xy=(ks, R), xytext=(-5.4, 1.1e3), color=GUIDE_GREEN, fontsize=8,
             arrowprops=dict(arrowstyle="->", color=GUIDE_GREEN, lw=0.8))
axm.annotate(rf"$f_p={fp/1e6:.6f}$ MHz" "\n" r"$|Z|$ in megohms",
             xy=(kp, np.abs(Z).max()), xytext=(21.0, 3.0e6), color=GUIDE_RED,
             fontsize=8, ha="center",
             arrowprops=dict(arrowstyle="->", color=GUIDE_RED, lw=0.8))
axm.set_ylabel(r"$|Z|$  ($\Omega$)")
axm.set_ylim(3, 3e7)
axm.set_yticks([10, 1e3, 1e5, 1e7])
axm.set_title(r"One crystal, two resonances "
              rf"${gap_ppm:.0f}$ ppm apart", fontsize=9.5)

# ---------------- reactance ----------------
axx.plot(khz, Z.imag, color=GUIDE_BLUE, zorder=4)
axx.axhline(0, color="0.4", lw=0.8)
axx.set_yscale("symlog", linthresh=100)
axx.set_ylabel(r"$\mathrm{Im}\{Z\}$  ($\Omega$)")
axx.set_xlabel(r"kHz above $f_s$")
axx.set_ylim(-3e6, 3e6)
axx.set_yticks([-1e5, -1e2, 0, 1e2, 1e5])
axx.set_yticklabels([r"$-10^5$", r"$-10^2$", "0", r"$10^2$", r"$10^5$"])
axx.annotate("capacitive", xy=(-4.0, -3e3), color="0.35", fontsize=8)
axx.annotate("capacitive", xy=(19.0, -3e3), color="0.35", fontsize=8)
axx.annotate("INDUCTIVE\nhere only", xy=(ks + (kp - ks)/2, 6e3), color=GUIDE_AMBER,
             fontsize=8, ha="center", fontweight="bold")

# the window, bracketed, with what it is for
axx.annotate("", xy=(ks, -1.3e5), xytext=(kp, -1.3e5),
             arrowprops=dict(arrowstyle="<->", color=GUIDE_AMBER, lw=1.1))
axx.annotate("the entire working range", xy=(7.5, -4.5e5), color=GUIDE_AMBER,
             fontsize=7.8, ha="center", va="center")
axx.set_xlim(khz[0], khz[-1])

save(fig, "crystal_impedance")
