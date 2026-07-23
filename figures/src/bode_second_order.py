"""Second-order low-pass Bode magnitude for several quality factors, showing
the resonant peak grow as Q increases (poles approach the jw axis)."""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_RED

apply_style()

w0 = 1.0
w = np.logspace(-1, 1, 600)
Qs = [(0.5, GUIDE_GREEN), (0.707, GUIDE_AMBER), (2.0, GUIDE_BLUE), (5.0, GUIDE_RED)]

fig, ax = plt.subplots(figsize=(6.2, 3.0))
for Q, c in Qs:
    # H(jw) = w0^2 / (w0^2 - w^2 + j w w0 / Q)
    H = w0**2 / ((w0**2 - w**2) + 1j*w*w0/Q)
    ax.semilogx(w, 20*np.log10(np.abs(H)), color=c,
                label=rf"$Q={Q:g}$ ($\zeta={1/(2*Q):.2f}$)")
ax.axhline(0, color="0.6", ls=":", lw=0.9)
ax.axvline(1, color="0.6", ls=":", lw=0.9)
ax.set_xlabel(r"Normalized frequency $\omega/\omega_0$")
ax.set_ylabel("Magnitude (dB)")
ax.set_ylim(-40, 18)
ax.legend(loc="lower left", fontsize=8)

save(fig, "bode_second_order")
