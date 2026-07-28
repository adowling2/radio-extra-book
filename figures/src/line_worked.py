"""The transmission-line worked example: a 100 Ohm load on a 50 Ohm line,
matched by a quarter-wave section of Z_t = 70.7 Ohm at f0 = 14.1 MHz.

Left:  standing-wave envelope |V(x)| along the UNMATCHED line, showing
       Vmax/Vmin = SWR = 2 and the quarter-wave spacing of the extremes.
Right: SWR versus frequency for the quarter-wave-matched line -- perfect only at
       f0, degrading away from it, which is what "narrowband match" means.
"""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_RED, GUIDE_LINE

apply_style()

Z0 = 50.0
ZL = 100.0
f0 = 14.1e6
Zt = np.sqrt(Z0*ZL)          # 70.71 ohm quarter-wave section

fig, (axs, axf) = plt.subplots(1, 2, figsize=(6.8, 3.0))

# ---------- left: standing-wave envelope on the unmatched line ----------
G = (ZL - Z0)/(ZL + Z0)      # = 1/3, real and positive
x = np.linspace(0, 1.25, 900)                 # position back from load, in wavelengths
env = np.abs(1 + G*np.exp(-1j*2*(2*np.pi)*x))  # |1 + G e^{-j2 beta x}|, beta x = 2pi x
axs.plot(x, env, color=GUIDE_BLUE, lw=2.0)
vmax, vmin = 1 + abs(G), 1 - abs(G)
axs.axhline(vmax, color=GUIDE_LINE, ls="--", lw=0.8)
axs.axhline(vmin, color=GUIDE_LINE, ls="--", lw=0.8)
axs.annotate(rf"$V_{{\max}}={vmax:.2f}$", xy=(1.30, vmax+0.05), color="0.35",
             fontsize=7.5, ha="left", va="center")
axs.annotate(rf"$V_{{\min}}={vmin:.2f}$", xy=(1.30, vmin-0.05), color="0.35",
             fontsize=7.5, ha="left", va="center")
axs.annotate(rf"SWR $=\dfrac{{V_{{\max}}}}{{V_{{\min}}}}={vmax/vmin:.0f}$",
             xy=(0.63, 1.49), color=GUIDE_RED, fontsize=8.5, ha="center",
             va="center")
# mark the quarter-wave spacing between a max and the next min
axs.annotate("", xy=(0.0, 0.80), xytext=(0.25, 0.80),
             arrowprops=dict(arrowstyle="<->", color=GUIDE_AMBER, lw=1.1))
axs.annotate(r"$\lambda/4$", xy=(0.125, 0.84), color=GUIDE_AMBER, fontsize=8,
             ha="center", va="bottom")
axs.set_xlabel(r"distance back from load, $x/\lambda$")
axs.set_ylabel(r"$|V(x)|$  (normalized to $|V^+|$)")
axs.set_xlim(0, 1.62)
axs.set_ylim(0.55, 1.60)
axs.set_title(r"Standing wave: $100\,\Omega$ on a $50\,\Omega$ line", fontsize=8.5)

# ---------- right: SWR(f) of the quarter-wave match ----------
f = np.linspace(0.4*f0, 1.6*f0, 1200)
# electrical length of the section: 90 deg at f0
bl = (np.pi/2)*(f/f0)
Zin = Zt*(ZL + 1j*Zt*np.tan(bl))/(Zt + 1j*ZL*np.tan(bl))
Gin = (Zin - Z0)/(Zin + Z0)
swr = (1 + np.abs(Gin))/(1 - np.abs(Gin))
axf.plot(f/1e6, swr, color=GUIDE_BLUE, lw=2.0)
axf.axhline((1 + abs(G))/(1 - abs(G)), color=GUIDE_AMBER, ls="--", lw=1.1)
axf.annotate(r"no matching: SWR $=2$", xy=(6.2, 2.06), color=GUIDE_AMBER,
             fontsize=7.5, ha="left", va="bottom")
axf.annotate("quarter-wave\nmatched", xy=(19.2, 1.17), color=GUIDE_BLUE,
             fontsize=7.5, ha="center", va="center")
axf.plot(f0/1e6, 1.0, "o", color=GUIDE_RED, ms=6, zorder=6)
axf.annotate(rf"perfect match only at $f_0$" "\n" rf"($Z_t={Zt:.1f}\,\Omega$)",
             xy=(f0/1e6, 1.0), xytext=(f0/1e6, 1.62), color=GUIDE_RED, fontsize=7.5,
             ha="center", va="center",
             arrowprops=dict(arrowstyle="->", color=GUIDE_RED, lw=0.9))
axf.set_xlabel(r"Frequency (MHz),  $f_0=14.1$ MHz")
axf.set_ylabel("SWR")
axf.set_xlim(f[0]/1e6, f[-1]/1e6)
axf.set_ylim(0.98, 2.40)
axf.set_title("The match is narrowband", fontsize=8.5)

fig.tight_layout()
save(fig, "line_worked")
