"""RC capacitor-voltage transient: charging and discharging, normalized, with the
one-time-constant marks (63.2% charging, 36.8% discharging)."""
import numpy as np
import matplotlib.pyplot as plt
from _style import apply_style, save, GUIDE_BLUE, GUIDE_GREEN, GUIDE_AMBER

apply_style()

t = np.linspace(0, 5, 400)          # time in units of tau = RC
charge = 1 - np.exp(-t)
discharge = np.exp(-t)

fig, ax = plt.subplots(figsize=(6.2, 3.0))
ax.plot(t, charge, color=GUIDE_BLUE, label=r"charging: $v_C=E\,(1-e^{-t/RC})$")
ax.plot(t, discharge, color=GUIDE_GREEN, label=r"discharging: $v_C=V_0\,e^{-t/RC}$")
ax.axvline(1, color=GUIDE_AMBER, ls="--", lw=0.9)
ax.plot(1, 1-np.exp(-1), "o", color=GUIDE_BLUE, ms=5, zorder=5)
ax.plot(1, np.exp(-1), "o", color=GUIDE_GREEN, ms=5, zorder=5)
ax.annotate(r"$63.2\%$ at $t=RC$", xy=(1, 1-np.exp(-1)), xytext=(1.5, 0.80),
            arrowprops=dict(arrowstyle="->", color="0.35", lw=0.8))
ax.annotate(r"$36.8\%$ at $t=RC$", xy=(1, np.exp(-1)), xytext=(1.5, 0.20),
            arrowprops=dict(arrowstyle="->", color="0.35", lw=0.8))
ax.set_xlabel(r"Time $t/RC$")
ax.set_ylabel(r"Capacitor voltage (normalized)")
ax.set_xlim(0, 5)
ax.set_ylim(0, 1.05)
ax.legend(loc="center right", fontsize=8)

save(fig, "rc_transient")
