"""Second-order step responses across damping regimes (over/critical/under),
normalized to the natural frequency omega_0 = 1."""
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER, GUIDE_RED

apply_style()

w0 = 1.0
t = np.linspace(0, 16, 600)
cases = [
    (0.1, GUIDE_RED,   r"$\zeta=0.1$ (underdamped, high $Q$)"),
    (0.4, GUIDE_BLUE,  r"$\zeta=0.4$ (underdamped)"),
    (1.0, GUIDE_AMBER, r"$\zeta=1$ (critical)"),
    (2.0, GUIDE_GREEN, r"$\zeta=2$ (overdamped)"),
]

fig, ax = plt.subplots(figsize=(6.2, 3.2))
for zeta, color, label in cases:
    sys = signal.TransferFunction([w0**2], [1, 2*zeta*w0, w0**2])
    _, y = signal.step(sys, T=t)
    ax.plot(t, y, color=color, label=label)
ax.axhline(1.0, color="0.55", ls=":", lw=1.0)
ax.set_xlabel(r"Time $\omega_0 t$")
ax.set_ylabel(r"Step response $y(t)$")
ax.set_xlim(0, 16)
ax.set_ylim(0, 2.0)
ax.legend(loc="upper right")

save(fig, "step_second_order")
