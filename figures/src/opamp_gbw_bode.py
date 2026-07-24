"""Op-amp gain-bandwidth product. A single-pole open-loop gain A(s)=A0/(1+s/wa)
is closed with several feedback fractions beta. Each closed-loop response is flat
at 1/beta then rolls off along the SAME open-loop skirt, so (gain x bandwidth) is
constant and equals the unity-gain frequency f_T."""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_LINE

apply_style()

A0 = 1e5            # 100 dB open-loop DC gain
fa = 10.0           # open-loop corner, Hz
fT = A0*fa          # gain-bandwidth product = 1 MHz

f = np.logspace(0, 7, 800)
s = 1j*f
A = A0/(1 + s/fa)

def dB(x):
    return 20*np.log10(np.abs(x))

fig, ax = plt.subplots(figsize=(6.4, 3.4))
ax.semilogx(f, dB(A), color=GUIDE_BLUE, lw=2.0, label=r"open loop $A(s)$")

betas = [(1.0, GUIDE_GREEN, r"$\beta=1$  (gain 1)"),
         (1e-2, GUIDE_AMBER, r"$\beta=10^{-2}$  (gain 100)"),
         (1e-3, "0.45", r"$\beta=10^{-3}$  (gain 1000)")]
for beta, col, lab in betas:
    Acl = A/(1 + A*beta)
    ax.semilogx(f, dB(Acl), color=col, lw=1.5, label=lab)

ax.axhline(0, color="0.6", lw=0.7)
ax.plot(fT, 0, "o", color=GUIDE_BLUE, ms=5, zorder=6)
ax.annotate(r"$f_T=A_0 f_a$ (unity-gain freq)", xy=(fT, 0), xytext=(3e3, 22),
            color="0.3", fontsize=8,
            arrowprops=dict(arrowstyle="->", color="0.4", lw=0.8))
ax.annotate("gain $\\times$ bandwidth\n= $f_T$ = const", xy=(3e2, 40),
            color="0.3", fontsize=8, ha="center")

ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Magnitude (dB)")
ax.set_xlim(1, 1e7)
ax.set_ylim(-20, 110)
ax.legend(loc="upper right", fontsize=8)

save(fig, "opamp_gbw_bode")
