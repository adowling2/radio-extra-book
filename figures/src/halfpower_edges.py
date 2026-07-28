"""The half-power bandwidth, drawn twice: as a width on the frequency response and
as a distance in the s-plane. Left panel shows that on a LOG frequency axis the
resonance sits exactly midway between the two -3 dB edges, which is the geometric
mean f0 = sqrt(f1 f2). Right panel shows the same bandwidth as 2*alpha, twice the
pole pair's distance from the jw axis. See sec:halfpower."""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_RED

apply_style()

Q = 1.5                      # low enough that the band is wide and readable
r = 1/(2*Q) + np.sqrt(1 + 1/(4*Q**2))
f1, f2 = 1.0/r, 1.0*r        # band edges, in units of f0

fig, (axL, axR) = plt.subplots(1, 2, figsize=(6.5, 2.9),
                               gridspec_kw={"width_ratios": [1.35, 1]})

# ---------------- left: current response on a log frequency axis ----------------
f = np.logspace(np.log10(0.2), np.log10(5.0), 4000)
D = f - 1.0/f                                   # detuning w/w0 - w0/w
mag = 1.0/np.sqrt(1 + (Q*D)**2)                 # |I|/I_max

axL.semilogx(f, mag, color=GUIDE_BLUE, zorder=4)
axL.axhline(1/np.sqrt(2), color=GUIDE_RED, ls="--", lw=1.0, zorder=2)
axL.annotate(r"$1/\sqrt{2}$  (half power)", xy=(0.215, 1/np.sqrt(2)),
             xytext=(0.215, 0.78), color=GUIDE_RED, fontsize=8)

for x, lab, col in ((f1, r"$f_1$", GUIDE_GREEN), (f2, r"$f_2$", GUIDE_GREEN)):
    axL.plot([x, x], [0, 1/np.sqrt(2)], color=col, lw=1.0, ls=":", zorder=3)
    axL.annotate(lab, xy=(x, 0.055), color=col, ha="center", fontsize=9)
axL.plot([1, 1], [0, 1], color=GUIDE_AMBER, lw=1.0, ls=":", zorder=3)
axL.annotate(r"$f_0$", xy=(1, 0.055), color=GUIDE_AMBER, ha="center", fontsize=9)

# brackets showing EQUAL spacing on the log axis, both sides of f0
ybr = 1.045
for a, b in ((f1, 1.0), (1.0, f2)):
    axL.annotate("", xy=(a, ybr), xytext=(b, ybr),
                 arrowprops=dict(arrowstyle="<->", color="0.30", lw=0.9))
axL.annotate("equal spacing on a log axis", xy=(1, ybr + 0.055), color="0.25",
             ha="center", fontsize=8.5)
axL.annotate(r"$\Rightarrow\ f_0=\sqrt{f_1f_2}$", xy=(1.62, 0.40), color="0.25",
             ha="left", fontsize=9.5)

axL.set_xlim(0.2, 5.0)
axL.set_ylim(0, 1.22)
axL.set_xlabel(r"$f/f_0$  (log scale)")
axL.set_ylabel(r"$|I|/I_{\max}$")
axL.set_xticks([0.2, 0.5, 1, 2, 5])
axL.set_xticklabels(["0.2", "0.5", "1", "2", "5"])
axL.set_yticks([0, 0.5, 1/np.sqrt(2), 1.0])
axL.set_yticklabels(["0", "0.5", "0.707", "1"])
axL.set_title(r"$BW=f_2-f_1=f_0/Q$   (exactly)", fontsize=9)

# ---------------- right: the same bandwidth in the s-plane ----------------
w0 = 1.0
alpha = w0/(2*Q)
wd = np.sqrt(max(0.0, w0**2 - alpha**2))

th = np.linspace(0, 2*np.pi, 400)
axR.plot(w0*np.cos(th), w0*np.sin(th), color="0.7", ls="--", lw=0.9)
axR.plot([-alpha, -alpha], [wd, -wd], "o", color=GUIDE_BLUE, ms=6, zorder=5)
axR.axhline(0, color="0.3", lw=0.7)
axR.axvline(0, color="0.3", lw=0.7)

# the alpha distance, drawn on both poles, with a guide line at sigma = -alpha
axR.plot([-alpha, -alpha], [-1.3, 1.3], color=GUIDE_RED, ls=":", lw=0.9, zorder=1)
for sgn in (+1, -1):
    axR.annotate("", xy=(0, sgn*wd), xytext=(-alpha, sgn*wd),
                 arrowprops=dict(arrowstyle="<->", color=GUIDE_RED, lw=1.1))
    axR.annotate(r"$\alpha$", xy=(-alpha/2, sgn*wd + (0.10 if sgn > 0 else -0.22)),
                 color=GUIDE_RED, ha="center", fontsize=9)
axR.annotate(r"$BW=2\alpha=\omega_0/Q$", xy=(-1.19, 1.34),
             color=GUIDE_RED, ha="left", va="center", fontsize=9)
axR.annotate(r"$|s|=\omega_0$", xy=(-1.19, -1.30), color="0.45", ha="left",
             va="center", fontsize=8)

axR.set_xlabel(r"$\sigma$ (real)")
axR.set_ylabel(r"$j\omega$ (imag)")
axR.set_xlim(-1.25, 0.32)
axR.set_ylim(-1.52, 1.52)
axR.set_aspect("equal")
axR.set_title("distance from the axis is half of it", fontsize=9)

save(fig, "halfpower_edges")
