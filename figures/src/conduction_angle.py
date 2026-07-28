"""Where the amplifier efficiency numbers come from. Left: the truncated-cosine device
current at three conduction angles, with the DC component each one draws drawn as a
dashed line -- narrowing the conduction angle cuts the DC average faster than it cuts
the fundamental, which is the whole mechanism. Right: efficiency against conduction
angle, with the two exactly-known points marked. See sec:conductionangle."""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_RED

apply_style()


def coeffs(th):
    """DC and fundamental of a cosine truncated at half-angle th, peak normalised."""
    Idc = (np.sin(th) - th*np.cos(th))/(np.pi*(1 - np.cos(th)))
    I1 = (th - np.sin(th)*np.cos(th))/(np.pi*(1 - np.cos(th)))
    return Idc, I1


fig, (axw, axe) = plt.subplots(1, 2, figsize=(6.6, 2.9),
                               gridspec_kw={"width_ratios": [1.25, 1]})

# ---------------- left: the current waveforms ----------------
phi = np.linspace(-np.pi, np.pi, 3000)
cases = [(360, "A", GUIDE_BLUE), (180, "B", GUIDE_GREEN), (120, "C", GUIDE_AMBER)]

for deg, cls, col in cases:
    th = np.radians(deg/2)
    i = np.where(np.abs(phi) <= th,
                 (np.cos(phi) - np.cos(th))/(1 - np.cos(th)), 0.0)
    Idc, _ = coeffs(th)
    axw.plot(np.degrees(phi), i, color=col, lw=1.5,
             label=rf"Class {cls}, $2\theta={deg}^\circ$")
    axw.axhline(Idc, color=col, ls="--", lw=0.9, alpha=0.85)

axw.annotate(r"dashed $=$ the DC component the supply delivers",
             xy=(0, 0.075), color="0.30", fontsize=7.4, ha="center",
             bbox=dict(fc="white", ec="none", pad=1.2))
axw.set_xlabel(r"$\phi$  (degrees of the cycle)")
axw.set_ylabel(r"device current  $i/I_{pk}$")
axw.set_xlim(-180, 180)
axw.set_ylim(-0.06, 1.14)
axw.set_xticks([-180, -90, 0, 90, 180])
axw.legend(loc="upper right", fontsize=7.2)
axw.set_title("Narrow the conduction, cut the DC", fontsize=9)

# ---------------- right: efficiency vs conduction angle ----------------
deg = np.linspace(2, 360, 4000)
ths = np.radians(deg/2)
Idc, I1 = coeffs(ths)
eta = 0.5*I1/Idc                      # tuned load, V1 -> Vdc

axe.plot(deg, 100*eta, color=GUIDE_BLUE, zorder=4)
for d, lab, col in ((360, r"A: $\frac{1}{2}$", GUIDE_BLUE),
                    (180, r"B: $\pi/4$", GUIDE_GREEN)):
    th = np.radians(d/2)
    a, b = coeffs(th)
    e = 100*0.5*b/a
    axe.plot([d], [e], "o", color=col, ms=5.5, zorder=6)
    tx, ty = (268, 44.5) if d == 360 else (98, 58.5)
    axe.annotate(rf"{lab}$={e:.1f}\%$", xy=(d, e), xytext=(tx, ty),
                 color=col, fontsize=8, ha="center",
                 arrowprops=dict(arrowstyle="->", color=col, lw=0.8))

axe.axhline(100, color="0.6", ls=":", lw=0.9)
axe.annotate(r"$\to100\%$ as $2\theta\to0$," "\n" r"but so does the output power",
             xy=(12, 99.3), xytext=(196, 105.5), color=GUIDE_RED, fontsize=7.4,
             ha="center", arrowprops=dict(arrowstyle="->", color=GUIDE_RED, lw=0.8))
axe.set_xlabel(r"conduction angle $2\theta$  (degrees)")
axe.set_ylabel(r"$\eta$  (\%), tuned load")
axe.set_xlim(0, 360)
axe.set_ylim(40, 114)
axe.set_xticks([0, 90, 180, 270, 360])
axe.set_title(r"$\eta=\frac{1}{2}(I_1/I_{\mathrm{dc}})(V_1/V_{\mathrm{dc}})$",
              fontsize=9)

fig.subplots_adjust(wspace=0.33)
save(fig, "conduction_angle")
