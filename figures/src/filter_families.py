"""Magnitude responses of the common analog filter families at the same order,
so the flatness/sharpness/ripple trade-offs are visible side by side."""
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_RED

apply_style()

N = 5           # filter order
wc = 1.0        # normalized cutoff
w = np.logspace(-1, 1, 1000)

designs = [
    ("Butterworth (maximally flat)", signal.butter(N, wc, analog=True), GUIDE_BLUE),
    ("Chebyshev I (1 dB ripple)",    signal.cheby1(N, 1, wc, analog=True), GUIDE_AMBER),
    ("Elliptic (1 dB / 40 dB)",      signal.ellip(N, 1, 40, wc, analog=True), GUIDE_RED),
    ("Bessel (linear phase)",        signal.bessel(N, wc, analog=True, norm='mag'), GUIDE_GREEN),
]

fig, ax = plt.subplots(figsize=(6.4, 3.4))
for label, (b, a), color in designs:
    _, h = signal.freqs(b, a, worN=w)
    ax.semilogx(w, 20*np.log10(np.abs(h)), color=color, label=label)

ax.axhline(-3.0103, color="0.6", ls=":", lw=0.9)
ax.axvline(1.0, color="0.6", ls=":", lw=0.9)
ax.set_xlabel(r"Normalized frequency $\omega/\omega_c$")
ax.set_ylabel("Magnitude (dB)")
ax.set_ylim(-70, 8)
ax.set_xlim(0.1, 10)
ax.legend(loc="lower left", fontsize=8)
ax.set_title(f"Order-{N} low-pass filter families", fontsize=10)

save(fig, "filter_families")
