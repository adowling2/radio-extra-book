"""Scope-probe compensation as pole-zero cancellation.
10:1 probe: R1 = 9 Mohm with trimmer C1, into a scope of R2 = 1 Mohm || C2 = 15 pF.

    H(s) = (R2/(R1+R2)) * (1 + s R1 C1) / (1 + s Rpar (C1+C2)),  Rpar = R1||R2

so there is a zero at -1/(R1 C1) and a pole at -1/(Rpar(C1+C2)). They cancel exactly
when R1 C1 = R2 C2, i.e. C1 = 1.67 pF here.

Left:  square-wave (step) response for under-, correctly, and over-compensated C1 --
       the rounded / flat / peaked traces every scope user recognizes.
Right: the same three cases as pole-zero plots, showing that "correctly compensated"
       means the zero has landed exactly on the pole.
"""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_RED

apply_style()

R1, R2, C2 = 9e6, 1e6, 15e-12
Rpar = R1*R2/(R1 + R2)
C1_ok = R2*C2/R1                     # 1.67 pF
K = R2/(R1 + R2)                     # 1/10

cases = [
    (0.80e-12, GUIDE_AMBER, "under-compensated"),
    (C1_ok,    GUIDE_GREEN, "compensated"),
    (3.50e-12, GUIDE_RED,   "over-compensated"),
]

fig, (axt, axp) = plt.subplots(1, 2, figsize=(6.8, 3.1))

# ---------- left: step response, normalized so the flat case sits at 1 ----------
t = np.linspace(0, 60e-6, 1200)
for C1, col, lab in cases:
    tz = R1*C1
    tp = Rpar*(C1 + C2)
    # step response of K(1+tz s)/(1+tp s):  K[1 + (tz/tp - 1) e^{-t/tp}]
    y = K*(1 + (tz/tp - 1)*np.exp(-t/tp))
    axt.plot(t*1e6, y/K, color=col, lw=1.8,
             label=rf"{lab} ($C_1={C1*1e12:.2f}$ pF)")
axt.axhline(1.0, color="0.6", ls=":", lw=0.9)
axt.set_xlabel(r"time ($\mu$s)")
axt.set_ylabel("output / final value")
axt.set_xlim(0, 60)
axt.set_ylim(0.35, 2.05)
axt.legend(loc="upper right", fontsize=7)
axt.set_title("Step response through the probe", fontsize=8.5)

# ---------- right: pole and zero locations ----------
axp.axvline(0, color="0.35", lw=0.7)   # the j-omega axis
for k, (C1, col, lab) in enumerate(cases):
    z = -1.0/(R1*C1)                  # zero
    p = -1.0/(Rpar*(C1 + C2))         # pole
    yy = 1.0 - k                      # rows offset for clarity only
    axp.plot([-14.5, 0.25], [yy, yy], color="0.85", lw=0.7, zorder=0)
    axp.plot(p*1e-4, yy, "x", color=col, ms=11, mew=2.2)
    axp.plot(z*1e-4, yy, "o", mfc="none", mec=col, ms=11, mew=1.8)
    axp.annotate(lab, xy=(0.30, yy), color=col, fontsize=7.5, ha="left",
                 va="center")
axp.annotate(r"$\times$ pole   $\circ$ zero", xy=(-13.6, 1.72), color="0.35",
             fontsize=7.5, ha="left", va="center")
axp.annotate("zero lands exactly\non the pole", xy=(-7.0, 0.0),
             xytext=(-13.6, 0.62), color=GUIDE_GREEN, fontsize=7.5,
             ha="left", va="center",
             arrowprops=dict(arrowstyle="->", color=GUIDE_GREEN, lw=0.9))
axp.set_xlim(-14.5, 3.2)
axp.set_ylim(-1.9, 2.1)
axp.set_xlabel(r"$\sigma$  ($10^4$ s$^{-1}$)")
axp.set_yticks([])
axp.grid(False)
axp.set_title("The same three cases in the s-plane", fontsize=8.5)

fig.tight_layout()
save(fig, "probe_compensation")
